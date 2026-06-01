from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied. Admins only.")
            return
        return func(user_role)
    return wrapper

@require_admin
def delete_user(user_role):
    print("User deleted successfully.")
delete_user("admin")  # This will work
delete_user("user")   # This will be denied access