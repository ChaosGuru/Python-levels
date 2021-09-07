""" Delete variable

del - deletes object (everything in Python is object)
"""


def foo():
    print("foo")


if __name__=='__main__':
    del foo

    try:
        foo()
    except NameError:
        print("Hello, World")