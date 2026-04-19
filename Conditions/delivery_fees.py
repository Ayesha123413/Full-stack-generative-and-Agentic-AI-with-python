order_amount= int(input("Enter the order amount: "))


delivery_fees= 0 if order_amount > 3000 else 300
print(f"Delivery fees: {delivery_fees} Rs.")

