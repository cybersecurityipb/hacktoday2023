from Crypto.Util.number import *
from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad
from hashlib import sha256
from secret import key,FLAG
from sage.all import *
import random

def gen():
    while True:
        try:    
            p = getPrime(0x400)
            a,b = random.randrange(1,p-1),random.randrange(1,p-1)
            x = Integer(key)
            E = EllipticCurve(GF(p), [0, 0, 0, a, b])
            P = E.lift_x(x)
            Q = E(-P[1] , P[0])
            assert P[0] != -P[1]
            return p,a,b,P+Q
        except:
            print("gagal gan")
            continue

def func1(a,b,c):
    x,y,z = (a+b), (b+c), (a+c)
    return x,y,z

def func2(s,t,u):
    v,w,x = s*t, t*u, s*u
    return v,w,x

def encrypt(m: str, key: int):
    key = sha256(long_to_bytes(key)).digest()[:16]
    enc = AES.new(key, AES.MODE_ECB)
    return enc.encrypt(pad(m.encode(),16)).hex()

def main():
    p,a,b,R = gen()
    m1,m2,m3 = func1(p,a,b)
    n1,n2,n3 = func2(m1,m2,m3)
    for _ in range(5):
        m1,m2,m3 = func1(n1,n2,n3)
        n1,n2,n3 = func2(m1,m2,m3)
    enc = encrypt(FLAG,key)
    
    with open("output.txt", "w") as f:
        f.write(f"{n1 = }\n")
        f.write(f"{n2 = }\n")
        f.write(f"{n3 = }\n")
        f.write(f"{enc = }\n")
        f.write("R = 'gak dikasih'\n")


if __name__ == "__main__":
  main()

