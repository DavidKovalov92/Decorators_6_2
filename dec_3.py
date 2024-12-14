def check_types(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for arg in args:
            print(f"Arg: {arg}, Type: {type(arg)}")
        if isinstance(result, int):
            return result
        else:
            return type(result)

    return wrapper


@check_types
def add(a: int, b: int) -> int:
    return a + b


print(add(1, 5))