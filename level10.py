""" Looping

for var in seq  - fixed number of loops
while cond  - you are not sure how many loops you need
break   - stop loop
continue    - go to the next loop
range(2)    - == [0, 1]
_   - when you do not need variable
"""


def greet():
    print("Hello, World")


if __name__=='__main__':
    
    for _ in range(1):
        greet()
        print("*1")

    while True:
        greet()
        print("*2")
        
        break
        print("*break")

    for _ in range(2):
        greet()
        print("*3")

        continue
        print("*continue")

