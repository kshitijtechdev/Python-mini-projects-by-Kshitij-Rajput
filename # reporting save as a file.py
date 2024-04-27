# reporting save as a file
name = input("Enter your name: ")
rollNumber = input("Enter your roll number: ")

subjects = []
percentages = []

numSubjects = int(input("How many subjects do you have? "))

for i in range(numSubjects):
    subject = input("Enter subject " + str(i + 1) + ": ")
    percentage = input("Enter percentage for " + subject + ": ")
    subjects.append(subject)
    percentages.append(percentage)

with open("report_card.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Roll Number: " + rollNumber + "\n\n")
    file.write("Subject-wise percentages:\n")
    for subject, percentage in zip(subjects, percentages):
        file.write(subject + ": " + percentage + "%\n")

print("Report card saved successfully!")