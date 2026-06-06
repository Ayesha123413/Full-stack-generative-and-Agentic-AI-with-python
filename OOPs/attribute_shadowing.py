class Chai:
    temperature="hot"
    strength="strong"


cutting=Chai()
print(f"cutting.temperature: {cutting.temperature}")  # Output: hot

cutting.temperature="cold"
print(f"After changing temperature of cutting: {cutting.temperature}")  # Output: cold
print(f"before changing temperature of cutting: {Chai.temperature}")  # Output: hot

del cutting.temperature
print(f"After deleting temperature of cutting: {cutting.temperature}")  # Output: hot

# this is attriute shadowing where we have same attribute name in class and object. when we change the value of attribute in object it will not change the value of attribute in class. and when we delete the attribute from object it will access the attribute from class.