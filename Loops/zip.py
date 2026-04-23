name=["Alice","Bob","Charlie","David","Eve"]
bills=[100,200,300,400]

for alias , amount in zip(name,bills):
    print(f"{alias} owes ${amount}.")