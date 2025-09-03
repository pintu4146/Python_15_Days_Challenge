"""


Exercise 11: Object Count Tracker:
 Design a class that tracks how many objects have been created from it
 and has a method to display this count.
"""


class InstanceCounter:
    count = 0

    def __init__(self):
        type(self).count += 1
    @staticmethod
    def display_count():
        print(f'Number of instance counted: {InstanceCounter.count}')
        return InstanceCounter.count

    def __repr__(self):
        return f'# of instance created= {self.count}'


obj_list = [InstanceCounter() for i in range(10)]
for obj in obj_list:
    print(f'instance created: {InstanceCounter.display_count()}')
