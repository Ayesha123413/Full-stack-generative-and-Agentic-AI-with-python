class Chai:
    pass

class ChaiType:
    pass


print(type(Chai))  # Output: <class 'type'>

ginger_tea = Chai()
print(type(ginger_tea))  # Output: <class '__main__.Chai'>
print(type(ginger_tea) is Chai)  # Output: True
print(type(ginger_tea) is ChaiType)  # Output: False