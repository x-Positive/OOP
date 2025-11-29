# Класс для представления студентов
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # Выставляет оценку Лектору за лекции
    def rate_lecture(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if grade <= 10:
                if course in lector.grades:
                    lector.grades[course] += [grade]
                else:
                    lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Вывод студента
    def __str__(self):
        return f'Имя: {self.name}\n'\
               f'Фамилия: {self.surname}\n'\
               f'Средняя оценка за домашние задание: {self.aver_grades_stud()}\n'\
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'\
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    # Возвращает среднюю оценку за домашние задания
    def aver_grades_stud(self):
        all_grades = [grade for add_grades in self.grades.values() for grade in add_grades]
        return sum(all_grades) / len(all_grades)

    # Сравнение студентов по средней оценке
    def __lt__(self, other):
        return self.aver_grades_stud() < other.aver_grades_stud()

    # Сравнение студентов на равенство средней оценки
    def __eq__(self, other):
        return self.aver_grades_stud() == other.aver_grades_stud()

# Класс представления преподавателей
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

# Класс представления лекторов
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    # Вывод лекторов
    def __str__(self):
        return f'Имя: {self.name}\n'\
               f'Фамилия: {self.surname}\n'\
               f'Средняя оценка за лекции: {self.aver_grades_lect()}'

    # Возвращает среднюю оценку за лекции
    def aver_grades_lect(self):
        all_grades = [grade for add_grades in self.grades.values() for grade in add_grades]
        return sum(all_grades) / len(all_grades)

    # Сравнение лекторов по средней оценке
    def __lt__(self, other):
        return self.aver_grades_lect() < other.aver_grades_lect()

    # Сравнение лекторов на равенство средней оценки
    def __eq__(self, other):
        return self.aver_grades_lect() == other.aver_grades_lect()

# Класс проверяющих
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    # Выставляет оценку студенту за домашние задание
    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if grade <= 10:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Вывод проверяющего
    def __str__(self):
        return f'Имя: {self.name}\n'\
               f'Фамилия: {self.surname}'

# print(isinstance(lecturer, Mentor))
# print(isinstance(reviewer, Mentor))
# print(lecturer.courses_attached)
# print(reviewer.courses_attached)

# Студенты
student = Student('Алёхина', 'Ольга', 'Ж')
student.courses_in_progress += ['Python', 'Java', 'Git']

some_student = Student('Ruoy', 'Eman', 'М')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']

# Лекторы
lecturer = Lecturer('Иван', 'Иванов')
lecturer.courses_attached += ['Python', 'C++', 'Git']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python', 'Git']

# Проверяющие
reviewer = Reviewer('Петр', 'Петров')
reviewer.courses_attached += ['Python', 'C++', 'Git']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python', 'Git']

# print(student.rate_lecture(lecturer, 'Python', 7))
# print(student.rate_lecture(lecturer, 'Java', 8))
# print(student.rate_lecture(lecturer, 'С++', 8))
# print(student.rate_lecture(reviewer, 'Python', 6))

# print(lecturer.grades)

# Проверяющие выставляют оценки студентам
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

# Студенты оценивают лекторов
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

# Калькулятор средней оценки студентов по курсу
def calc_aver_student_grade(student_list, courses_name):
    total_grade = []
    for stud in student_list:
        if courses_name in stud.grades:
            total_grade.extend(stud.grades[courses_name])
        res = sum(total_grade) / len(total_grade)
    return f'Средняя оценка студентов по курсу: "{courses_name}" = {res}'

# Калькулятор средней оценки лекторов по курсу
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
print()
print(f"Студент {student.name} < {some_student.name}? {student < some_student}")
print(f"Лектор {lecturer.name} > {some_lecturer.name}? {lecturer > some_lecturer}")










