import csv

students = []

"""
With this first approach, the reader is very sensible to columns switching
"""
# with open("names.csv") as file:
#     reader = csv.reader(file)
#     for name, home in reader:
#         students.append({"name": name, "home": home})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

"""
In this second approach, the `DictReader` solves the problem for us,
at the condition that the first row are the names of the columns
"""

with open("names.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")