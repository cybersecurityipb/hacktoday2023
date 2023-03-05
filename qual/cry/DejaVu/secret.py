from Crypto.Util.number import getPrime
from random import randint

def get_all_key():
    m = getPrime(100)
    c = getPrime(100)
    n = getPrime(105)
    x = randint(1000, n)
    return m,c,n,x
