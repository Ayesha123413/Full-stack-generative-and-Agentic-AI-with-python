
def print_order():
    # global chai_type
    chai_type="Cardamom"
    def print_chai():
        nonlocal chai_type
        chai_type="Ginger"
        def print_chai_type():
            # global chai_type
            chai_type="Saffron"
            def print_chai2():
                nonlocal chai_type
                chai_type="Mint"
            print_chai2()
            print(f"Your order is = {chai_type}.")
        print_chai_type()
    print_chai()
    print(f"Your order is: {chai_type}.")
       
   
   
    



chai_type="cinamon"
print_order()
print(f"Your order is {chai_type}.")