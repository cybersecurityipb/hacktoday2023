from Crypto.Util.number import *
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib
from sage.all import *

f = open("output.txt", "r")
exec(f.read())
f.close()

def legendre(a, p):
    return pow(a, (p - 1) // 2, p)

def tonelli(n, p):
    assert legendre(n, p) == 1, "not a square (mod p)"
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        return pow(n, (p + 1) // 4, p)
    for z in range(2, p):
        if p - 1 == legendre(z, p):
            break
    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    t2 = 0
    while (t - 1) % p != 0:
        t2 = (t * t) % p
        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break
            t2 = (t2 * t2) % p
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return r

def get(p,q):        
    ttest = [(p-1, p), (q-1,q)]
    temp = []
    for n, p in ttest:
        r = tonelli(n, p)
        assert (r * r - n) % p == 0                
        a1 = r        
        L = [[p,0],[a1,1]]
        L = matrix(L)                
        L = L.LLL()                        
        temp.append(L[0])
    return temp

def gcd(a, b): 
    while b:
        a, b = b, a % b
    return a.monic()

def franklinreiter(C1, C2, e, N, a, b):
    P = PolynomialRing(Zmod(N), names='X')
    X = P.gen()
    g1 = (a*X + b)**e - C1
    g2 = X**e - C2

    phi = -gcd(g1, g2).coefficients()[0]    
    return pow(e,-1,int(phi))
    

def main():
    d = franklinreiter(hint1,hint2,3,n,2*pow(3,-1,n), 1*pow(3,-1,n))
    e = 3            
    h = RSA.construct((n,e,d))
    p = h.p
    q = h.q    
    temp = get(p,q)
    flag = b""
    for lis in temp:
        pa = abs(lis[0])
        pb = abs(lis[1])        
        key1 = hashlib.md5(long_to_bytes(pa)).hexdigest()[:16]
        key2 = hashlib.md5(long_to_bytes(pb)).hexdigest()[:16]
        enc = AES.new((key1+key2).encode(), AES.MODE_ECB)
        enc2 = AES.new((key2+key1).encode(), AES.MODE_ECB)
        length = len(arr[0])//2                                
        try:
            flag+=unpad(enc.decrypt(bytes.fromhex(arr[0])),length)
        except:
            pass
        try:
            flag+=unpad(enc.decrypt(bytes.fromhex(arr[1])),length)
        except:
            pass
        try:
            flag+=unpad(enc2.decrypt(bytes.fromhex(arr[0])),length)
        except:
            pass
        try:
            flag+=unpad(enc2.decrypt(bytes.fromhex(arr[1])),length)
        except:
            pass
    print(flag[flag.index(b"hacktoday"):] +flag[:flag.index(b"hacktoday")] )


if __name__ == "__main__":
    main()