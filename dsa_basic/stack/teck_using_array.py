import unittest


class MyStack:
    def __init__(self):
        self.arr = []

    def push(self, data: int) -> list:
        """ push to push the data to the arr"""
        self.arr.append(data)
        return self.arr

    def pop(self):
        """

        :return: None
        """
        if len(self.arr) == 0:
            return -1
        self.arr.pop()

    def peek(self):
        if len(self.arr) == 0:
            return -1
        return self.arr[-1]

    def isEmpty(self):
        return True if len(self.arr) == 0 else False

    def size(self):
        return len(self.arr)


stack = MyStack()

stack.push(10)
print(stack.arr)
print(stack.size())
stack.pop()
print(stack.arr)


class MyStackTest(unittest.TestCase):

    def setUp(self):
        self.stack = MyStack()

    def test_push(self):
        self.stack.push(10)
        self.stack.push(1)
        self.assertEqual(self.stack.arr, [10, 1])

    def test_pop(self):
        self.stack.push(10)
        self.stack.push(1)
        self.stack.pop()
        self.assertEqual(self.stack.arr, [10])

    def test_peek(self):
        self.stack.push(10)
        top_ele = self.stack.peek()
        self.assertEqual(top_ele, 10)

    def test_is_empty(self):
        self.assertTrue(self.stack.isEmpty())
        self.stack.push(10)
        self.assertTrue(self.stack, False)
