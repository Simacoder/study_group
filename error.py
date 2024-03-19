# check error 
# x = int(input('Enter your naumber: ')
import math
y = 0
x = 0
def division(y,x):
    #x = int(input('enter the number: '))
    #y = int(input('enter the nmber: '))
    #quotient = y/x
    #print(f'The quoteint is: {quotient}')
    #if not isinstance(x, (int, float)):
        #raise TypeError('x must be numeric')
    #elif x == 0:
        #raise ValueError('x cannot be negative')
    try:
        y = int(input('enter your number: '))
        x = int(input('enter your numer: '))
        quotient = y / x
    except ZeroDivisionError:
        print(f"it is illegal to divide by '{x}'")

division(y,x)
