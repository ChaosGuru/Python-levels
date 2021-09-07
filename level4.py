""" Lambda functions

lambda x: do staff with x   - usually is used as parameter to functions
"""


def main(greet):
    greet("Hello, World")


if __name__=='__main__':
    main(lambda x: print(x))