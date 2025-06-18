if __name__ == "__main__":
 import SimpleFunctions as s
 import TrigFunctions as t
 import LogFunctions as l
 import ComplexFunctions as c
 import ShapesFunctions as sh
bot_name: str = 'Euler'
print(f'Hello! I\'m {bot_name}!')
flag = True

while flag is True:
    user_input: str = input('You:').lower()
    if user_input in ['hi','hello','hello euler','hi euler']:
        print(f'Hi there How can i help you')
    elif user_input in ['bye','goodbye','see you later','see you','bye euler','goodbye euler']:
        print(f'Goodbye see you next time')
        flag = False
    elif user_input in ['add', '+','addition']:
        s.addition()
    elif user_input in ['minus','-','subtraction']:
        s.subtraction()
    if user_input in ['division','/','div']:
        s.division()
    elif user_input in ['Multiplication','x']:
        s.multiplication()
    elif user_input in ['Exponents','^']:
        s.exponents()
    elif user_input in ['Square root','sqrt']:
        s.square_roots()
    elif user_input in ['!','factorial']:
        s.factorial()
    elif user_input in ['mod']:
        s.modulus()
    elif user_input in ["tan"]:
        t.tan()
    elif user_input in ['cos']:
        t.cos()
    elif user_input in ['sin']:
        t.sin()
    elif user_input in ['arcsin']:
        t.arcsin()
    elif user_input in ['arctan']:
        t.arctan()
    elif user_input in ['arccos']:
        t.arccos()
    elif user_input in ['cosecant','csc']:
        t.cosecant()
    elif user_input in ['secant','sec']:
        t.secant()
    elif user_input in ['cotanget','cot']:
        t.cotangent()
    elif user_input in ['log10']:
        l.Log10()
    elif user_input in ['log2']:
        l.Log2()
    elif user_input in ['log3']:
        l.Log3()
    elif user_input in ['log4']:
        l.Log4()
    elif user_input in ['log5']:
        l.Log5()
    elif user_input in ['log']:
        l.Logn()
    elif user_input in ['log23']:
        l.log23()
    elif user_input in ['slope']:
        c.Slope_Finder()
    elif user_input in ['pythagorean','a^2+b^2=c^2','pythagoras']:
        c.Pythagorean_Theorem()
    elif user_input in ['compound interest','compound']:
        c.Compound_Interest()
    elif user_input in ['simple interest','simple']:
        c.Simple_Interest()
    elif user_input in ['mean']:
        c.Mean()
    elif user_input in ['mode']:
        c.Mode()
    elif user_input in ['median']:
        c.Median()
    elif user_input in ['circle']:
        sh.Circle()
    elif user_input in ['triangle']:
        sh.Triangle()
    elif user_input in ['square']:
        sh.Square()
    elif user_input in ['rectangle']:
        sh.Rectangle()
    elif user_input in ['parallelogram']:
        sh.Parallelogram()
    elif user_input in ['ellipse']:
        sh.Ellipse()
    elif user_input in ['rhombus']:
        sh.Rhombus()
    elif user_input in ['trapezoid']:
        sh.Trapezoid()
    elif user_input in ['kite']:
        sh.Kite()
    elif user_input in ['polygon','regular polygon']:
        sh.Regular_Polygon()
    elif user_input in ['?', 'help']:
        print(f'Ok which functions do you need simple functions,complex functions,trig functions,log functions or shapes functions?')
    elif user_input in ['simple functions']:
        print(f'Here are the simple ones +: Addition -: Subtraction /: Division x: Multiplication Exponents sqrt: square roots')
    elif user_input in ['complex functions']:
        print(f'Here are the complex ones^: !: Factorials mod: modulus')
    elif user_input in ['trig functions','trigonometric functions']:
        print(f'Here are the trig ones tan:tangent cos:cosine sin:sines arcsin:arcsines arctan:arctangents arccos:arccosine')
    elif user_input in ['logarithms functions','Log functions']:
        print(f'Here are the Logarithms log2:log base 2 log3:log base 3 log4:log base 4 log5:log base 5 log10:log base 10 Log:Log base n')
    elif user_input in ['complex functions']:
        print(f'Here are the kind of complex ones slope:Slope finder pythagoras:pythagoras theorem compound:Compound Interest simple:Simple Interest')
    elif user_input in ['shapes','shape functions','shapes functions']:
        print(f'Here are the Shapes Circle:circle Square:square parallelogram:parallelogram Ellipse:ellipse Rhombus:rhombus Trapezoid:trapezoid Kite:kite Regular polygon:polygon')
