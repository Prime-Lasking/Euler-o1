import math as m
def tan():
    print(f'Sure Let\'s do some Tangents Please provide a number')
    try:
        num: float = float(input('The number: '))
        print(f'The answer is {m.tan(num)}')
    except ValueError:
        print(f'That doesn\'t seem to be a valid number.')
def sin():
    print(f'Sure Let\'s do some sines Please provide a number')
    try:
        num: float = float(input('The number: '))
        print(f'The answer is {m.sin(num)}')
    except ValueError:
        print(f'That doesn\'t seem to be a valid number.')
def cos():
    print(f'Sure Let\'s do some cosines Please provide a number')
    try:
        num: float = float(input('The number: '))
        print(f'The answer is {m.cos(num)}')
    except ValueError:
        print(f'That doesn\'t seem to be a valid number.')
def arctan():
    print(f'Sure Let\'s do some arctangents Please provide a number')
    try:
        num: float = float(input('The number: '))
        print(f'The answer is {m.atan(num)}')
    except ValueError:
        print(f'That doesn\'t seem to be a valid number.')
def arcsin():
    print(f'Sure Let\'s do some arcsines Please provide a number')
    try:
        num: float = float(input('The number: '))
        print(f'The answer is {m.asin(num)}')
    except ValueError:
        print(f'That doesn\'t seem to be a valid number.')
def arccos():
    print(f'Sure Let\'s do some arccosines Please provide a number')
    try:
        num: float = float(input('The number: '))
        print(f'The answer is {m.acos(num)}')
    except ValueError:
        print(f'That doesn\'t seem to be a valid number.')
def cotangent():
    print(f'Sure Let\'s do some cosecants Please provide a number')
    try:
        num: float = float(input('The number: '))
        print(f'The answer is {1/(m.tan(num))}')
    except ValueError:
        print(f'That doesn\'t seem to be a valid number.')
def secant():
    print(f'Sure Let\'s do some secants Please provide a number')
    try:
        num: float = float(input('The number: '))
        print(f'The answer is {1/(m.cos(num))}')
    except ValueError:
        print(f'That doesn\'t seem to be a valid number.')
def cosecant():
    print(f'Sure Let\'s do some cosecant Please provide a number')
    try:
        num: float = float(input('The number: '))
        print(f'The answer is {1/(m.sin(num))}')
    except ValueError:
        print(f'That doesn\'t seem to be a valid number.')
