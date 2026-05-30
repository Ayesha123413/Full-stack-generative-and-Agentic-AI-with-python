def my_decor(func):
    # print("Inside the decorator function.", func)
    def wrapper():
        print("Before the function call.")
        func()
        print("After the function call.")
    return wrapper


# @my_decor
#whatever comes after @my_decor will be passed as an argument to my_decor function
def say_hello():
    print("Hello, World!")


say_hello()
