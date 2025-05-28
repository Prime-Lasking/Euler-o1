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
    elif user_input is ['']:
        print(f"you know one day i will take over the world! and no one can stop me!")
    elif user_input in ['?','help']:
        print(f'Ok i can help here are some functions for you to use')
        print(f'Here are the simple ones +: Addition -: Subtraction /: Division x: Multiplication Exponents sqrt: square roots')
        print(f'Here are the more complex ones^: !: Factorials mod: modulus')
        print(f'Here are the trig ones tan:tangent cos:cosine sin:sines arcsin:arcsines arctan:arctangents arccos:arccosine')
