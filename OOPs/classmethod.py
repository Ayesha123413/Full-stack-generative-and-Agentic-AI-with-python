class Chai:
    def __init__(self,tea_type,strength,size):
        self.tea_type=tea_type
        self.strength=strength
        self.size=size
        pass

    @classmethod
    def from_dict(cls,order_data):
        return cls(
            order_data["tea_type"],
            order_data["strength"],
            order_data["size"],
        )
                       
    @classmethod
    def from_string(cls,order_string):
        tea_type,strength,size=order_string.split("-")
        return cls(tea_type,strength,size)
    

class ClassUtils:
    @staticmethod
    def check_in_size(size):
        return size in ["small","medium","large"]
    

print(ClassUtils.check_in_size("small"))

order1=Chai.from_dict({
    "tea_type":"masala",
    "strength":"strong",
    "size":"large"
})

order2=Chai.from_string("ginger-mild-small")

order3=Chai("green", "strong","extralarger")

print(order1.__dict__)
print(order2,order2.__dict__)
print(order3.__dict__)