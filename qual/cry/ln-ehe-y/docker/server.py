#!/usr/bin/env python3
from random import randrange
from numpy import matlib
import numpy as np
from z3 import *


# VARIABLES
a = randrange(1000000000)
b = randrange(1000000000)
c = randrange(1000000000)
d = randrange(1000000000)
M = 6507347070768067803177302629220355584585341427822710449

seq = [randrange(1000000000), randrange(1000000000), randrange(1000000000), randrange(1000000000)]


# MATRIX EXPONENTIATION
def matrexpo(n):
    res = np.matlib.array([
        seq,
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ], dtype=object)
    mlt = np.matlib.array([
        [0, 0, 0, a],
        [1, 0, 0, b],
        [0, 1, 0, c],
        [0, 0, 1, d]
    ], dtype=object)

    while n > 0:
        if n % 2 == 1:
            res = np.matlib.dot(res, mlt) % M

        mlt = np.matlib.dot(mlt, mlt) % M
        n //= 2
    return res[0, 0]


# CALCULATING VALUE
def calc(n):
    n = (n // 69) * 69
    return (matrexpo(n - 0 * 69) * matrexpo(n - 1 * 69)) ^ (matrexpo(n - 2 * 69) * matrexpo(n - 3 * 69))


# GENERATING CREDS
creds = 'ln_y{' + ''.join(str(matrexpo(x))[1::2] + str(matrexpo(x))[::2] + '_' for x in range(10))[:-1] + '}'
print(f'creds:', creds)


# GENERATING PASSWORD
password = 0
for i in range(1, 10):
    password ^= calc(1111111111111111111111111111111111111 * i)


# CHECKER
checker = int(input('\n\ninfokan password kaks.... hihihi :V\n'))
if checker != password:
    print('\nkamu bukan orang yang aku kenal >:(')
else:
    with open("flag.txt", "rb") as file:
        flag = file.read().decode()
        file.close()
        
    print('\nehehe~ ahaha~ nih hadiah ^_^')
    print(flag)