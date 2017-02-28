# Class inheritance in Python.
class Animal:

    def __init__(self, name):
        self.name = name

    def say(self):
        print "I am an animal " + self.name


class Cat(Animal):

    def say(self):
        print "I am a cat " + self.name

class Dog(Animal):
    pass


cat = Animal("Kitty")
cat.say()

catcat = Cat("Nia")
catcat.say()

dog = Dog("Wert")
dog.say()
