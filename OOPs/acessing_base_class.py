class Chai:
    def __init__(self,type_,strength):
        self.type=type_
        self.strength=strength
        pass


# Duplication
# class MasalaChai(Chai):
#     def __init__(self,type_,strength,spice_level):
#         self.type=type_
#         self.strength=strength
#         self.spice_level=spice_level
#         pass



# Expilcit call 
# class MasalaChai(Chai):
#     def __init__(self, type_, strength,spice_level):
#         Chai.__init__(self, type_, strength) 
#         self.spice_level=spice_level



# super 
class MasalaChai(Chai):
    def __init__(self, type_, strength,spice_level):
        super().__init__(type_, strength)
        self.spice_level=spice_level
