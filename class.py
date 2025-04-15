#Create a class representing anything you like a book
#Add attributes and methods to bring the class to life!
#Use constructors to initialize each object with unique values.
#Add an inheritance layer to explore polymorphism or encapsulation.

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        print(f"Reading '{self.title}' by {self.author}.")

    def info(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages."
    


#Create a program that includes animals or vehicles with the same
 #action (like move()). However, make
# each class define move() differently (for example, Car.move()
 # prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️)
class Animal:
    def __init__(self, name):
        self.name = "cat"

    def move(self):
        print(f"{self.name} is moving.")






