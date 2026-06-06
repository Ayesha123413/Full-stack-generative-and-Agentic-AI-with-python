class Chai:
    origin="Pakistan"


print(Chai.origin)  # Output: Pakistan
Chai.is_hot=True
print(Chai.is_hot)  # Output: True

# creating object of class

masala=Chai()
print(f"masala.origin: {masala.origin}")  # Output: Pakistan
print(f"masala.is_hot: {masala.is_hot}")  # Output: True


masala.is_hot=False
print(f"masala.is_hot: {masala.is_hot}")  # Output: False
print(f"Chai.is_hot: {Chai.is_hot}")  # Output: True

masala.is_sweet=True
print(f"masala.is_sweet: {masala.is_sweet}")  # Output: True

# print("masala object properties: ", masala.__dict__)  # Output: {'is_hot': False, 'is_sweet': True}