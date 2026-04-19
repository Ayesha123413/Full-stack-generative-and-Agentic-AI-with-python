seat_type=input("Enter the seat type (Sleeper, AC, General, Luxury ): ").lower()

match seat_type:
    case "sleeper":
        print("The price of Sleeper seat is 500 Rs.")
    case "ac":
        print("The price of AC seat is 1000 Rs.")
    case "general":
        print("The price of General seat is 300 Rs.")
    case "luxury":
        print("The price of Luxury seat is 2000 Rs.")
    case _:
        print("Sorry! We don't have that type of seat.")