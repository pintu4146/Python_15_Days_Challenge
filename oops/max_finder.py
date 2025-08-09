"""
Exercise 5: Create a class MaxFinder that identifies the largest number in a list.
"""

class MaxFinder:
    @staticmethod
    def find_max(number_list: list) -> int:
        return max(number_list)




print(MaxFinder.find_max([1,3,6,3,67,7,8]))