"""
Exercise 12: Calculating Student Results:
Develop a class to accept a student's name and marks in three subjects,
then calculate and display the total and average marks

"""


class StudentAverageMarks:
    def __init__(self, s_name: str, sub_1: int, sub_2: int, sub_3: int) -> None:
        self.s_name = s_name
        self.sub_1 = sub_1
        self.sub_2 = sub_2
        self.sub_3 = sub_3

    @property
    def avarage_marks(self):
        avg_marks = (self.sub_1 + self.sub_2 + self.sub_3) / 3
        print(f'avg marks of {self.s_name}: {avg_marks}')
        return avg_marks

    def display_name_avg(self):
        print(f'avg marks of {self.s_name}: {self.avarage_marks}')


student_one = StudentAverageMarks('Pintu', 10, 20, 30)
student_one.display_name_avg()
