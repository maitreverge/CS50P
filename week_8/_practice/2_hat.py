import random

# This design allows the user to instanciate multiples sorting hats
# Which are not meant to exist multiples times.
class Hat:
    def __init__(self):
        self.houses = ["Gryfondor", "Serdaigle", "Poufsoufle", "Serpendart"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))

def main():
    hat = Hat()
    hat.sort("Harry")

if __name__ == "__main__":
    main()