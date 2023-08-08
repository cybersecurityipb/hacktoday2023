#!/usr/bin/python3

from Crypto.Util.number import *
import os, random, time

with open("flag.txt","r") as f:
    FLAG = f.read().rstrip()
    f.close()

NBIT = 2048
e = 0x10001
BATAS = 40
NUMBER_LIST = list(range(-BATAS,0)) + list(range(1,BATAS+1))
LIST_TIMES = []

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

    if avg_times < 5:
        print(f"Congrats!\nHere's the flag : {FLAG}")
    else:
        print(f"Nice Try!. {avg_times}")


if __name__ == "__main__":
    main()    