from Course import Course

course_Math = Course()
course_English = Course()

course_Math.addStudents("Tony Dangerous")
course_English.addStudents("Gu MarYae")
course_Math.addStudents("Ashley Carter")
course_Math.addStudents("Maya Williams")

print("Number of students in Math: ")
print(course_Math.getNumberOfStudents(), "\nStudent names: ")

for student in course_Math.getStudentNames():
    print (student)