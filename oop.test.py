class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if grade <= 10:
                if course in lector.grades:
                    lector.grades[course] += [grade]
                else:
                    lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\n'\
               f'Фамилия: {self.surname}\n'\
               f'Средняя оценка за домашние задание: {self.aver_grades()}\n'\
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'\
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def aver_grades(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    grades = {}

    def __str__(self):
        return f'Имя: {self.name}\n'\
               f'Фамилия: {self.surname}\n'\
               f'Средняя оценка за лекции: {self.aver_grades()}'

    def aver_grades(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades)


class Reviewer(Mentor):
    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if grade <= 10:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\n'\
               f'Фамилия: {self.surname}'

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Петр', 'Петров')

# print(isinstance(lecturer, Mentor))
# print(isinstance(reviewer, Mentor))
# print(lecturer.courses_attached)
# print(reviewer.courses_attached)

student = Student('Алёхина', 'Ольга', 'Ж')
student.courses_in_progress += ['Python', 'Java']

lecturer.courses_attached += ['Python', 'C++']

reviewer.courses_attached += ['Python', 'C++']

# print(student.rate_lecture(lecturer, 'Python', 7))
# print(student.rate_lecture(lecturer, 'Java', 8))
# print(student.rate_lecture(lecturer, 'С++', 8))
# print(student.rate_lecture(reviewer, 'Python', 6))

# print(lecturer.grades)

some_student = Student('Ruoy', 'Eman', 'М')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python', 'Git']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python', 'Git']

some_reviewer.rate_student(some_student, 'Python', 9)
some_reviewer.rate_student(some_student, 'Python', 10)
some_reviewer.rate_student(some_student, 'Python', 10)
some_reviewer.rate_student(some_student, 'Git', 10)
some_reviewer.rate_student(some_student, 'Git', 10)
some_reviewer.rate_student(some_student, 'Git', 10)
some_reviewer.rate_student(some_student, 'Git', 10)
some_reviewer.rate_student(some_student, 'Git', 10)
some_reviewer.rate_student(some_student, 'Git', 10)
some_reviewer.rate_student(some_student, 'Git', 10)

some_student.rate_lecture(some_lecturer, 'Python', 9)
some_student.rate_lecture(some_lecturer, 'Python', 10)
some_student.rate_lecture(some_lecturer, 'Python', 10)
some_student.rate_lecture(some_lecturer, 'Python', 10)
some_student.rate_lecture(some_lecturer, 'Python', 10)
some_student.rate_lecture(some_lecturer, 'Python', 10)
some_student.rate_lecture(some_lecturer, 'Python', 10)
some_student.rate_lecture(some_lecturer, 'Git', 10)
some_student.rate_lecture(some_lecturer, 'Git', 10)
some_student.rate_lecture(some_lecturer, 'Git', 10)

print(some_reviewer)
print()
print(some_lecturer)
print()
print(some_student)






