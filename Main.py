import sqlite3
from Student import Student

conn = sqlite3.connect('StudentDB.db')
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS Student(StudentId INTEGER PRIMARY KEY AUTOINCREMENT, FirstName varchar(25),"
          "LastName varchar(25), GPA NUMERIC, Major varchar(20), FacultyAdvisor varchar(25));")

'''stu = Student ('Rene', 'FooBar', 'safsfsf', 'name', '4.0','123')
c.execute("INSERT INTO Student ('FirstName', 'LastName', 'Major', 'FacultyAdvisor', 'GPA', 'StudentID')"
          "VALUES (?,?,?,?,?,?)", stu.getStudentTuple())

stu1 = Student ('Omar', 'Arafeh', 'SE', 'Linstead', '1.0','1123')
c.execute("INSERT INTO Student ('FirstName', 'LastName', 'Major', 'FacultyAdvisor', 'GPA', 'StudentID')"
         "VALUES (?,?,?,?,?,?)", stu1.getStudentTuple())

stu2 = Student ('Jeff', 'Lingard', 'CS', 'Linstead', '2.0','2123')
c.execute("INSERT INTO Student ('FirstName', 'LastName', 'Major', 'FacultyAdvisor', 'GPA', 'StudentID')"
         "VALUES (?,?,?,?,?,?)", stu2.getStudentTuple())

stu3 = Student ('John', 'Clementine', 'Comm', 'Linstead', '3.0','3123')
c.execute("INSERT INTO Student ('FirstName', 'LastName', 'Major', 'FacultyAdvisor', 'GPA', 'StudentID')"
         "VALUES (?,?,?,?,?,?)", stu3.getStudentTuple())'''

conn.commit()
repeatThis = True

while (repeatThis):
    print ("record created: ")
    print("1) Display all: ")
    print("2) Create new: ")
    print("3) Update student: ")
    print("4) delete student: ")
    print("5) Search for a student: ")
    print("6) Exit: ")

    print ("Enter a choice")
    usersChoice = int(input("#: "))

    if (usersChoice == 1):
        c.execute("SELECT * FROM Student")
        rows = c.fetchall()
        for row in rows:
            print(row)

    elif (usersChoice == 2):
        inputCheck = True
        newFirst = raw_input("Please enter the First Name of the student: ")
        newLast = raw_input("Enter the Last name now: ")
        while (inputCheck):
            try:
                gpa = float(input("Enter GPA: "))
            except:
                print("Enter Valid GPA: ")
            else:
                inputCheck = False
        major = raw_input("Enter Major: ")
        advisor = raw_input("Enter Faculty Advisor: ")
        # inputCheckId = True
        # while (inputCheckId):
        #     try:
        #         studentid = int(input("enter student ID"))
        #     except:
        #         print("please enter valid ID")
        #     else:
        #         inputCheckId = False
        stu = Student(newFirst, newLast, gpa, major, advisor)
        c.execute("INSERT INTO Student('FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor')"
        "VALUES (?,?,?,?,?)", stu.getStudentTuple())
        conn.commit()
    
    elif (usersChoice == 3):
        stuID = int(input("Updated student Id: "))
        major = str(raw_input("Enter Major Change: "))
        advisor = raw_input ("Enter new Advisor")
        c.execute("UPDATE Student SET Major = ? WHERE StudentId = ?", (major, stuID))
        c.execute("UPDATE Student SET FacultyAdvisor = ? WHERE StudentId = ?", (advisor, stuID))

    elif (usersChoice ==4):
        stuID = input("Please enter the student ID: ")
        c.execute ("delete from Student where StudentId = (?)", (stuID,))
        conn.commit()
        print("You have deleted them. ")

    elif (usersChoice == 5):
        print("Please Check Code; was unable to get this to work")
        '''search = input ("Please enter GPA, Major, or Advisor: ")
        input = raw_input()
        if input.upper() == "GPA":
            print("What GPA would you like to search?: ")
            number = raw_input()
            c.execute("SELECT * FROM Student WHERE GPA = ?", (number,))
            result = c.fetchall()
            for x in result:
                print(x)
                break
        elif input.upper() == "Major":
            print( "What is the major?")
            major = raw_input()
            c.execute("SELECT * FROM Student WHERE Major = ?", (majorinput,))
            result = c.fetchall()
            for maj in result:
                print(maj)
                break
        elif input.upper() == "Advisor":
            print("What advisor are you searching for?: ")
            advisor = raw_input()
            c.execute("SELECT * FROM Student WHERE FacultyAdvisor = ?", (facultyinput,))
            result = c.fetchall()
            for fac in result:
                print(fac)
                break
        else:
            print("Bad Input. Please type either GPA, Major, or Faculty")'''



    elif (usersChoice == 6):
        repeatThis= False




