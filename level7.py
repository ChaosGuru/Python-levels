""" Conditioning and False

elif    - checking second condition if first is False
else    - if all previous conditions are False

False, None, 0, '', [], (), {} - are False
"""

if __name__=='__main__':
    first_false = False
    second_false = False

    if first_false:
        print("*Hello")
    elif second_false:
        print("*World")
    else:
        print("Hello, World")