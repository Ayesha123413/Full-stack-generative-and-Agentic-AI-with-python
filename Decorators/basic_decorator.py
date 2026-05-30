from functools import wraps

def my_decor(func):
    # print("Inside the decorator function.", func)
    @wraps(func)
    def wrapper():
        print("Before the function call.")
        func()
        print("After the function call.")
    return wrapper


@my_decor
#whatever comes after @my_decor will be passed as an argument to my_decor function
def say_hello():
    print("Hello, World!")


say_hello()

# without usinf functools warsps function name will be wrapper instead of say_hello because wrapper is the function that is returned by my_decor function and it is the function that is called when we call say_hello function. So to preserve the original function name we can use functools wraps decorator. It will preserve the original function name and other attributes of the original function.
print(say_hello.__name__)
