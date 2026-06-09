class ChaiOrder:
    price=100
    def __init__(self,type_,size): # weput undescore to avoid conflict with reserved keyword 'type', this is best practice
        self.type=type_
        self.size=size
    
    def summary(self):
        return f"Order: {self.size} {self.type} chai. Price: ${self.price}"
    

order1=ChaiOrder("Masala","Large")
print(order1.summary())

order2=ChaiOrder("Green","Medium")
print(order2.summary())