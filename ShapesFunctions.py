import math as m
pi = m.pi
def Circle():
    print(f'Sure! Let\'s do some Circles!')
    try:
        Radius: float = float(input('Radius: '))
        print(f'The Circumference is {2*pi*Radius} The Area is {(pi**2)*Radius}')
    except ValueError:
        print(f'That doesn\'t seem to be a valid Radius.')
def Triangle():
    print(f'Sure! Let\'s do some Triangles!')
    try:
        a: float = float(input('1st side: '))
        b: float = float(input('2nd side: '))
        c: float = float(input('3rd side: '))
        base: float = float(input('Base: '))
        height: float = float(input('Height: '))
        print(f'The Perimeter is {a*b*c} The Area is {.5*base*height}')
    except ValueError:
        print(f'That doesn\'t seem valid.')
def Square():
    print(f'Sure! Let\'s do some Squares')
    try:
        a: float = float(input('A side: '))
        print(f'The Perimeter is {a*4} The Area is {a**2}')
    except ValueError:
        print(f'That doesn\'t seem valid.')
def Rectangle():
    print(f'Sure! Let\'s do some Rectangles!')
    try:
        length: float = float(input('Length: '))
        width: float = float(input('Width: '))
        print(f'The Perimeter is {(length*2)+(width*2)} The Area is {length*width}')
    except ValueError:
        print(f'That doesn\'t seem valid.')
def Parallelogram():
    print(f'Sure! Let\'s do some Parallelograms!')
    try:
        base: float = float(input('Base: '))
        height: float = float(input('Height: '))
        a: float = float(input('Long side: '))
        b: float = float(input('Short side: '))
        print(f'The Perimeter is {2*(a+b)} The Area is {height*base}')
    except ValueError:
        print(f'That doesn\'t seem valid.')
def Ellipse():
    print(f'Sure! Let\'s do some Ellipses!')
    try:
        a: float = float(input('Semi-major axis: '))
        b: float = float(input('Semi-minor axis: '))
        print(f'The Perimeter is around {pi*(((3*a)+b)-((3*a)+b)*(a+(3*b)))} there isn\'t a formula for it  The Area is {pi*a*b}')
    except ValueError:
        print(f'That doesn\'t seem valid.')
def Rhombus():
    print(f'Sure! Let\'s do some Ellipses!')
    try:
        d1: float = float(input('First diagonal: '))
        d2: float = float(input('Second diagonal: '))
        a: float = float(input('A side: '))
        print(f'The Perimeter is {4*a} The Area is {.5*d1*d2}')
    except ValueError:
        print(f'That doesn\'t seem valid.')
#Trapezoid,Kite,Regular Polygon