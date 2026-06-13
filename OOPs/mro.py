class A:
    label ="A: masala chai"

class B:
    label="B: ginger chai"

class C:
    label="C: lemon chai"

# class D(B,C):
class D(C,B):
    pass

cup=D()
print(cup.label)