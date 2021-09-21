class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f'Имя {self.name},\nФамилия {self.surname},\nСредняя оценка за дз : {self.get_mean_gread()},'

    def __lt__(self, second):
        if isinstance(second, Student):
            if self.get_mean_gread() > second.get_mean_gread():
                return False
            else:
                return True
        
    def __gt__(self, second):
        pass

    def get_mean_gread(self):
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
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

noob_student = Student('Мишустин', 'Лох', 'your_gender')
noob_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

cool_mentor.rate_hw(noob_student, 'Python', 2)
cool_mentor.rate_hw(noob_student, 'Python', 2)
cool_mentor.rate_hw(noob_student, 'Python', 5)

cool_lector = Lecturer('Дядя', 'Вася')
cool_lector.courses_attached += ['Python']

not_cool_lector = Lecturer('Путин', 'Вася')
not_cool_lector.courses_attached += ['Html']

print(cool_lector.name)
print(cool_lector.courses_attached)

best_student.rate_lection(cool_lector, 'Python', 10)
best_student.rate_lection(cool_lector, 'Python', 10)
 

print(best_student.grades)
print(cool_lector.grades)

# проверочка
print(isinstance(cool_lector, Mentor))
print(isinstance(cool_lector, Lecturer))
print(isinstance(cool_mentor, Lecturer))



print(best_student)


print(best_student < noob_student)

