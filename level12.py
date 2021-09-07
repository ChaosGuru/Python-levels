""" Class

class name: - define class
__init__    - the method calls upon object creation
self    - reference to self object inside class
"""


class Greetings:
    def __init__(self, greeting):
        print(greeting)


if __name__=='__main__':
    Greetings("Hello, World")