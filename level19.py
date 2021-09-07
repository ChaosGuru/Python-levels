"""  The same object

var1 is var2    - True if tow vars are the same object
"""


class Greetings:
    def __init__(self, greeting):
        self.greeting = greeting

    def greet(self):
        print(self.greeting)


if __name__=='__main__':
    g1 = Greetings("Hello, World")
    g2 = g1

    if g2 is g1:
        g2.greet()