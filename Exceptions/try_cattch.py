order={"masala":11,"elechi":12}

try:
    print(order["spicy"])
except KeyError:
    print("The key that you are trying to access doesn't exist")