""" levels 1-20
"""

allow = False


class Greetings:
    def __init__(self, greeting):
        assert type(greeting) == str
        assert "Hello" in greeting

        self.greeting = greeting


class NewGreetings(Greetings):
    def greet(self, greet_func):
        greet_func(self.greeting)


def main():
    try:
        g = NewGreetings("Hello, World")
        g1 = g

        if g1 is g:
            g1.greet(lambda x: print(x))
    except AssertionError:
        print("*assertion error")
    finally:
        return True


def change_allow():
    global allow
    allow = not allow


if __name__=='__main__':
    times_to_run_program = 9

    change_allow()    

    for _ in range(times_to_run_program):
        if allow and main():
            print("*end")
        else:
            print("*press red button")

        # lol
        break

    # why?
    del times_to_run_program