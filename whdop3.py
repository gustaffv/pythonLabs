#Calc

import math

x = input('enter x: ')
    function = input('choose function (sqrt, log10, log2, cos, sin, tan, pow, hypot): ')
        if function == 'sqrt':
        print('sqrtX = ' + str(math.sqrt(float(x))))
    elif function == 'log10':
        print('log10X = ' + str(math.log10(float(x))))
    elif function == 'log2':
            print('log2X = ' + str(math.log2(float(x))))
    elif function == 'cos':
        print('cosX = ' + str(math.cos(float(x))))
    elif function == 'sin':
            print('sinX = ' + str(math.sin(float(x))))
    elif function == 'tan':
            print('tanX = ' + str(math.tan(float(x))))
    elif function == 'pow':
    y = input('Enter y: ')
            print('powX, Y = ' + str(math.pow(float(x), float(y))))
    elif function == 'hypot':
    y = input('Enter y: ')
            print('hypotX, Y = ' + str(math.sqrt(int(x), int(x) + int(y), int(y))))
else:
print("incorrect input")
