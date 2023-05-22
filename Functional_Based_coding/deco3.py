def repeat(num_repeats):
    def decorator_func(original_func):
        def wrapper_func(*args, **kwargs):
            for i in range(num_repeats):
                result = original_func(*args, **kwargs)
            return result
        return wrapper_func
    return decorator_func


@repeat(num_repeats=3)
def greet(name):
    print(f"Hello, {name}!")


greet("rahul Gupta")