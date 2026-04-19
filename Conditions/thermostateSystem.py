device_status=input("device_status : ").lower()

if device_status=="active":
    temperature=int(input(" Enter temperature : "))
    if(temperature>35):
        print("Warning High temperature! Turn on the AC")
    else:
        print("Temperature is normal")

else:
    print("Thermostat is off")