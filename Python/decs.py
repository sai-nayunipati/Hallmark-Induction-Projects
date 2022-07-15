# An example of a decorator.
def print_lines(function):
    def inner_function(name):
        print("-"*30)
        function(name)
        print("-"*30)

    return inner_function


@print_lines
def print_hello(name):
    print("Hello " + name + ".")


print_hello("John")


class Person:
    def __call__(self, name):
        print("Hello " + name + ".")
