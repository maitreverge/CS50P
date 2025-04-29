name = input("What's your name? ")

# Open with `w` erase everytime, but open it with `a` means append
# file = open("names.txt", "w")

# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

"""
When manipulating File I/O, it is way too easy to forget to close the fd.
Most of the time, it is not a big deal, but it can lead to problems like
corrupted files, lost data and so on.

Another way of typing it is to introduce a new word called `with`
"""

with open("names.txt", "a") as file:
    file.write(f"{name}\n")