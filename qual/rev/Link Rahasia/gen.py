import random
a = "https://youtu.be/TBTj4vdtqbg"
b = "1ni-ri77-f74g"
idx = []

# panjangin jadi kelipatan 4
while len(b) % 4 != 0:
    b += '\x3d'

# ubah ke biner
biner = ""
for i in b:
    temp = str(bin(ord(i)))[2:]
    while len(temp) < 7:
        temp = "0" + temp
    biner += temp
print("biner:",biner)

# acak per panjang 4 / 28
# ABCDEFG --> EFBGCAD
rill_ans = ""
for i in range(len(b)//4):
    p = biner[i*28:(i+1)*28]
    num = int(p, 2)
    ans = ((num >> 4) & 15) << 20
    ans |= ((num >> 16) & 15) << 8
    ans |= ((num >> 20) & 15) << 16
    ans |= ((num >> 12) & 15)
    ans |= ((num >> 8) & 15) << 24
    ans |= (num & 15) << 12
    ans |= ((num >> 24) & 15) << 4
    temp = str(bin(ans))[2:]
    while len(temp) < 28:
        temp = "0" + temp
    rill_ans += temp
print("ans  :", rill_ans)

# ubah a ke bentuk base 5
p = ""
for i in range(len(a)):
    temp = ""
    val = ord(a[i])
    for j in range(4):
        temp = str(val%5) + temp
        val //= 5
    p += temp
print("base5:",p)

# generate array
for i in range(len(p)):
    temp = random.randint(0,5)*5 + (int(p[i]) - int(rill_ans[i])) 
    while temp < 0:
        temp += random.randint(0,5)*5
    idx.append(temp)
print(idx)