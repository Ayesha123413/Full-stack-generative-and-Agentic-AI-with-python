class InvalidChaiError(Exception): pass

def bill(flavor,cup):
    menu={"masala":20,"ginger":40}
    try:
        if flavor not in menu:
            raise InvalidChaiError("This flavor does not exist!")
            # print("this is ypur bill")
        if not isinstance(cup,int):
            raise TypeError("cup should be an integer ")
        total=menu[flavor] * cup
        print(f"you bill for {cup} of {flavor} is : {total} rupess")
    except  Exception as e :
        print(f"Error : {e}")
    finally:
        print("thank you for visiting us:)")


bill("mint",2)
bill("ginger","two")
bill("masala",3)
