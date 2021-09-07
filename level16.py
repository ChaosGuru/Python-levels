""" Display error if smthing goes wrong

try - block wher error can happen
raise   - announce error
except  - catch error
"""

if __name__=='__main__':
    try:
        raise 1
    except:
        print("Hello, World")