size = input("Enter the size of your chai (small/medium/large) :").lower()

if size=="small":
    print("The price of small chai is 10 Rs.")
elif size=="medium":
    print("The price of medium chai is 20 Rs.")
elif size=="large":
    print("The price of large chai is 30 Rs.")
else:
    print("Sorry! We don't have that size of chai.")