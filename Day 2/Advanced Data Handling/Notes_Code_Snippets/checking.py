def square(x):
    print(f"  computing {x} * {x}")
    return x * x

gen = (square(x) for x in range(3))
print("Generator created: nothing computed yet")

print("Asking for first value...")
print(next(gen))

print("Asking for second value...")
print(next(gen))