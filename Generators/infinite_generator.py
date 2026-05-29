def infinite_chai():
    """A generator that yields an infinite sequence of natural numbers."""
    n = 1
    while True:
        yield f"refill # {n}"
        n += 1


refill=infinite_chai()

user2=infinite_chai()

for _ in range(5):
    print(next(refill))

for _ in range(3):
    print(next(user2))