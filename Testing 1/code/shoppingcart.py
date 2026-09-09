# ─────────────────────────────────────────────────────────────────────────────
# shoppingcart.py
# A simple shopping cart implementation covering:
#   Product, ProductCatalog, ShoppingCart, discount rules, and CheckoutService
# ─────────────────────────────────────────────────────────────────────────────


# ── Product ───────────────────────────────────────────────────────────────────

class Product:
    """A single product in the catalogue."""

    def __init__(self, id: int, name: str, price: float, category: str):
        self.id = id
        self.name = name
        self.price = price
        self.category = category

    def __repr__(self):
        return f"Product({self.id}, {self.name!r}, £{self.price}, {self.category!r})"


# ── ProductCatalog ────────────────────────────────────────────────────────────

class ProductCatalog:
    """Stores all available products and provides look-up helpers."""

    def __init__(self):
        self._products: dict[int, Product] = {}   # keyed by product id for O(1) look-up

    def add_product(self, product: Product) -> None:
        """Add a product to the catalogue."""
        self._products[product.id] = product

    def get_product(self, product_id: int) -> Product:
        """Return a product by id, or raise KeyError if not found."""
        if product_id not in self._products:
            raise KeyError(f"Product with id {product_id} not found")
        return self._products[product_id]

    def get_products_by_category(self, category: str) -> list[Product]:
        """Return all products that belong to the given category."""
        return [p for p in self._products.values() if p.category == category]

    def search_products(self, query: str) -> list[Product]:
        """Case-insensitive search across product names."""
        query_lower = query.lower()
        return [p for p in self._products.values() if query_lower in p.name.lower()]


# ── ShoppingCart ──────────────────────────────────────────────────────────────

class ShoppingCart:
    """
    Holds items a customer intends to buy.
    Each item is stored as {"product": Product, "quantity": int}.
    """

    def __init__(self, catalog: ProductCatalog):
        self._catalog = catalog
        self._items: dict[int, dict] = {}   # keyed by product_id for easy look-up

    # ── mutation ──────────────────────────────────────────────────────────────

    def add_item(self, product_id: int, quantity: int = 1) -> None:
        """
        Add `quantity` of a product to the cart.
        Raises KeyError if the product doesn't exist in the catalogue.
        Raises ValueError if quantity is not a positive integer.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        product = self._catalog.get_product(product_id)   # raises KeyError if missing

        if product_id in self._items:
            self._items[product_id]["quantity"] += quantity   # increment existing line
        else:
            self._items[product_id] = {"product": product, "quantity": quantity}

    def remove_item(self, product_id: int, quantity: int = None) -> None:
        """
        Remove an item from the cart.
        If quantity is given, reduce by that amount (removing the line if it hits 0).
        If quantity is None, remove the entire line regardless of current quantity.
        Raises KeyError if the product is not in the cart.
        """
        if product_id not in self._items:
            raise KeyError(f"Product {product_id} is not in the cart")

        if quantity is None:
            del self._items[product_id]   # remove the whole line
        else:
            self._items[product_id]["quantity"] -= quantity
            if self._items[product_id]["quantity"] <= 0:
                del self._items[product_id]   # drop the line if quantity reaches zero

    def update_quantity(self, product_id: int, quantity: int) -> None:
        """
        Set the quantity of an item directly.
        Setting quantity to 0 removes the item from the cart entirely.
        """
        if product_id not in self._items:
            raise KeyError(f"Product {product_id} is not in the cart")

        if quantity == 0:
            del self._items[product_id]
        else:
            self._items[product_id]["quantity"] = quantity

    def clear(self) -> None:
        """Remove all items from the cart."""
        self._items.clear()

    # ── read-only helpers ─────────────────────────────────────────────────────

    def get_items(self) -> list[dict]:
        """Return all cart lines as a list of {"product": ..., "quantity": ...} dicts."""
        return list(self._items.values())

    def get_total(self) -> float:
        """Return the sum of (price × quantity) for every line in the cart."""
        return sum(
            item["product"].price * item["quantity"]
            for item in self._items.values()
        )


# ── Discount Rules ────────────────────────────────────────────────────────────

class PercentageDiscount:
    """
    Applies a flat percentage discount to the entire cart total.
    Optionally requires a minimum cart value before the discount kicks in.
    """

    def __init__(self, percentage: float, minimum_order: float = 0):
        if not (0 <= percentage <= 100):
            raise ValueError(f"Percentage must be between 0 and 100, got {percentage}")
        self.percentage = percentage
        self.minimum_order = minimum_order

    def apply(self, cart: ShoppingCart) -> float:
        """Return the discount amount (0 if the cart total is below minimum_order)."""
        total = cart.get_total()
        if total < self.minimum_order:
            return 0                                  # minimum not reached - no discount
        return round(total * self.percentage / 100, 2)


class CategoryDiscount:
    """
    Applies a percentage discount only to items that belong to a specific category.
    """

    def __init__(self, category: str, percentage: float):
        if not (0 <= percentage <= 100):
            raise ValueError(f"Percentage must be between 0 and 100, got {percentage}")
        self.category = category
        self.percentage = percentage

    def apply(self, cart: ShoppingCart) -> float:
        """Return the discount amount calculated only on matching category items."""
        category_total = sum(
            item["product"].price * item["quantity"]
            for item in cart.get_items()
            if item["product"].category == self.category
        )
        return round(category_total * self.percentage / 100, 2)


# ── PaymentGateway ────────────────────────────────────────────────────────────

class PaymentGateway:
    """
    Represents an external payment processor (e.g. Stripe, PayPal).
    In tests this is replaced with a MagicMock so no real money moves.
    """

    def process_payment(self, amount: float, payment_details: dict) -> dict:
        """
        Submit a payment request to the external gateway.
        Returns {"success": bool, "transaction_id": str}.
        In production this would make a real API call.
        """
        raise NotImplementedError("Implement with a real payment provider")


# ── CheckoutService ───────────────────────────────────────────────────────────

class CheckoutService:
    """
    Orchestrates the checkout flow:
      1. Calculate the discounted total
      2. Charge the customer via the payment gateway
      3. Clear the cart on success
    """

    def __init__(self, cart: ShoppingCart,
                 discounts: list = None,
                 payment_gateway: PaymentGateway = None):
        self.cart = cart
        self.discounts = discounts or []          # list of discount rule objects
        self.payment_gateway = payment_gateway    # can be None for total-only calculations

    def calculate_total(self) -> float:
        """
        Return the cart total after applying all discount rules.
        Each discount rule's apply() returns a discount amount; we subtract them all.
        """
        gross = self.cart.get_total()
        total_discount = sum(d.apply(self.cart) for d in self.discounts)
        return round(gross - total_discount, 2)

    def checkout(self, payment_details: dict) -> dict:
        """
        Charge the customer and, on success, clear the cart.
        Returns the gateway response enriched with the final total.
        Raises RuntimeError if no payment gateway has been configured.
        """
        if self.payment_gateway is None:
            raise RuntimeError("No payment gateway configured")

        total = self.calculate_total()

        # Delegate the actual charge to the gateway (mocked in tests)
        result = self.payment_gateway.process_payment(total, payment_details)

        if result.get("success"):
            self.cart.clear()   # only clear the cart after a confirmed successful payment

        # Merge our total into the gateway response so the caller gets one clean dict
        return {**result, "total": total}
