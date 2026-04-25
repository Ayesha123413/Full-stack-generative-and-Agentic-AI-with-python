value=13

# reminder=value%5

# if reminder>0:
#     print(f" Reminder is:  {reminder}")

if (reminder:=value%5) > 0:
    print(f" Reminder is:  {reminder}")

available_size=["small","medium","large"]

if (demanded_size:=input("Enter the size you want: ")).lower() in available_size:
    print(f"{demanded_size} is available.")
else:
    print(f"{demanded_size} is not available.")