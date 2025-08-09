"""
Exercise 1: Create a class Greeter with a method greet(name) that prints a greeting for the provided name.
"""


class Greeter:
    """ Greeter class for printing the greetingd from the given name"""
    def __init__(self):
        pass

    def greet(self, name):
        """ greeter function
        :arg -> name
        :return -> None
        """
        print(f'Hello {name}')


greeter_obj = Greeter()
greeter_obj.greet('Pint')




