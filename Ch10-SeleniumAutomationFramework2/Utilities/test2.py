class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + " is speaking.")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(self.name + " is speaking Bow.")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(self.name + " is speaking Meow.")


my_animal = Animal('Peso')
print(my_animal.name + " is an animal!")
my_animal.speak()

my_dog = Dog('Willie')
print(my_dog.name + " is a dog.")
my_dog.speak()
