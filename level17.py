""" Raise exception based on condition

assert condition    - raises error if condition if False
finally - do smth after
"""

if __name__=='__main__':
    try:
        assert False
    except AssertionError:
        print("Hello, World")
    finally:
        print("*finally")