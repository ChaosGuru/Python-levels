""" Inherited from parent

inheritance, encapsulating and polymorphism
"""


class Parent:
    def __init__(self, greeting):
        self.greeting = greeting

    def greet(self):
        print("Gōdne ǣfen")


class Child(Parent):
    def greet(self):
        print(self.greeting)


if __name__=='__main__':
    Child("Hello, World").greet()