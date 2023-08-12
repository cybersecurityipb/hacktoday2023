a = "https://youtu.be/TBTj4vdtqbg"
arr = [0, 23, 0, 29, 4, 29, 27, 1, 0, 9, 22, 0, 4, 28, 7, 6, 19, 24, 12, 24, 20, 6, 10, 28, 14, 16, 23, 21, 14, 1, 23, 6, 4, 19, 23, 0, 0, 8, 7, 25, 5, 8, 12, 11, 9, 9, 2, 16, 24, 28, 17, 2, 20, 10, 24, 5, 4, 23, 23, 17, 9, 14, 14, 15, 4, 11, 23, 1, 25, 12, 1, 4, 19, 22, 3, 25, 25, 22, 16, 28, 4, 24, 6, 10, 19, 21, 14, 7, 19, 19, 22, 2, 24, 23, 19, 15, 4, 3, 28, 20, 19, 3, 26, 27, 19, 2, 4, 18, 15, 3, 10, 22]

base5 = ""

for i in a:
    temp = ""
    val = ord(i)
    for j in range(4):
        temp = str(val%5) + temp
        val //= 5
    base5 += temp

base5_arr = [int(i) for i in base5]


for i in range(len(arr)):
    base5_arr[i] -= arr[i]
    while base5_arr[i] < 0:
        base5_arr[i] += 5


biner = ''.join(str(i) for i in base5_arr)
rill_ans = ""

for i in range(len(base5_arr)//28):
    p = biner[i*28:(i+1)*28]
    num = int(p, 2)
    ans = ((num >> 4) & 15) << 24
    ans |= ((num >> 16) & 15) << 20
    ans |= ((num >> 8) & 15) << 16
    ans |= (num & 15) << 12
    ans |= ((num >> 24) & 15) << 8
    ans |= ((num >> 20) & 15) << 4
    ans |= ((num >> 12) & 15)
    temp = str(bin(ans))[2:]
    while len(temp) < 28:
        temp = "0" + temp
    rill_ans += temp

ans = ""
for i in range(0, len(rill_ans), 7):
    temp = 0
    kali = 1
    for j in range(7):
        temp += int(rill_ans[i+6-j]) * kali
        kali *= 2
    ans += chr(temp)

while ans[-1] == '=':
    ans = ans[:-1]
print(ans)
