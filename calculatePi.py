from math import factorial
from decimal import Decimal, getcontext
import datetime



def calc(n, precision):
    getcontext().prec = precision
    t= Decimal(0)
    pi = Decimal(0)
    deno= Decimal(0)
    k = 0
    for k in range(n):
        t = ((-1)**k)*(factorial(6*k))*(13591409+545140134*k)
        deno = factorial(3*k)*(factorial(k)**3)*(640320**(3*k))
        pi += Decimal(t)/Decimal(deno)
    pi = pi * Decimal(12)/Decimal(640320**Decimal(1.5))

    pi = 1/pi
    return pi

digitlength =  [10, 100, 200, 500, 1000, 5000, 10000, 20000]
for n in range(len(digitlength)):
    start = datetime.datetime.now()
    pi_str = calc(25, digitlength[n])
    finish = datetime.datetime.now()
    #print (pi_str)
    pi_length = len(str(pi_str))
    print ("It  took " + str(finish-start) + " to calculate " + str(pi_length) + " digits of pi")
