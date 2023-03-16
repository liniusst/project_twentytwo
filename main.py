# Task 3
# Define the Animal, Mammal, and Primate classes.
# Animal should have a name attribute and a make_noise() method.
# Mammal should have a warm_blooded attribute and a give_birth() method.
# Primate should have an opposable_thumbs attribute and a swing() method.
# Test the classes by creating a Chimpanzee and making it do various things :)

class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def make_noise(self):
        print("Some generic animal noise")


class Mammal(Animal):
    def __init__(self, name: str, warm_blooded: bool) -> None:
        super().__init__(name)
        self.warm_blooded = warm_blooded

    def give_birth(self):
        print("Giving birth to a baby mammal")


class Primate(Mammal):
    def __init__(self, name: str, warm_blooded: bool, opposable_thumbs: bool) -> None:
        super().__init__(name, warm_blooded)
        self.opposable_thumbs = opposable_thumbs

    def swing(self):
        print("Swinging through the trees")


chimpanzee = Primate("Charlie", True, True)
print(chimpanzee.name)
print(chimpanzee.warm_blooded)
print(chimpanzee.opposable_thumbs)
chimpanzee.make_noise()
chimpanzee.give_birth()
chimpanzee.swing()
