class Student:
    def __init__(self, first_name, last_name, major, facultyadvisor, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.facultyadvisor = facultyadvisor
        self.gpa = gpa
        #self.studentid = studentid




    def getFirstName(self):
        return self.first_name
    def getLastName(self):
        return self.last_name
    def getMajor(self):
        return self.major
    def getfacultyadvisor(self):
        return self.facultyadvisor
   # def getStudentID(self):
       # return self.studentid
    def getGPA(self):
        return self.gpa
    def getStudentTuple(self):
        return (self.getFirstName(), self.getLastName(), self.getMajor(), self.getfacultyadvisor(), self.getGPA())