""" Booling

bool and bool   - True if both are True
bool or bool    - True if any are True
not bool    - True if False
"""

if __name__=='__main__':
    true = True
    false = False

    if true and false:
        print("*and")
    elif false or false:
        print("*or")
    elif not true:
        print("*not")
    else:
        print("Hello, World")