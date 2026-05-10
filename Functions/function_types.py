

# total = 0


# # pure function does not manipulate any global value
# def pure_function(x, y): 
#     return x + y


# #impure function manipulates global value , suppose to be avoided and not recommended to use in programming
# def impure_function(x):
#     global total
#     total += x
#     return total



def recursive_function(n):
    print(f"Recursion level: {n}")
    if n == 0:
        return "Recursion ends here."
    recursive_function(n - 1)

recursive_function(5)