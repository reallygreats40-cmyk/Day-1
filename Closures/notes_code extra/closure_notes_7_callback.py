"""
Closures Notes Section 7: Lightweight Callbacks and Event Hooks
Demonstrating how closures maintain contextual configuration state for events.
"""

def register_click_handler(button_id, action_name):
    # Closure captures configuration metadata dynamically
    def click_callback():
        print(f"[BUTTON CLICK] Action '{action_name}' executed on button '{button_id}'.")
    return click_callback

def main():
    # Register event handlers with dynamic context
    save_button = register_click_handler("btn_save", "Save Draft")
    cancel_button = register_click_handler("btn_cancel", "Discard Changes")
    
    # Simulate UI event trigger dispatch loops
    save_button()
    cancel_button()

if __name__ == "__main__":
    main()
