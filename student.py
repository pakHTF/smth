class Student:
    def __init__(self, name, group):
        self.name=name
        self.group=group
        self.grades=[]
    def add_grade(self, grade):
        if 2<=grade<=5:
            self.grades.append(grade)
    def average_grade(self):
        if not self.grades:
            return 0.0
        return sum(self.grades)/len(self.grades)
    def info(self):
        return f"{self.name}, группа {self.group}, средний балл: {self.average_grade()}"
# primer
s = Student("Mark", "ФИПМ_67")
s.add_grade(3)
s.add_grade(4)
s.add_grade(3)
s.add_grade(2)
s.add_grade(1)
print(s.average_grade())   # 3.0
print(s.info())            # "Анна, группа ФИПМ_21, средний балл: 3.0"
