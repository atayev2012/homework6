#Function to calculate average grade
def average_in_dict(dict):
    sum_num = 0
    qty = 0
    for course in dict:
        sum_num += sum(dict[course])
        qty += len(dict[course])
    if qty > 0:
        return float((sum_num/qty))


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_in_dict(self.grades):0.1f}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def rate_teach(self, teacher, course, grade):
        if isinstance(teacher, Lecturer) and course in self.courses_in_progress and course in teacher.courses_attached:
            if course in teacher.grades:
                teacher.grades[course] += [grade]
            else:
                teacher.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if isinstance(other, Student):
            return (average_in_dict(self.grades)) < (average_in_dict(other.grades))


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def rate_hw(self, student, course, grade):
        print('Лекторы не могут выставлять оценки студентам')

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {average_in_dict(self.grades)}'''

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return (average_in_dict(self.grades)) < (average_in_dict(other.grades))


class Reviewer(Mentor):
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'



#Creating 2 examples of each class
student1 = Student('Andrew', 'Garfield', 'male')
student2 = Student('Jenifer', 'Lawrence', 'female')

#Adding data to created students
student1.courses_in_progress = ['Pyhton']
student1.courses_in_progress += ['Javascript']

student2.courses_in_progress = ['Python']
student2.courses_in_progress += ['Django']

student1.finished_courses = ['Web design']
student1.finished_courses += ['Introduction to Frontend Development']

student2.finished_courses = ['PHP']
student2.finished_courses += ['SQL Databases']

#Creating 2 examples of Lecturers and Reviewers
lecturer1 = Lecturer('Bill', 'Gates')
lecturer2 = Lecturer('Steve', 'Jobs')

reviewer1 = Reviewer('Alexandr', 'Bardin')
reviewer2 = Reviewer('Yelena', 'Nikitina')

#Adding data to created mentors
lecturer1.courses_attached = ['Pyhton']
lecturer1.courses_attached += ['Operating Systems']

lecturer2.courses_attached = ['Python']
lecturer2.courses_attached += ['Business Management']

#Grading students
reviewer1.rate_hw(student1,'Python',7)
reviewer1.rate_hw(student1,'Python',10)

reviewer2.rate_hw(student1,'Python',8)
reviewer2.rate_hw(student1,'Python',5)

reviewer1.rate_hw(student2,'Python',10)
reviewer1.rate_hw(student2,'Python',10)

reviewer2.rate_hw(student2,'Python',10)
reviewer2.rate_hw(student2,'Python',9)

print(student1.grades)
print(student2.grades)
#Grading lecturers
student1.rate_teach(lecturer1, 'Python', 10)
student1.rate_teach(lecturer1, 'Python', 7)

student2.rate_teach(lecturer1, 'Python', 8)
student2.rate_teach(lecturer1, 'Python', 1)

student1.rate_teach(lecturer2,'Python',9)
student1.rate_teach(lecturer2,'Python',3)

student2.rate_teach(lecturer2,'Python',5)
student2.rate_teach(lecturer2,'Python',7)

#Printing results of all methods

print('-'*20)
print(lecturer1)
print(lecturer1.grades)


