import math as m
#List of functions
user_input: str = input('You:').lower()
def addition():
        print(f'Sure! Let\'s do some addition! Please provide 2 numbers for me to add')
        try:
            num1: float = float(input('First number: '))
            num2: float = float(input('Second number: '))
            print(f'The sum is {num1 + num2}')
        except ValueError:
            print(f'That doesn\'t seem to be a valid number.')
def subtraction():
    print(f'Sure Let\'s do some subtraction Please provide 2 different numbers')
    try:
        num1: float = float(input('First number: '))
        num2: float = float(input('Second number: '))
        print(f'The answer is {num1 - num2}')
    except ValueError:
        print(f'That doesn\'t seem to be a valid number.')
def division():
    print(f'Sure Let\'s do some division Please provide 2 different numbers')
    try:
        num1: float = float(input('First number: '))
        num2: float = float(input('Second number: '))
        print(f'The answer is {num1 / num2}')
    except ValueError:
        print(f'That doesn\'t seem to be a valid number.')
    except ZeroDivisionError:
        print(f'That\'s division by zero')
def multiplication():
    print(f'Sure Let\'s do some multiplication Please provide 2 different numbers')
    try:
        num1: float = float(input('First number: '))
        num2: float = float(input('Second number: '))
        print(f'The product is {num1 * num2}')
    except ValueError:
        print(f'That doesn\'t seem to be a valid number.')
def exponents():
    print(f'Sure Let\'s do some Exponents Please provide 2 different numbers')
    try:
        num1: float = float(input('First number: '))
        num2: float = float(input('Second number: '))
        print(f'The answer is {num1 ** num2}')
    except ValueError:
        print(f'That doesn\'t seem to be a valid number.')
def square_roots():
    print(f'Sure Let\'s do some Square roots Please provide a number')
    try:
        num: float = float(input('The number: '))
        print(f'The answer is {num**.5}')
    except ValueError:
        print(f'That doesn\'t seem to be a valid number.')
def factorial():
    print(f'Sure Let\'s do some Factorials Please provide a number but remember factorials only use integers')
    try:
        num: int = int(input('The number: '))
        print(f'The answer is {m.factorial(num)}')
    except ValueError:
        print(f'That doesn\'t seem to be a valid number.')
def modulus():
    print(f'Sure Let\'s do a Modulus Please provide 2 different numbers')
    try:
        num1: float = float(input('First number: '))
        num2: float = float(input('Second number: '))
        print(f'The answer is {num1 % num2}')
    except ValueError:
        print(f'That doesn\'t seem to be a valid number.')
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
