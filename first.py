"""
First implementation of the interceptor pattern using Python
"""

def interceptor(func):
    """
    This is a decorator used to intercept other function calls
    """
    print("Executed During function definition")

    def wrapper(*args, **kwargs):
        print("Just before function execution")
        result = func(*args, **kwargs)
        print("Just after function execution")
        return result
    
    return wrapper


@interceptor
def some_function(arg: str):
    print("Some test function")
    print(f"The argument: {arg}")


if __name__ == "__main__":
    some_function("hello")