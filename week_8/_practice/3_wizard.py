class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

# For class inheritance, we can just pass the class as a parameter
class Student(Wizard):
    def __init__(self, name, house):
        # super() is an object calling the parent class
        super().__init__(name)
        self.house = house


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

wizard = Wizard("Albus") 
student = Student("Harry", "Gryfondor")
professor = Professor("Severus", "Defense contre les forces du mal")
