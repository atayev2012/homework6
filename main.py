class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):

        sum_num = 0
        qty = 0

        for course in self.grades:
            sum_num += sum(self.grades[course])
            qty += len(self.grades[course])

        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {sum_num/qty}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def rate_teach(self, teacher, course, grade):
        if isinstance(teacher, Lecturer) and course in self.courses_in_progress and course in teacher.courses_attached:
            if course in teacher.grades:
                teacher.grades[course] += [grade]
            else:
                teacher.grades[course] = [grade]
        else:
            return 'Ошибка'

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

        sum_num = 0
        qty = 0
        for course in self.grades:
            sum_num += sum(self.grades[course])
            qty += len(self.grades[course])

        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {sum_num/qty}'


class Reviewer(Mentor):
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
#
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
#
cool_lect = Lecturer('Boby','Dylan')
cool_lect.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

best_student.rate_teach(cool_lect,'Python',8)
best_student.rate_teach(cool_lect,'Python',10)

print(best_student)
print(cool_mentor)
print(cool_lect)

# print(best_student.grades)