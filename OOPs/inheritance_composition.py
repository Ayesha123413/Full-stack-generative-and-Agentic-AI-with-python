class BaseClass:
    def __init__(self,type_):
        self.type=type_
    
    def prepare(self):
        print(f"prepare {self.type} chai...") 


class MasalaChai(BaseClass):
    def add_spices(self):
        print("adding cardamom, ginger & cloves")

class ChaiShop:
    cls_var=BaseClass

    def __init__(self):
        self.chai=self.cls_var("Regular")
    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare


class FancyChaiShop(ChaiShop):
    cls_var=MasalaChai


shop=ChaiShop()
fancy=FancyChaiShop()
masala=MasalaChai("special") #bcz masala class inherited from base class and base class expect an arg for type_

shop.serve()
fancy.serve()
fancy.chai.add_spices()
masala.add_spices()
