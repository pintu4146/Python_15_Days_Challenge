

class Student:
    def __init__(self, name:str, marks:list) -> None:
        self.name = name
        self.marks = marks
        self.avg_marks = 0


    def average_marks(self) -> int:
        self.avg_marks = sum(self.marks)// len(self.marks)
        return self.avg_marks

    def get_grade(self) -> dict:

        if 100 > self.avg_marks >= 90:
            return {'Grade': 'A'}
        elif 90 > self.avg_marks >= 80:
            return {'Grade': 'B'}
        elif 80 > self.avg_marks >= 70:
            return {'Grade': 'C'}

    def __repr__(self):
        return f'name: {self.name} marks: {self.marks} avg_marks: {self.avg_marks}'




student = Student('Pintu', [10,80,90,40,50,60])
student.average_marks()

print(student)
