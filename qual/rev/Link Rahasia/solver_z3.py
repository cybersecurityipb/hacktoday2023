from z3 import *

a = [0, 23, 0, 29, 4, 29, 27, 1, 0, 9, 22, 0, 4, 28, 7, 6, 19, 24, 12, 24, 20, 6, 10, 28, 14, 16, 23, 21, 14, 1, 23, 6, 4, 19, 23, 0, 0, 8, 7, 25, 5, 8, 12, 11, 9, 9, 2, 16, 24, 28, 17, 2, 20, 10, 24, 5, 4, 23, 23, 17, 9, 14, 14, 15, 4, 11, 23, 1, 25, 12, 1, 4, 19, 22, 3, 25, 25, 22, 16, 28, 4, 24, 6, 10, 19, 21, 14, 7, 19, 19, 22, 2, 24, 23, 19, 15, 4, 3, 28, 20, 19, 3, 26, 27, 19, 2, 4, 18, 15, 3, 10, 22]

b = "https://youtu.be/TBTj4vdtqbg"
b = [ord(c) for c in b]
link = []

for i in range(len(b)):
    link.append(BitVec(str(i), 32))

# A.a()
Aa = []
for i in range(len(link)-1, -1, -1):
    charAt = link[i]
    for j in range(7):
        Aa.append(charAt % 2)
        charAt /= 2

Aa = Aa[::-1]

# A.c()
for i in range(0, len(Aa), 28):
    #A.b()
    i2 = 1
    i3 = 0
    i4 = i + 27
    while i4 >= i:
        i3 += Aa[i4] * i2
        i2 *= 2
        i4 -= 1

    Ab = i3
    i2 = (((Ab >> 4) & 15) << 20) | (((Ab >> 16) & 15) << 8) | (((Ab >> 20) & 15) << 16) | ((Ab >> 12) & 15) | (((Ab >> 8) & 15) << 24) | ((Ab & 15) << 12) | (((Ab >> 24) & 15) << 4)
    i3 = i + 27
    while i3 >= i:
        Aa[i3] = i2 % 2
        i2 /= 2
        i3 -= 1

#A.d() 
res = []
i = 0 
while i < 112 and i < len(Aa):
    Aa[i] = (Aa[i] + a[i]) % 5
    i += 1

for i2 in range(len(Aa) // 4):
    i3 = 0
    i4 = 1
    i5 = (i2+1) * 4 - 1
    while i5 >= i2 * 4:
        i3 += i4 * Aa[i5]
        i4 *= 5
        i5 -= 1
    
    tmp = If(i3 > 256, ord('='), i3) 
    res.append(tmp)

s = Solver()
for c in link:
    s.add(c > 30, c < 128)

for i in range(len(b)):
    s.add(b[i] == res[i])

if s.check() == sat:
    sol = s.model()
    print(sol)
    ans = ''
    for i in range(28):
        ans += chr(int(str(sol[link[i]])))
    print(ans)