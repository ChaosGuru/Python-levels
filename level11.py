""" Do after loop

else    - can be used after naturally finished loop
"""


def do_nothing():
    pass


if __name__=='__main__':
    
    for i in range(1):
        do_nothing()
    else:
        print("Hello, World")

    for i in range(1):
        do_nothing()
        break
    else:
        print("Hello, World")
        print("*with break")