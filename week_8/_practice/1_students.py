class Student:
    """
    NOTE ON CLASS:
    Unlike CPP, we do not need to declare upfront variables
    As long as they are present in the constructor
    """
    # This is a constructor
    def __init__(self, name, house, patronus):
        self.name = name
        # ! IMPORTANT : When assigning a value with a proprety, the prorety will be called
        # ! That's why we don't have a self_house = house
        self.house = house
        self.patronus = patronus
    
    # This print the object
    def __str__(self):
        return f"{self.name} from {self.house}"

    """
    By declaring a class method, we can now instanciate and return an instance
    of the class without needing first and instance of the class itslef
    """
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        patronus = input("Patronus: ")
        return cls(name, house, patronus)
    
    # ! By convention, any method must have a self object
    def charm(self):
        match self.patronus:
            case "Cheval":
                return "🐴"
            case "Tigre":
                return "🐯"
            case "Tortue":
                return "🐢"
            case "Lapin":
                return "🐰"
            case _:
                return "🪄"
    
    # @proprety == Getter
    @property
    def house(self):
        return self._house
    
    # @house.setter == Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryfondor", "Serdaigle", "Poufsoufle", "Serpendart"]:
            raise ValueError("Wrong house")
        self._house = house
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name


def main():
    student = Student.get()
    print("Expecto Patronum")
    # student.house = "Hehe"

    # ! NOTE
    # When the setter student.house = ... is called, this is enough clues
    # to Python to call the getter


if __name__ == "__main__":
    main()
