
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.courses_attached = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _aver_rating(self):
        _sum = 0
        counter = 0
        for value in self.grades.values():
            for i in value:
                _sum += i
                counter += 1

            return round(_sum / counter, 2)
        
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._aver_rating()}\nКурсы в процессе: {", ".join(self.courses_in_progress)}\nЗавершённые курсы: {"".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не является экземпляром класса Student.')
            return
        return self._aver_rating() < other._aver_rating()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []       

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.courses_in_progress = []
        self.grades = {}

    def _aver_rating(self):
        _sum = 0
        counter = 0
        for value in self.grades.values():
            for i in value:
                _sum += i
                counter += 1
            
            return round(_sum / counter, 2)        

    def __str__(self): 
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._aver_rating()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не является экземпляпом класса Lecturer.')
            return
        return self._aver_rating() < other._aver_rating()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)


some_student = Student('Mara', 'Kolet', 'female')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']

some_reviewer = Reviewer('Peter', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']
 
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9)


best_lecturer = Lecturer('Tom', 'Raimy')
best_lecturer.courses_in_progress += ['Python']

some_student.courses_attached += ['Python']

some_student.rate_hw(best_lecturer, 'Python', 9)
some_student.rate_hw(best_lecturer, 'Python', 10)
some_student.rate_hw(best_lecturer, 'Python', 9)
some_student.rate_hw(best_lecturer, 'Python', 9)


some_lecturer = Lecturer('Sam', 'Raimy')
some_lecturer.courses_in_progress += ['Python']

some_student.rate_hw(some_lecturer, 'Python', 9)
some_student.rate_hw(some_lecturer, 'Python', 8)
some_student.rate_hw(some_lecturer, 'Python', 9)
some_student.rate_hw(some_lecturer, 'Python', 9)


print(best_lecturer)
print(some_lecturer)
print(best_student)
print(some_student)
print(some_reviewer)


print(best_lecturer.__lt__(some_lecturer))
print(best_student.__lt__(some_student))


student_list = [best_student, some_student]
lecturer_list = [best_lecturer, some_lecturer]

def average_rat_stud(students, course):
    '''Функция для подсчёта средней оценки за домашнее задание по всем студентам в рамках курса'''
    _sum = []
    for student in student_list:
        if isinstance(student, Student) and course in student.grades:
            _sum.extend(student.grades[course])
        else:
            print('Error.')
            return
    return f'Средняя оценка студентов по {course}: {round(sum(_sum) / len(_sum), 2)}'

print(average_rat_stud(student_list, 'Python'))

def average_rat_lect(lecturers, course):
    '''Функция для подсчёта средней оценки за лекции по всем лекторам в рамках курса.'''
    _sum = []
    for lecturer in lecturer_list:
        if isinstance(lecturer, Lecturer) and course in lecturer.grades:
            _sum.extend(lecturer.grades[course])
        else:
            print('Error.')
            return
    return f'Средняя оценка лекторов по Python: {round(sum(_sum) / len(_sum), 2)}'

print(average_rat_lect(lecturer_list, 'Python'))