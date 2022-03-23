#Function to calculate average grade
def average_in_dict(dict):
    sum_num = 0
    qty = 0
    for course in dict:
        sum_num += sum(dict[course])
        qty += len(dict[course])
    if qty > 0:
        return (sum_num/qty)

#function to calculate average grade for multiple lecturers or students for a specific course
def course_rate_average(stud_or_teach, course):
    sum_num = 0
    qty = 0
    for person in stud_or_teach:
        sum_num += sum(person.grades[course])
        qty += len(person.grades[course])
    if qty > 0:
        return (sum_num/qty)


#Class for students
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

#Mentor class
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

#Lecturer class - child of Mentor
class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_in_dict(self.grades)}'

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return (average_in_dict(self.grades)) < (average_in_dict(other.grades))

#Reviewer class - child of Mentor
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'



#Creating 2 examples of each class
student1 = Student('Andrew', 'Garfield', 'male')
student2 = Student('Jenifer', 'Lawrence', 'female')

#Adding data to created students
student1.courses_in_progress = ['Python']
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
lecturer1.courses_attached = ['Python']
lecturer1.courses_attached += ['Operating Systems']

lecturer2.courses_attached = ['Python']
lecturer2.courses_attached += ['Business Management']

reviewer1.courses_attached = ['Python']
reviewer2.courses_attached = ['Python']

#Grading students - using rate_hw method
reviewer1.rate_hw(student1,'Python',7)
reviewer1.rate_hw(student1,'Python',10)

reviewer2.rate_hw(student1,'Python',8)
reviewer2.rate_hw(student1,'Python',5)

reviewer1.rate_hw(student2,'Python',10)
reviewer1.rate_hw(student2,'Python',10)

reviewer2.rate_hw(student2,'Python',10)
reviewer2.rate_hw(student2,'Python',9)

#Grading lecturers - using rate teach method
student1.rate_teach(lecturer1, 'Python', 10)
student1.rate_teach(lecturer1, 'Python', 7)

student2.rate_teach(lecturer1, 'Python', 8)
student2.rate_teach(lecturer1, 'Python', 1)

student1.rate_teach(lecturer2,'Python',9)
student1.rate_teach(lecturer2,'Python',3)

student2.rate_teach(lecturer2,'Python',5)
student2.rate_teach(lecturer2,'Python',7)

#Printing out _str_ methods
print('-'*20)
print('Лекторы:')
print('-'*20)
print(lecturer1)
print()
print(lecturer2)
print()
print('-'*20)
print('Эксперты:')
print('-'*20)
print(reviewer1)
print()
print(reviewer2)
print()
print('-'*20)
print('Студенты:')
print('-'*20)
print(student1)
print()
print(student2)
print()
print('-'*20)

#Printing out __lt__ methods
print(f'Средняя оценка лектора {lecturer1.name} меньше чем у лектора {lecturer2.name}: {lecturer1 < lecturer2}')
print(f'Средняя оценка студента {student1.name} меньше чем у студента {student2.name}: {student1 < student2}')

#printing out overall average for grades of students or lecturers for a specific course
print()
print('-'*20)
print(f'Средняя оценка лекторов {lecturer1.name} и {lecturer2.name} по курсу "Python": {course_rate_average([lecturer1, lecturer2],"Python"):0.2f}')
print(f'Средняя оценка студентов {student1.name} и {student2.name} по курсу "Python": {course_rate_average([student1, student2],"Python"):0.2f}')
