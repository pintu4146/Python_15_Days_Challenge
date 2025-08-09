class Calculator:
    # def __init__(self, a, b):
    #     self.a = a
    #     self.b = b

    def add(self, a: int, b: int, *args: int) -> int:
        if args:
            return a + b + sum(args)
        return a + b

    def sub(self, a: int, b: int) -> int:
        return a - b


c = Calculator()
res = c.add(1, 2, 34, 45, 6)
print(res)

