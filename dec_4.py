def cash_func(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = args + tuple(kwargs.items())
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper


@cash_func
def square(a):
    return a ** 200


print(square(3))