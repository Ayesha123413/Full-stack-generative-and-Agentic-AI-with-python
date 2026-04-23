
menu=["spice","green","masala","simple"]

print(list(enumerate(menu,start=1)))

for index,item in enumerate(menu,start=1):
    print(f"{index}: {item}")
    