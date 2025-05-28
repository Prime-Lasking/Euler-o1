import math as m
user_input: str = input('You:').lower()
def Log2():
    print(f'Sure Let\'s do some base 2 logs Please provide a number')
    try:
        num: float = float(input('The number: '))
        print(f'The answer is {m.log2(num)}')
    except ValueError:
        print(f'That doesn\'t seem to be a valid number.')
def Log10():
    print(f'Sure Let\'s do some base 10 logs Please provide a number')
    try:
        num: float = float(input('The number: '))
        print(f'The answer is {m.log10(num)}')
    except ValueError:
        print(f'That doesn\'t seem to be a valid number.')
def Log3():
    print(f'Sure Let\'s do some base 3 logs Please provide a number')
    try:
        num: float = float(input('The number: '))
        print(f'The answer is {m.log3(num)}')
    except ValueError:
        print(f'That doesn\'t seem to be a valid number.')
def Log4():
    print(f'Sure Let\'s do some base 4 logs Please provide a number')
    try:
        num: float = float(input('The number: '))
        print(f'The answer is {m.log4(num)}')
    except ValueError:
        print(f'That doesn\'t seem to be a valid number.')
def Log5():
    print(f'Sure Let\'s do some base 5 logs Please provide a number')
    try:
        num: float = float(input('The number: '))
        print(f'The answer is {m.log5(num)}')
    except ValueError:
        print(f'That doesn\'t seem to be a valid number.')
def Logn():
    print(f'Sure Let\'s do some base n logs Please provide a number')
    try:
        num: float = float(input('The number: '))
        base: int = int(input('The base: '))
        print(f'The answer is {m.log(num,base)}')
    except ValueError:
        print(f'That doesn\'t seem to be a valid number.')

