class Tealeaf:
    def __init__(self, age):
        self._age=age


    # getter for age 
    @property
    def age(self):
        print("getter called")
        return self._age
    
    # setter for age 
    @age.setter
    def age(self,value):
        print("setter called ")
        if value<=0:
            raise ValueError("age is not valid")
        else:
          self._age=value
          return self._age


leaf=Tealeaf("20")
print(leaf.aged)
leaf.age=10
print(f"set age = {leaf.age}")


    



