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
               f'Средняя оценка за домашние задание: {self.aver_grades_stud()}\n'\
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'\
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def aver_grades_stud(self):
        all_grades = [grade for add_grades in self.grades.values() for grade in add_grades]
        return sum(all_grades) / len(all_grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\n'\
               f'Фамилия: {self.surname}\n'\
               f'Средняя оценка за лекции: {self.aver_grades_lect()}'

    def aver_grades_lect(self):
        all_grades = [grade for add_grades in self.grades.values() for grade in add_grades]
        return sum(all_grades) / len(all_grades)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

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

# print(isinstance(lecturer, Mentor))
# print(isinstance(reviewer, Mentor))
# print(lecturer.courses_attached)
# print(reviewer.courses_attached)

student = Student('Алёхина', 'Ольга', 'Ж')
student.courses_in_progress += ['Python', 'Java', 'Git']

some_student = Student('Ruoy', 'Eman', 'М')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']

lecturer = Lecturer('Иван', 'Иванов')
lecturer.courses_attached += ['Python', 'C++', 'Git']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python', 'Git']

reviewer = Reviewer('Петр', 'Петров')
reviewer.courses_attached += ['Python', 'C++', 'Git']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python', 'Git']

# print(student.rate_lecture(lecturer, 'Python', 7))
# print(student.rate_lecture(lecturer, 'Java', 8))
# print(student.rate_lecture(lecturer, 'С++', 8))
# print(student.rate_lecture(reviewer, 'Python', 6))

# print(lecturer.grades)

reviewer.rate_student(student, 'Python', 8)
reviewer.rate_student(student, 'Python', 7)
reviewer.rate_student(student, 'Git', 8)

reviewer.rate_student(some_student, 'Python', 9)
reviewer.rate_student(some_student, 'Python', 10)
reviewer.rate_student(some_student, 'Python', 10)
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
student.rate_lecture(lecturer, 'Python', 10)
student.rate_lecture(lecturer, 'Git', 8)
student.rate_lecture(lecturer, 'Git', 9)

print(some_reviewer)
print()
print(some_lecturer)
print()
print(some_student)
print()

add_student = [student, some_student]
add_lecture = [lecturer, some_lecturer]

def calc_aver_student_grade(student_list, courses_name):
    total_grade = []
    for stud in student_list:
        if courses_name in stud.grades:
            total_grade.extend(stud.grades[courses_name])
        res = sum(total_grade) / len(total_grade)
    return f'Средняя оценка студентов по курсу: "{courses_name}" = {res}'

def calc_aver_lecturer_grade(lecture_list, courses_name):
    total_grade = []
    for lect in lecture_list:
        if courses_name in lect.grades:
            total_grade.extend(lect.grades[courses_name])
        res = sum(total_grade) / len(total_grade)
    return f'Средняя оценка лекторов по курсу: "{courses_name}" = {res}'

print(calc_aver_student_grade(add_student, 'Python'))
print(calc_aver_lecturer_grade(add_lecture, 'Python'))
print(calc_aver_student_grade(add_student, 'Git'))
print(calc_aver_lecturer_grade(add_lecture, 'Git'))








