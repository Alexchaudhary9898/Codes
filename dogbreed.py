class Dog:
    species = "Canine"
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def show(self):
        print(f"{self.name} is a {self.breed} ({Dog.species})")
d1 = Dog("tommy", "labrador")
d2 = Dog("bruno", "beagle")
d1.show()
d2.show()