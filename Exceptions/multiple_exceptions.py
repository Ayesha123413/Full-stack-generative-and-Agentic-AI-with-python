def process_order(item,quantity):
    try:
        price={"masala":20}[item] 
        # “Go to dictionary and get value using this key”
        cost=price * int(quantity)
        print(f"total cost is : {cost}")
    except KeyError:
        print("this type of tea is not available ")
    except ValueError:
        print("quantity should be in numbers")

process_order("ginger ",20)
process_order("masala","two")