import random

# This design allows the user to instanciate multiples sorting hats
# Which are not meant to exist multiples times.
class Hat:
    def __init__(self):
        self.houses = ["Gryfondor", "Serdaigle", "Poufsoufle", "Serpendart"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))


class Hat:
    houses = ["Gryfondor", "Serdaigle", "Poufsoufle", "Serpendart"]

    """
    @classmethod
    Used when the method doesn't need an instance, but does need access to the class itself (usually to read or modify class-level data, or create instances in flexible ways).

    @staticmethod
    Used when the method doesn't need access to either the instance or the class — it's just a utility that logically belongs to the class.
    """
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))



def main():
    Hat.sort("Harry")

if __name__ == "__main__":
    main()