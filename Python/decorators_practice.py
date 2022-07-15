def f1(func):
    def wrapper(*args, **kwargs):
        print("Started")
        val = func(*args, **kwargs)
        print("Ended")
        return val
    return wrapper


def f(a, b=9):
    print(a, b)


f1(f)(1, 2)
