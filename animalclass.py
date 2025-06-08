from abc import ABC, abstractclassmethod
class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("i can walk and run")
class Snake(Animal):
    def move(self):
        print("i can crawl")
class Dog(Animal):
    def move(self):
        print("i can bark")
class Lion(Animal):
    def move(self):
        print("i can roar")
R = Human()
R.move()
K = Snake()
K.move()
R = Dog()
R.move()
K = Lion()
K.move()