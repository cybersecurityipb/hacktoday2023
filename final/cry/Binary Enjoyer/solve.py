
from Crypto.Util.number import *
import math
from hashlib import sha256
from pwn import *

r = process("./server.py")

def bin2bytes(binary : str):
    if len(binary) % 8 != 0:
        binary = binary.zfill(len(binary) + 8 - len(binary) % 8)
    return int(binary, 2).to_bytes(len(binary) // 8, byteorder='big')

def bytes2bin(msg : bytes):
    return bin(int.from_bytes(msg,'big'))[2:]

def flip(string : str, ind : int):
    listed = list(string)
    if listed[ind] == '0':
        listed[ind] = '1'
    else:
        listed[ind] = '0'
    return ''.join(listed)

def check1(a):
    i = 0
    while True:
        if pow(2,i)-1 >= a:
            break
        i+=1
    return i

def fun(a,b):
    temp = 0
    for i in range(1,len(b)+1):
        if math.log2(i)%1 != 0 and (bin(i)[2:]).zfill(check1(len(b)))[-a] == '1':
            temp ^= int(b[i-1])
    return str(temp)

def encrypt(msg):
    binary = msg
    enc = ""
    for i in range(1,len(binary)):
        if math.log2(i)%1 == 0:
            enc += fun(int(math.log2(i))+1, binary)
    return enc    

def solve(r):
    cor = bytes2bin(r)[::-1]
    leng = check1(len(cor))
    ham = ''
    for i in range(leng):
        ham += cor[pow(2,i)-1]
    rand = int(encrypt(cor)[::-1],2)^int(ham[::-1],2)
    q = flip(cor,rand-1)
    t = ''
    for i in range(1,len(q)+1):
        if math.log2(i)%1!= 0:
            t += q[i-1]
    return bin2bytes(t[::-1])

def get():
    temp = r.recvline(0)
    temp = temp.split()[-1].decode()
    return temp

def main():
    while True:
        #r = remote("103.167.132.101", 16000, level = 'warning')
        global r
        s = get()
        u = len(bytes2bin(bytes.fromhex(s)))
        print(u)
        t = check1(u)
        sisa = 8-(1024+check1((u-t)//2))%8
        must = 1024*2 + t + check1((u-t)//2)*2+sisa
        if len(bytes2bin(bytes.fromhex(s))) != must:
            r.close()
            r = process("./server.py")
            continue
        a = solve(bytes.fromhex(s))
        a1 = solve(a[:len(a)//2])
        a2 = solve(a[len(a)//2:])
        r.sendlineafter(b":", sha256(a1+a2).digest().hex().encode())
        r.interactive()
        break

if __name__ == '__main__':
    main()