# name = input("What is you name? " )


# with open("student.txt", 'a') as file:
#     file.write(f"{name}\n")

# with open("student.txt") as file:
#     file = file.readlines()
#     for name in sorted(file):
#         print("Hello,",name.rstrip())

students = []
with open("students.csv") as file:
    for line in file:
        name, home = line.rstrip().split(",")
        student = {"Name": name, "Home": home}
        students.append(student)

for student in sorted(students, key = lambda student: student['Name'], reverse= True):
    print(f" {student['Name']} leaves in {student['Home']}")