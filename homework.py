class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecture, course, grade):
        if isinstance(lecture, Lecture) and course in self.courses_in_progress and course in lecture.courses_attached:
             if course in lecture.grades and 10 >= grade:
                lecture.grades[course] += [grade]
             else:
                lecture.grades[course] = [grade]
        else:
             return 'Ошибка'

    def __str__(self):
        return  (f'Имя: {self.name}\n'
                 f'Фамилия: {self.surname}\n'
                 f'Средняя оценка за домашние задания: {self.calculate_grades()}\n'
                 f'Курсы в процессе изучения: {". ".join(self.courses_in_progress)}\n'
                 f'Завершенные курсы: {". ".join(self.finished_courses)}\n')


    def calculate_grades(self):
        grades = sum(sum(grades) for grades in self.grades.values())
        count_ = sum(len(grades) for grades in self.grades.values())
        return round(grades / count_, 2)

    def __eq__(self, other):
        return self.calculate_grades() == other.calculate_grades()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecture(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.calculate_grades()}\n')

    def calculate_grades(self):
        grades = sum(sum(grades) for grades in self.grades.values())
        count_ = sum(len(grades) for grades in self.grades.values())
        return round(grades / count_, 2)

    def __eq__(self, other):
        return self.calculate_grades() == other.calculate_grades()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n')