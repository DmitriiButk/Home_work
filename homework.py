class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def lect_rate(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
            and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def average_grades(self):
        grades = sum(self.grades.values(), [])
        if grades:
            return sum(grades) / len(grades)
        return

    def courses_in_progress(self):
        return self.courses_in_progress()

    def finished_courses(self):
        return self.finished_courses()

    def __str__(self):
        return f"Имя студента: {self.name}\nФамилия студента: {self.surname}\n" \
               f"Средняя оценка за домашнее задание: {self.average_grades()}\n" \
               f"Курсы в процессе изучения: {self.courses_in_progress}\n" \
               f"Завершённые курсы: {self.finished_courses}"

    def __lt__(self, other):
        return self.average_grades() < other.average_grades()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grades(self):
        if not self.grades:
            return f"Нет оценок"
        else:
            grades = sum(self.grades.values(), [])
            return sum(grades) / len(grades)

    def __str__(self):
        return f"Имя лектора: {self.name}\nФамилия лектора: {self.surname}\n" \
               f"Средняя оценка за лекции: {self.average_grades()}"

    def __lt__(self, other):
        return self.average_grades() < other.average_grades()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        return f"Имя ревьювера: {self.name}\nФамилия ревьювера: {self.surname}"


def aver_gr_st(students, course):
    grades = []
    for student in students:
        if course in student.courses_in_progress:
            if course in student.grades:
                grades.extend(student.grades[course])
    if grades:
        return sum(grades) / len(grades)
    return 0

def aver_gr_lec(lecturers, course):
    grades = []
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            if course in lecturer.grades:
                grades.extend(lecturer.grades[course])
    if grades:
        return sum(grades) / len(grades)
    return 0


student_one = Student("Дмитрий", "Бутков","M")
student_one.courses_in_progress += ["Python", "Java", "SQL"]
student_two = Student("Никита", "Кучеров", "M")
student_two.courses_in_progress += ["Data Scientist", "Product Manager", "UX/UI - дизайнер"]

lecturer_one = Lecturer("Сергей", "Бобровский")
lecturer_one.courses_attached += ["Python", "Data Scientist", "Java"]
lecturer_two = Lecturer("Артемий", "Панарин")
lecturer_two.courses_attached += ["SQL", "Product Manager", "UX/UI - дизайнер"]

reviewer_one = Reviewer("Андрей", "Василевский")
reviewer_one.courses_attached += ["Python", "SQL", "Product Manager"]
reviewer_two = Reviewer("Александр", "Овечкин")
reviewer_two.courses_attached += ["Data Scientist", "UX/UI - дизайнер", "Java"]

student_one.lect_rate(lecturer_one, "Python", 8)
student_one.lect_rate(lecturer_one, "Data Scientist", 9)
student_one.lect_rate(lecturer_two, "SQL" , 7)
student_one.lect_rate(lecturer_two, "UX/UI - дизайнер", 8)
student_two.lect_rate(lecturer_one, "Java", 9)
student_two.lect_rate(lecturer_one, "Python", 7)
student_two.lect_rate(lecturer_two, "Product Manager", 9)
student_two.lect_rate(lecturer_two, "SQL", 10)

reviewer_one.rate_hw(student_one, "Python", 9)
reviewer_one.rate_hw(student_two, "Data Scientist", 8)
reviewer_two.rate_hw(student_one, "SQL", 7)
reviewer_two.rate_hw(student_two, "UX/UI - дизайнер", 8)

student_one.add_courses("Data Scientist")
student_two.add_courses("Python")

print(student_one)
print(student_two)
print(lecturer_one)
print(lecturer_two)
print(reviewer_one)
print(reviewer_two)

print(student_one > student_two)
print(lecturer_one < lecturer_two)

students = [student_one, student_two]
lecturers = [lecturer_one, lecturer_two]

print(aver_gr_st(students, "Python"))
print(aver_gr_lec(lecturers, "SQL"))























