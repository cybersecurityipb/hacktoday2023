from gmpy2 import *
from libnum import *
import time

t = time.time()

e = 0x10001
batas = 0x3e8
number_list = list(range(10,batas+1))

list_product = [i*j for i, j in list(product(number_list,repeat=2))]
list_product = list(set(list_product))
print(len(list_product))

exec(open('output.txt').read())

i = 0
while(x % n == 0):
    x = x//n
    i += 1

w = 2*i + 13
x = x//nCk(w,i)
x = x//pow(7*3, i)
z = pow(21*n,13)
x_quad = pow(x, 2)
multiplier = 4 * z
list_product = list(map(lambda x: pow(x, w), list_product))

m = None

iterasi = 0
for prod in list_product:
    iterasi += 1
    tmp = multiplier * prod
    cek = iroot(x_quad + tmp,2)
    if cek[1]:
        a_2 = x + int(cek[0])
        p = gcd(a_2,n)
        if p > 1:
            q = n//p
            d = pow(e, -1, (p-1)*(q-1))
            m = pow(c,d,n)
            break
    if iterasi % 10000 == 0:
        print(iterasi)

print(n2s(m).decode(), iterasi, time.time() - t)
