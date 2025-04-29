import csv

# ! First implementation

# name = input("What's your name? ")
# home = input("What's your home? ")

# with open("new_students.csv", "a")as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])

# ! Second implementation

name = input("What's your name? ")
home = input("What's your home? ")

with open("new_students.csv", "a")as file:
    # The fieldname must match the order in which we are writting those data...
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    # ... so the order in which we're appending it does not matter
    writer.writerow({"home": home, "name": name})