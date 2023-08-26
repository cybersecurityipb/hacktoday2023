from numpy import matlib
import numpy as np
from z3 import *


# GET CREDENTIALS
creds = input('credentials: ')[5:-1].split('_')


# DECODE SEQUENCE FROM CREDENTIALS
seq = []
for x in creds:
    result = ''
    for i in range(len(x) // 2):
        result += x[len(x) // 2 + i] + x[i]
    if len(x) % 2 == 1:
        result += x[-1]
    seq.append(int(result))


# SOLVE Z3
M = 6507347070768067803177302629220355584585341427822710449
a, b, c, d = Ints('a b c d')
s = Solver()

s.add(a <= 1000000000)
s.add(b <= 1000000000)
s.add(c <= 1000000000)
s.add(d <= 1000000000)
for i in range(4, 8):
    s.add((seq[i - 4] * a + seq[i - 3] * b + seq[i - 2] * c + seq[i - 1] * d) == seq[i])

if s.check() == sat:
    model = s.model()
    a = int(str(model.eval(a)))
    b = int(str(model.eval(b)))
    c = int(str(model.eval(c)))
    d = int(str(model.eval(d)))
else:
    print('run ulang bang hehe :V')
    exit()


# MATRIX EXPONENTIATION
def matrexpo(n):
    res = np.matlib.array([
        seq[:4],
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


# GENERATING PASSWORD
password = 0
for i in range(1, 10):
    password ^= calc(1111111111111111111111111111111111111 * i)
print(password)