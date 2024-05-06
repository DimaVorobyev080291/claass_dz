class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grads = 0 
        

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
            
    def _average(self):
        total_subject_grades = 0
        count_subject_grades = 0
        for subject, value in self.grades.items():
            total_subject_grades += sum(value)
            count_subject_grades += len(value)
        result = round(total_subject_grades / count_subject_grades , 1)
        self.average_grads = result
        return result
        
    def _average_st_course(self, course):
        total_subject_grades = 0
        count_subject_grades = 0
        for keys in self.grades.keys():
            if keys == course:
                total_subject_grades += sum(self.grades[course])
                count_subject_grades += len(self.grades[course])
        return round(total_subject_grades / count_subject_grades, 1)
            
    def __str__(self):
        result = f'Имя: {self.name}\n'\
                 f'Фамилия: {self.surname}\n'\
                 f'Средняя оценка за домашние задания: {self._average()}\n'\
                 f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'\
                 f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return result
        
        
    def __lt__(self, student):
        if isinstance(student, Student):
            result = self._average() < student._average()
        else:
            print('Ошибка')
            return
        return result
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average(self):
       total_subject_grades = 0
       count_subject_grades = 0
       for subject, value in self.grades.items():
           total_subject_grades += sum(value)
           count_subject_grades += len(value)
       return  round(total_subject_grades / count_subject_grades , 1)
       
    def _average_lt_course(self, course):
        total_subject_grades = 0
        count_subject_grades = 0
        for keys in self.grades.keys():
            if keys == course:
                total_subject_grades += sum(self.grades[course])
                count_subject_grades += len(self.grades[course])
        return round(total_subject_grades / count_subject_grades, 1)
    
    def __str__(self):
      result = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n'\
              f'Средняя оценка за лекции:{self._average()}\n'
      return result
      
    def __lt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            result = self._average() < lecturer._average()
        else:
            print('Ошибка')
            return
        return result

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n') 
        
lecturer_1 = Lecturer('Степан', 'Степанов')
lecturer_1.courses_attached += ['Python', 'Exel','C+']
lecturer_2 = Lecturer('Светлана', 'Светланова')
lecturer_2.courses_attached += ['JavaScript', 'Python','C+']

student_1 = Student('Иван', 'Иванов', 'male')
student_1.courses_in_progress += ['Python', 'C+','Exel']
student_1.finished_courses += ['JavaScript']
student_1.rate_lec(lecturer_1, 'Python', 5)
student_1.rate_lec(lecturer_2, 'Python', 8)
student_1.rate_lec(lecturer_1, 'C+', 5)
student_1.rate_lec(lecturer_2, 'C+', 7)

student_2 = Student('Ирина', 'Иринова', 'female')
student_2.courses_in_progress += ['Python', 'Exel','C+']
student_2.finished_courses += ['JavaScript']
student_2.rate_lec(lecturer_1, 'Python', 8)
student_2.rate_lec(lecturer_2, 'Python', 6)
student_2.rate_lec(lecturer_1, 'C+', 3)
student_2.rate_lec(lecturer_2, 'C+', 2)

reviewer_1 = Reviewer('Тимур', 'Тимуров')
reviewer_1.courses_attached += ['Python', 'Exel','C+']
reviewer_1.rate_student(student_1, 'Python', 2)
reviewer_1.rate_student(student_2, 'Python', 4)
reviewer_1.rate_student(student_1, 'C+', 1)
reviewer_1.rate_student(student_2, 'C+', 2)


reviewer_2 = Reviewer('Татьяна', 'Татьянова')
reviewer_2.courses_attached += ['JavaScript', 'Python', 'C+']
reviewer_2.rate_student(student_1, 'Python', 3)
reviewer_2.rate_student(student_2, 'Python', 5)
reviewer_2.rate_student(student_1, 'C+',5)
reviewer_2.rate_student(student_2, 'C+',6)

print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)

print('Сравнение студентов:')
print('student_1 < student_2:', student_1 < student_2)
print('Сравнение лекторов:')
print('lecturer_1 < lecturer_2:', lecturer_1 < lecturer_2)
print 
student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]


def grade_all_st(student_list, course):
    summ_all = 0
    len_all = 0
    for students in student_list:
        summ = students._average_st_course(course)
        summ_all += summ
        len_all += 1
    result = round(summ_all / len_all, 1)
    return result
    
def grade_all_lt(lecturer_list, course):
    summ_all = 0
    len_all = 0
    for lecturers in lecturer_list:
        summ = lecturers._average_lt_course(course)
        summ_all += summ
        len_all += 1
    result = round(summ_all / len_all, 1)
    return result

print(f'Cредняя оценка за домашние задания:')
print(grade_all_st(student_list, 'C+'))

print(f'Средняя оценка за лекции:')
print(grade_all_lt(lecturer_list, 'Python'))