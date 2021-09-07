""" Changing global var

global gl_var   - if you want to assign to and not only use global variable

built in, global, non local, local  - python namespaces
"""

greeting = "Gōdne ǣfen"


def update_greeting():
    global greeting
    greeting = "Hello, World"


if __name__=='__main__':
    update_greeting()
    print(greeting)