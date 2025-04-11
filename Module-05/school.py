class Student:
    def __init__(self,name,currentClass,id):
        self.name = name
        self.id = id
        self.currentClass = currentClass

    def __repr__(self) -> str:
        return f'student with name: {self.name} id : {self.id} class: {self.currentClass}'
    
class Teacher : 
    def __init__(self,name,id,subject) -> None:
        self.name = name
        self.id = id
        self.subject = subject

    def __repr__(self) ->str:
        return f'Teacher: {self.name} subject : {self.subject}'

class School :
    def __init__(self,name):
        self.name = name
        self.teachers = []
        self.students = []

    def addTeacher(self,name,subject):
        id = len(self.teachers)+100
        teacher = Teacher(name,id,subject)
        self.teachers.append(teacher)

    def enroll(self,name,fee):
        if fee < 6500:
            return 'not enough fee'
        else :
            id = len(self.students) + 1
            student = Student(name , 'C',id)
            self.students.append(student)
            return f'{name} is enroll with {id}, extra fee {fee - 6500}'
    def __repr__(self):
        print('welcome to ',self.name)
        print('-------------------------')
        print('Meet out teachers')
        for teacher in self.teachers :
            print(teacher)
        print('-------------------------')
        print('Meet our students')
        for student in self.students:
            print(student)
        print('-------------------------')
        return 'Thank you for enrolling '


# meherun = Student('Meherun',1,12)
# shahin = Student('Shahin',101,'OOP')
# print(meherun)
# print(shahin)

phitron = School('Phitron')
phitron.enroll('Shahin',8000)
phitron.enroll('Meherun',7000)
phitron.enroll('Meherab',6500)

phitron.addTeacher('Jankar sir','Python')
phitron.addTeacher('Pias vai','DS')
phitron.addTeacher('Atiqur vai','Algo')
phitron.addTeacher('Arif vai','Database')

print(phitron)