# Composition example: A Course HAS-A list of students.
# The list is stored as a data field inside the Course class.

class Course:
    def __init__(currentObj, courseName = ""):
        currentObj.__courseName = courseName
        currentObj.__students = []
    
    
# getters
    def getCourseName(currentObj):
        return currentObj.__courseName
    def getStudentNames(currentObj):
        return currentObj.__students
# getter for a list
    def getNumberOfStudents(currentObj):
        return len(currentObj.__students)
# mutators/setters
    def addStudents(currentObj, student):
        currentObj.__students.append(student)
# functions
    def dropStudent(currentObj, student):
        currentObj.__students.remove(student)
        
        