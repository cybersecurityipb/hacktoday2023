from gmpy2 import iroot
from Crypto.Cipher import AES
from Crypto.Util.number import *
import hashlib
from sage.all import *

a = open("output.txt", 'r')
exec(a.read())

m1 = int(iroot(n1*n3//n2,2)[0]) 
m2 = int(iroot(n1*n2//n3,2)[0]) 
m3 = int(iroot(n2*n3//n1,2)[0])
jmlh = (m1 + m2 + m3)//2
p = jmlh - m2
q = jmlh - m3
r = jmlh - m1
for _ in range(5):
    m1 = int(iroot(p*q//r,2)[0]) 
    m2 = int(iroot(p*r//q,2)[0]) 
    m3 = int(iroot(r*q//p,2)[0])
    jmlh = (m1 + m2 + m3)//2
    p = jmlh - m2
    q = jmlh - m3
    r = jmlh - m1
    
a = r
b = q
print(p,a,b)
x = PolynomialRing(IntegerModRing(p), 'x').gen()
f = x ** 3 + a * x + b
print("loading")
r0 = ((x ** 2 - b) ** 2 - f * (f + a) ** 2).roots()


for r in r0:
    key1 = hashlib.sha256(long_to_bytes(int(r[0]))).digest()[:16]
    cipher = AES.new((key1), AES.MODE_ECB)
    print(cipher.decrypt(bytes.fromhex(enc)))