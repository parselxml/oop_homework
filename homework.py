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
                 f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                 f'Завершенные курсы: {", ".join(self.finished_courses)}\n')


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

super_lecture1 = Lecture('Анна', 'Петрова')
super_lecture1.courses_attached += ['Python']
super_lecture2 = Lecture('Максим', 'Иванов')
super_lecture2.courses_attached += ['Python']

best_student1 = Student('Светлана', 'Сидорова', 'your_gender')
best_student1.courses_in_progress += ['Python', 'Git']
best_student1.finished_courses += ['Введение в программирование']
best_student2 = Student('Алексей', 'Кузнецов', 'your_gender')
best_student2.courses_in_progress += ['Python', 'Discord']
best_student1.finished_courses += ['Введение в программирование']

best_student1.rate_lecture(super_lecture1, 'Python', 10)
best_student1.rate_lecture(super_lecture2, 'Python', 9)
best_student1.rate_lecture(super_lecture2, 'Python', 10)

cool_mentor1 = Reviewer('Ольга', 'Смирнова')
cool_mentor1.courses_attached += ['Python']
cool_mentor2 = Reviewer('Дмитрий', 'Федоров')
cool_mentor2.courses_attached += ['Python']

cool_mentor1.rate_hw(best_student1, 'Python', 10)
cool_mentor1.rate_hw(best_student2, 'Python', 10)
cool_mentor1.rate_hw(best_student2, 'Python', 8)

def avg_grades_hw(students: list, course: str):
    avg_grades = 0
    for student in students:
        if course in student.courses_in_progress:
            avg_grades += student.calculate_grades()
    return avg_grades / len(students)


def avg_grades_lecture(lectures: list, course: str):
    avg_grades = 0
    for lecture in lectures:
        if course in lecture.courses_attached:
            avg_grades += lecture.calculate_grades()
    return avg_grades / len(lectures)

print(best_student1)
print(best_student2)
print(super_lecture1)
print(super_lecture2)
print(cool_mentor1)
print(cool_mentor2)
print(super_lecture1 == super_lecture2)
print(best_student1 == best_student2)
print(avg_grades_hw([best_student1, best_student2], 'Python'))
print(avg_grades_lecture([super_lecture1, super_lecture2], 'Python'))