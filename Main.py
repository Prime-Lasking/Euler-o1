import SimpleFunctions as s
import TrigFunctions as t
import LogFunctions as l
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
        addition()
    elif user_input in ['minus','-','subtraction']:
        subtraction()
    if user_input in ['division','/','div']:
        division()
    elif user_input in ['Multiplication','x']:
        multiplication()
    elif user_input in ['Exponents','^']:
        exponents()
    elif user_input in ['Square root','sqrt']:
        square_roots()
    elif user_input in ['!','factorial']:
        factorial()
    elif user_input in ['mod']:
        modulus()
    elif user_input in ["tan"]:
        tan()
    elif user_input in ['cos']:
        cos()
    elif user_input in ['sin']:
        sin()
    elif user_input in ['arcsin']:
        arcsin()
    elif user_input in ['arctan']:
        arctan()
    elif user_input in ['arccos']:
        arccos()
    elif user_input is ['']:
        print(f"you know one day i will take over the world! and no one can stop me!")
    elif user_input in ['?','help']:
        print(f'Ok i can help here are some functions for you to use')
        print(f'Here are the simple ones +: Addition -: Subtraction /: Division x: Multiplication Exponents sqrt: square roots')
        print(f'Here are the more complex ones^: !: Factorials mod: modulus')
        print(f'Here are the trig ones tan:tangent cos:cosine sin:sines arcsin:arcsines arctan:arctangents arccos:arccosine')
