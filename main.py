class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.get_mean_grade()}\nКурсы в процессе изучения: {self.get_all_courses()}\nЗавершенные курсы: {self.get_ended_courses()}'

    def __lt__(self, second):
        if isinstance(second, Student):
            if self.get_mean_grade() > second.get_mean_grade():
                return False
            else:
                return True
        
    def __gt__(self, second):
        if isinstance(second, Student):
            if self.get_mean_grade() < second.get_mean_grade():
                return False
            else:
                return True

    def get_all_courses(self):
        all_courses = None
        for items in self.courses_in_progress:
            if all_courses is None:
                all_courses = items
            else:
                all_courses = all_courses + ', ' + items
        return all_courses

    def get_ended_courses(self):
        ended_courses = None
        for items in self.finished_courses:
            if ended_courses is None:
                ended_courses = items
            else:
                ended_courses = ended_courses + ', ' + items
        return ended_courses       


    def get_mean_grade(self):
        all_gread = []
        for keys, values in self.grades.items():
            all_gread.extend(values)
        mean_gread = sum(all_gread) / len(all_gread)
        return mean_gread
            
    def rate_lection(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
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
        return f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_mean_grade()}'
    
    def __lt__(self, second):
        if isinstance(second, Lecturer):
            if self.get_mean_grade() > second.get_mean_grade():
                return False
            else:
                return True
        
    def __gt__(self, second):
        if isinstance(second, Lecturer):
            if self.get_mean_grade() < second.get_mean_grade():
                return False
            else:
                return True

    def get_mean_grade(self):
        all_gread = []
        for keys, values in self.grades.items():
            all_gread.extend(values)
        mean_gread = sum(all_gread) / len(all_gread)
        return mean_gread
        
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']

noob_student = Student('Мишустин', 'Люблюденюшки', 'your_gender')
noob_student.courses_in_progress += ['Html']

noob_student2 = Student('Медвед', 'Компоткин', 'your_gender')
noob_student2.courses_in_progress += ['Html']


# создаём двух лекторов
cool_lector = Lecturer('Дядя', 'Вася')
cool_lector.courses_attached += ['Python']

not_cool_lector = Lecturer('Путин', 'Люблюракеты')
not_cool_lector.courses_attached += ['Html']

# создаём ревьюеров
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

html_mentor = Reviewer('Any', 'Buddy')
html_mentor.courses_attached += ['Html']
 

# проставляем оценки лучшему студенту
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

# проставляем оценки худшему студенту
html_mentor.rate_hw(noob_student, 'Html', 2)
html_mentor.rate_hw(noob_student, 'Html', 2)
html_mentor.rate_hw(noob_student, 'Html', 3)

html_mentor.rate_hw(noob_student2, 'Html', 10)
html_mentor.rate_hw(noob_student2, 'Html', 10)
html_mentor.rate_hw(noob_student2, 'Html', 10)



# оцениваем студентами лекторов
best_student.rate_lection(cool_lector, 'Python', 10)
best_student.rate_lection(cool_lector, 'Python', 9)
 
noob_student.rate_lection(not_cool_lector, 'Html', 7)
noob_student.rate_lection(not_cool_lector, 'Html', 5)


# проверочка
# print(isinstance(cool_lector, Mentor))
# print(isinstance(cool_lector, Lecturer))
# print(isinstance(cool_mentor, Lecturer))


# проверочка перегрузки __str__ у студента
print(best_student)
print(noob_student)

# проверочка перегрузки __str__ у лектора
print(cool_lector)
print(not_cool_lector)


# проверочка перегрузки __str__ у ревьюера
print(cool_mentor)

# сравнение средних оцененок у студентов за домашние задания
print(best_student < noob_student)
print(best_student > noob_student)

# сравнение средних оцененок у лекторов за лекции
print(cool_lector < not_cool_lector)
print(cool_lector > not_cool_lector)



# 4 задание
# я или упустил или не было. А можно как-то выводить все объекты по классу? ну чтобы такой список был всегда актуальный?
# Иначе при создании нового студенты или лектора надо будет реализовать и создание его в общем списке.
all_students = [best_student, noob_student, noob_student2]
all_lectors = [cool_lector, not_cool_lector]

# делаем первую функцию с средней оценкой студентов по определённому предмету
def get_all_grades_course_students(students, course):
    all_grades = []
    for student in students:
        if course in student.courses_in_progress:
            all_grades.extend(student.grades[course])
    mean_grades = sum(all_grades) / len(all_grades)
    return mean_grades
        

mean_grade_html_student = get_all_grades_course_students(all_students, 'Html')
print(mean_grade_html_student)


# делаем вторую функцию с средней оценкой лекторов по определённому предмету
def get_all_grades_course_lectors(lectors, course):
    all_grades = []
    for lector in lectors:
        if course in lector.courses_attached:
            all_grades.extend(lector.grades[course])
    mean_grades = sum(all_grades) / len(all_grades)
    return mean_grades
        

mean_grade_html_lector = get_all_grades_course_lectors(all_lectors, 'Html')
print(mean_grade_html_lector)