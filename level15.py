""" Non global and non local

nonlocal    - get variable in between
"""


def outer():
    greeting = "Gōdne ǣfen"

    def inner():
        nonlocal greeting
        greeting = "Hello, World"

    inner()
    return greeting


if __name__=='__main__':
    print(outer())