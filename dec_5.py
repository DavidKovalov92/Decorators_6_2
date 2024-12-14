from functools import wraps
import time


def max_per_minute(func):
    call_times = []

    @wraps(func)
    def wrapper(*args, **kwargs):
        current_time = time.time()
        call_times[:] = [t for t in call_times if current_time - t < 60]

        if len(call_times) >= 60:
            print("Limit is reached")
            return None

        call_times.append(current_time)
        return func(*args, **kwargs)

    return wrapper


@max_per_minute
def square(a):
    return a ** 200


for i in range(70):
    result = square(i)
    if result is not None:
        print(f"square({i}) = {result}")
    else:
        print(f"square({i})")
    time.sleep(0.5)