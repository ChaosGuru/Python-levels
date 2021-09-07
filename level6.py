""" Making sure that variable is string

type(var)   - built in method to check type
"""

if __name__=='__main__':
    greeting = "Hello, World"
    
    if type(greeting) == str:
        print(greeting)