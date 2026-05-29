def send_data_to_generator():
    print("Generator is ready to receive data.")

    while True:
        data = yield
        print(f"Received data: {data}")


generator = send_data_to_generator()
next(generator)  # Start the generator

# for better understanding just comment .send method line .Next function is only runs function and yeild expect some value to recieve
# if there is no value to receive then it will wait until it receive some value from .send method. So we have to use .send method to send some value to generator and then it will print that value.
#while while loop again runs after first iteration , then yeild again wait for value to receive that is why while loop is stops .
# send another value through send method and function run where it stops . Whole generator works like this.
generator.send("Hello, Generator!")

# generator.send("This is another message.")
