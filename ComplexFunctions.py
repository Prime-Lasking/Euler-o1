import math as m

def Slope_Finder():
    print(f'Sure! Let\'s find the slope! Please provide 2 points x and y  ')
    try:
        x1: float = float(input('x1: '))
        y1: float = float(input('y1: '))
        x2: float = float(input('x2: '))
        y2: float = float(input('y2: '))
        print(f'The Slope is {(y2-y1)/(x2-x1)}')
    except ZeroDivisionError:
        print(f'That\'s Divison by zero')
    except ValueError:
        print(f'That doesn\'t seem to be a valid set of points.')
def Pythagorean_Theorem():
    print(f'Sure! Let\'s get c please provide a and b')
    try:
        a: float = float(input('a: '))
        b: float = float(input('b: '))
        print(f'C is equal to {m.sqrt(a**2+b**2)}')
    except ValueError:
        print(f'That dosen\'t seem to be a valid number.')
    except ZeroDivisionError:
        print('That\'s division by zero')
def Compound_Interest():
    print(f'Sure! Let\'s do some Compund interest please provide some info')
    try:
        P: float = float(input('Initial sum of money: '))
        R: float = float(input('Annual Rate(Decimal): '))
        T: float = float(input('Time(Years): '))
        N: float = float(input('The amount of times interest compounded per year: '))
        return print(f'Compounded {N} times give you {round(P*((1+R/N)**(N*T)),2)} dollars')
    except ValueError:
        print(f'That dosen\'t seem to be a valid number.')
    except ZeroDivisionError:
        print('That\'s division by zero')
def Simple_Interest():
    print(f'Sure! Let\'s do some Simple interest please provide some info')
    try:
        P: float = float(input('Initial sum of money: '))
        R: float = float(input('Annual Rate(Decimal): '))
        T: float = float(input('Time(Years): '))
        return print(f'If you add interest to your Initial sum of money you get {round(P*(1+((R/100)*T)),2)} dollars')
    except ValueError:
        print(f'That dosen\'t seem to be a valid number.')
    except ZeroDivisionError:
        print('That\'s division by zero')
def Mean():
        print("Let's calculate the Mean. Please provide some numbers.")
        try:
            data = list(map(float, input("Enter numbers separated by spaces: ").split()))
            mean_value = round(sum(data) / len(data), 2)
            print(f"Mean: {mean_value}")
        except ValueError:
            print("That doesn't seem to be a valid number.")
def Median():
    print("Let's calculate the Median. Please provide some numbers.")
    try:
        data = list(map(float, input("Enter numbers separated by spaces: ").split()))
        data.sort()
        n = len(data)
        if n % 2 == 0:
            median_value = round((data[n//2 - 1] + data[n//2]) / 2, 2)
        else:
            median_value = round(data[n//2], 2)
        print(f"Median: {median_value}")
    except ValueError:
        print("That doesn't seem to be a valid number.")

def Mode():
    print("Let's calculate the mode. Provide some numbers.")
    try:
        data = list(map(float, input("Enter numbers separated by spaces: ").split()))
        frequency = {num: data.count(num) for num in set(data)}

        mode = max(frequency, key=frequency.get)
        print(f"Mode: {mode}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

