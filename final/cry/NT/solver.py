from pwn import *
from Crypto.Util.number import *
from itertools import combinations,product
import numpy as np

guessMatrix = np.identity(9, dtype=int)

def OBE_1(matrix, i, k):
    assert k != 0
    matrix[i] = matrix[i] * k

def OBE_2(matrix, i , j):
    assert i != j
    matrix[i], matrix[j] = matrix[j].copy(), matrix[i].copy()

def OBE_3(matrix, i , j, k):
    assert i != j
    matrix[i] = matrix[i] + matrix[j] * k

def LCM(a,b):
    return (a * b) // GCD(a, b)

def matrix_to_bytes(matrix):
    result = b"".join(bytes(list(vec)) for vec in matrix).rstrip(b"\xff")
    return result


context.log_level = "warning"

e = 0x10001
batas = 40
number_list = list(range(1,batas+1))

list_product = [i*j for i, j in list(product(number_list,repeat=2))]
list_product = list(set(list_product))

list_times = []

r = process("./server.py")

# r = remote("103.181.183.216", 18004)

iterasi = 50
for loop in range(iterasi):
    
    dapetP = False
    for _ in range(4):
        exec(r.recvline(0))
    
    start = time.time()
    
    hint_1_bit = round(hint_1.bit_length() / 1024)
    hint_2_bit = round(hint_2.bit_length() / 1024)
    KPK = LCM(hint_1_bit,hint_2_bit)
    power_hint_1 = KPK // hint_1_bit
    power_hint_2 = KPK // hint_2_bit
    
    hint_1 %= n
    hint_2 %= n
    

    hint_1 = pow(hint_1, power_hint_1, n)
    hint_2 = pow(hint_2, power_hint_2, n)

    for u in list_product:
        u_pow = pow(u, power_hint_2, n)
        for v in list_product:
            hint_1_u = (hint_1 * u_pow) % n
            hint_2_v = (hint_2 * pow(v, power_hint_1, n)) % n
            p = GCD(hint_1_u + hint_2_v, n)
            if p == 1:
                p = GCD(hint_1_u - hint_2_v, n)
                if p == 1:
                    continue
            dapetP = True
            break
        if dapetP:
            break

    d = pow(e,-1,p-1)
    secret = str(pow(c,d,p)).encode()
    

    r.sendlineafter(b"? ", secret)
    
    times_taken = time.time() - start
    list_times.append(times_taken)

    r.recvuntil(b"Good Job!\n")
    if (loop + 1) % 10 == 0:
        avg_times = round(sum(list_times) / (loop + 1), 2)
        print(f"stage {loop + 1}, {avg_times = } seconds")
print()
avg_times = round(sum(list_times) / iterasi, 2)
# print(f"{avg_times = } seconds")
print()

r.recvuntil(b"you\n\n")


# OBE_1(guessMatrix, 0 , 42)

nrow = 9
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

forYou = []
for i in range(9):
    forYou.append(eval(r.recvline(0)))

forYou = np.array(forYou)

print(guessMatrix)

flagMatrix = np.dot(np.linalg.inv(guessMatrix), forYou)
flagMatrix = list(flagMatrix)
flag = []
for i in range(nrow):
    for j in range(nrow):
        flag.append(round(flagMatrix[i][j]))

print(bytes(flag))

r.interactive()