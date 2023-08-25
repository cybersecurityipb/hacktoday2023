#!/usr/bin/python3
from pwn import *

#r = remote("103.181.183.216", 19000)
r = process("./server.py", level="debug")

kamus = {}
db = open('database.txt', 'r').readlines()
for i in db:
    assert '? ' in i and i.count('? ') == 1
    i = i.strip().split('? ')
    # print(i[0]+'?')
    kamus[i[0]+'?'] = i[1]

count = 0
while count != 100:
    r.recvline_startswith(b"nyawa")
    soal = r.recvline(0).decode()
    # print(soal[:-1])
    # print(kamus[soal][:-1])
    # print(kamus[soal])
    r.sendlineafter(b": ", kamus[soal])
    if b"salah" in r.recvline(0):
        break
    count += 1
r.interactive()