class School:
    def __init__(self , name , address) -> None:
        self.name = name
        self.address = address
        self.teachers = {}
        #composition
        self.classrooms = {}
    
    def add_classrooms(self,classroom):
        self.classrooms[classroom.name] = classroom
    
    def add_teacher(self,subject,teacher):
        self.teachers[subject] = teacher    
        
    def student_addmission(self,student):
        className = student.classroom.name
        if className in self.classrooms:
            self.classrooms[className].add_student(student)
        else:
            print(f'No classname as named {className}')
            
    def __repr__(self) ->str:
        print('--------ALL ClASSES--------')
        for key , value in self.classrooms.items():
            print(key)
            
        print('------All Classes and Students------')
        total_student = 0
        for key,value in self.classrooms.items():
            total_student +=len(self.classrooms[key].student)
            print(key,' : ',value)
            print('----------------------')
        print(f'The total students of this School is : {total_student}')
        # eight = self.classrooms['Eight']
        # for student in eight.student:
        #     print(student.name)
        return ''
            
class ClassRoom:
    def __init__(self,name) -> None:
        self.name = name
        self.student = []
        self.subject = []
        
    def add_student(self, student):
        serial_id = f'{self.name}--{len(self.student)+1}'
        student.id = serial_id
        self.student.append(student)
        
    def __str__(self) -> str:
        return f'{self.name}--{len(self.student)}'
    
    #TODO : sort student by grade
    def get_top_students(self):
        pass