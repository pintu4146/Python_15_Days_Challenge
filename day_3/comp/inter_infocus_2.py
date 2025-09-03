"""

Implement a compose function that allows mathematical function composition: .
Usage: compose(str, lambda x: x*2, lambda x: x+1)(5) -> "12"

"""


def compose(*arg):
    def inner(input):
        res = None
        for func in reversed(arg):
            if res:
                res = func(res)
            else:
                res = func(input)

        return res

    return inner


f = lambda x: x * 2
g = lambda x: x + 1
i = lambda x: x + 1

h = compose(str, f, g, i)(5)
print(h)


# with open(f'test')

# def addition(x: int, y: int) -> int:
#     return x + y
#
#
# addition("ab", "cd")
