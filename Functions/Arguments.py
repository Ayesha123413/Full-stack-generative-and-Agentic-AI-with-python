

# def ingredient_print(*ingredients,**extras): next one is same and used by programmers 
def ingredient_print(*args,**kwargs): # args =positional argumenets and kwargs= keyword arguments, can give any name to arguments but these are convention
    print("The ingredients are:",args,"and the extras are:",kwargs)
  
ingredient_print("milk","sugar","cardamom",topping="chocolate",sweetener="honey")