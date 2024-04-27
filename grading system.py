# grading system
print("Enter student's name: ")
name = input()

print("Enter section: ")
section = input()

print("Enter class: ")
c = input()

print("Enter roll number: ")
rollno = input()

print("Enter the number of subjects: ")
numsubjects = int(input())

print("\nEnter subject-wise marks:")

print("\nSubject-wise Grades:")
for i in range(numsubjects):
    print("Enter subject name: ")
    subject = input()
    print("Enter marks: ")
    marks = int(input())

    if (0 <= marks <= 100):
        if (90 <= marks <= 100):
            grade = "A+"
        elif (80 <= marks < 90):
            grade = "A"
        elif (70 <= marks < 80):
            grade = "B+"
        elif (60 <= marks < 70):
            grade = "B"
        elif (50 <= marks < 60):
            grade = "C+"
        elif (40 <= marks < 50):
            grade = "C"
        else:
            grade = "F"
        print(subject , ": " , grade)
    else:
        print("Invalid mark! Marks should be in the range of 0-100.")

print("\nStudent Details:")
print("Name:", name)
print("Section:", section)
print("Class:", c)
print("Roll Number:", rollno)
