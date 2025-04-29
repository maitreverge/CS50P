students = []

# ! Attenpt one to sort student regarding their Names

# with open("names.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}")

# for student in sorted(students):
#     print(student)

# ! Attempt 2  to sort student regarding their Names
# with open("names.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)

# def get_name(student):
#     return student["name"]

# for student in sorted(students, key=get_name):
#     print(f"{student['name']} is in {student['house']}")

# ! Attempt 3 = lamdba functions
with open("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

# def get_name(student):
#     return student["name"]

# Lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.
# It is a way to create small, one-time, anonymous function objects in Python.
# The lambda function is used to sort the list of students by their names.
# The lambda function takes one argument, student, and returns the value of the "name" key in the student dictionary.
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")