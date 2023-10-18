from School import School,ClassRoom
from Person import Student,Teacher

def main():
    school = School('Gaja Baba','Uttara')
    
    # add class
    Seven = ClassRoom('Seven')
    school.add_classrooms(Seven)
    
    Eight = ClassRoom('Eight')
    school.add_classrooms(Eight)
    
    Nine = ClassRoom('Nine')
    school.add_classrooms(Nine)
    
    Ten = ClassRoom('Ten')
    school.add_classrooms(Ten)
    
    Eleven = ClassRoom('Eleven')
    school.add_classrooms(Eleven)
    
    # add students
    joy = Student('joy',Seven)
    school.student_addmission(joy)
    
    jaber = Student('jaber',Eight)
    school.student_addmission(jaber)
    
    riyan = Student('riyan',Ten)
    school.student_addmission(riyan)
    
    ahmed = Student('ahmed',Nine)
    school.student_addmission(ahmed)
    
    shafil = Student('shafil',Eleven)
    school.student_addmission(shafil)
    
    print(school)
    
if __name__ == '__main__':
    main()