import re

name = input("What's your name? ").strip()

# This first version is really sensitive to ", " within split
# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"
# print(f"Hello, {name}")

"""
The () in regex, in addition to group things, also allows to returns data
In the following pattern :

matches = re.search(r"^(.+), (.+)$", name)
The two parenthesis will return 2 strings
"""
matches = re.search(r"^(.+), (.+)$", name)

if matches:
    last, first = matches.groups()
    name = f"{first} {last}"
    """
    or we can do
    last = matches.group(1)
    first = matches.group(2)

    OOOOOR GO EVEN FURTHER
    name = matches.group(2) + " " + matches.group(1)
    """
print(f"Hello, {name}")

"""
:=     => Walrus operator

matches = re.search(r"^(.+), (.+)$", name)
if matches:

We can turn assignment and boolean checking in the same line as follows :

if matches := re.search(r"^(.+), (.+)$", name):
    ...

"""


