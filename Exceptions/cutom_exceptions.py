class OutOfIngridentsError(Exception):
    pass

def brew_tea(milk,sugar):
    if milk==0 or sugar==0:
        raise OutOfIngridentsError("we cannot make chai...")
    print("chai is ready to server")

brew_tea(0,1)