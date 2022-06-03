class Courses:
    #intializing self variables for name and ID
    def __init__(self, name, ID):
        self.name = name 
        self.id = ID
        
    def getName(self):
        return self.name
    
    def getId(self):
        return self.id
    
    #Method to display the tile and the course id
    def display(self):
        print('Title: {}  \nID: {}'.format(self.name, self.id))
    
class OfferedCourse(Courses):
    
    #intializing self variables for name and ID along with the student IDs
    def __init__(self, name, ID, idno):
        super().__init__(name, ID)
        self.idno = idno
            
    def getNumberStudents(self):
        return len(self.idno)
    
    #method to add a student 
    def addStudent(self,idno):
        if idno in self.idno:
            print("The student {} is already there" .format(self.idno))
        else:
            self.idno.append(self.idno)
            
    #method to drop a student    
    def dropStudent(self,idno):
        if idno in self.idno:
            self.idno.remove(self.idno)
        else:
            print("The student {} is not there" .format(self.idno))
            
    #method to display the tile and the course id from the super class along with the number of students            
    def display(self):
        super().display()
        print("Enrolment: {}" .format(self.getNumberStudents()))
        
        
class StudentCourse(Courses):
    
    ##intializing self variables for name and ID along with the grade
    def __init__(self, name, ID, grade):
        super().__init__(name, ID)
        self.grade = grade
        
    def getGrade(self):
        return self.grade
    
    #method to display the tile and the course id from the super class along with the grade
    def display(self):
        super().display()
        print("Grade: {}" .format(self.grade))
        
        
def main():
    course1 = Courses("Introduction to Programming", 83713)
    course1.display() #output display for the tile and the course id
    studentlst1 = OfferedCourse("Introduction to Programming", 83713, [1,2,3,4,5,6,7]) #passing in a list for student ids
    studentlst1.display #output display from the super class along with the number of students
    print()
    studentlst1.addStudent(8)   #adding a student and displaying it
    studentlst1.display()
    print()
    studentlst1.dropStudent(4)  #removing a student and displaying it
    studentlst1.display()
    print()   
    grade1 = StudentCourse("Introduction to Programming", 83713, 88)
    grade1.display()  #output display from the super class along along with the grade
    
main()
