staff=[('Alice', 16), ('Bob', 20), ('Charlie', 22), ('David', 24), ('Eve', 26)]

for name , age in staff:
    if age <= 11:
        print(f"{name} is eligible for staff.")
        break
else:
    print("No staff member is eligible.")