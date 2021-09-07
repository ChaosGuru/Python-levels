""" Generator

generator   - generates new value when called, do not sace in memory
yield   - return next value
next(generator) - get next value
print(text, end='') - set print end string, defalut is '\n' (new line)
"""


def greeting_generator():
    for i in "Hello, World":
        yield i


if __name__=='__main__':
    greeting = greeting_generator()
    
    try:
        while True:
            print(next(greeting), end='')
    except StopIteration:
        print("\n*last element")