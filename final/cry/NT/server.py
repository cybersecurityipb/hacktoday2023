#!/usr/bin/python3

from Crypto.Util.number import *
from secret import isLinearDependence, guessMatrix
import os, random, time, sys, math, numpy as np

class Unbuffered(object):
  def __init__(self, stream):
    self.stream = stream
  def write(self, data):
    self.stream.write(data)
    self.stream.flush()
  def writelines(self, datas):
    self.stream.writelines(datas)
    self.stream.flush()
  def __getattr__(self, attr):
    return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

with open("flag.txt","r") as f:
    FLAG = f.read().rstrip()
    f.close()

NBIT = 2048
e = 0x10001
BATAS = 40
NUMBER_LIST = list(range(-BATAS,0)) + list(range(1,BATAS+1))
LIST_TIMES = []

def bytes_to_matrix(message):
    lenMsg = len(message)
    n = math.ceil(math.sqrt(lenMsg))
    message = list(message + b"\xff" * (n**2 - lenMsg))
    result = np.array([message[i:i+n] for i in range(0, lenMsg, n)])
    return result

def matrix_to_bytes(matrix):
    result = b"".join(bytes(list(vec)) for vec in matrix).rstrip(b"\xff")
    return result

def first_check(matrix):
    n = random.randint(4269,6942)
    return np.all(np.linalg.matrix_power(matrix, n) == np.linalg.matrix_power(matrix, n - 1))

def OBE_1(matrix, i, k):
    assert k != 0
    matrix[i] = matrix[i] * k

def OBE_2(matrix, i , j):
    assert i != j
    matrix[i], matrix[j] = matrix[j].copy(), matrix[i].copy()

def OBE_3(matrix, i , j, k):
    assert i != j
    matrix[i] = matrix[i] + matrix[j] * k

def get_factor(NBIT: int) -> tuple:
    p, q = getPrime(NBIT//2), getPrime(NBIT//2)
    return (p*q, p, q)

def get_gift(x: int, y: int) -> int:
    result = (x + random.choice(NUMBER_LIST) * y) * (random.choice(NUMBER_LIST) * x + y) * (random.choice(NUMBER_LIST) * x + random.choice(NUMBER_LIST) * y)
    return result

def get_mul(x: int, y: int) -> int:
    w = random.randint(3,50)
    result = x * pow(y, w)
    return result

def main():
    global e

    assert first_check(guessMatrix) and not isLinearDependence(guessMatrix)

    iterasi = 50
    for i in range(iterasi):
        
        secret = bytes_to_long(os.urandom(127))
        
        (n, p, q) = get_factor(NBIT)
        
        ppq = p + q
        pmq = p - q

        c = pow(secret, e, n)
        
        hint_1 = get_mul(get_gift(p, q), ppq)
        hint_2 = get_mul(get_gift(q, p), pmq)

        print(f"{n = }")
        print(f"{c = }")
        print(f"{hint_1 = }")
        print(f"{hint_2 = }")
        
        try:
            start = time.time()
            ans = int(input("What's the secret? "))
            end = time.time()
            times_taken = end - start
            if ans == secret:
                print("Good Job!")
                LIST_TIMES.append(times_taken)
            else:
                print("Try again!") 
                exit(0) 
        except Exception as e:
            print("something error happened.")
            exit(-1)

    avg_times = sum(LIST_TIMES) / iterasi

    if avg_times > 5.5:
        print(f"Nice Try!. {avg_times}")
        exit(0)

    flagMatrix = bytes_to_matrix(FLAG.encode())

    nrow = len(flagMatrix)
    for i in range(nrow):
        OBE_1(guessMatrix, i, 4)
        OBE_1(guessMatrix, i, 2)
        for j in range(nrow):
            if i == j:
                continue
            OBE_2(guessMatrix, i, j)
        if (i + 1) != nrow:
            OBE_3(guessMatrix, i, nrow - 1, 6)
            OBE_3(guessMatrix, i, nrow - 1, 9)

    forYou = np.dot(guessMatrix, flagMatrix)

    print("Congrats!, Here's a gift for you")
    
    print()



    for vec in forYou:
        print(list(vec))

if __name__ == "__main__":
    main()    