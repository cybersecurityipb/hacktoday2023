#!/usr/bin/env python3

import itertools
from pwn import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

tampung = []

r = process("./server.py", level="warning")

def encrypt(iv, msg):
    r.sendlineafter(b"[>] ", b'1')
    r.sendlineafter(b"[>] IV (hex): ", iv)
    r.sendlineafter(b"[>] Plaintext (hex): ", msg)
    r.recvuntil(b"[*] Ciphertext: ")
    ct = r.recvline(0).decode()
    return bytes.fromhex(ct)

def get():
    r.sendlineafter(b"[>] ", b'2')
    r.recvuntil(b"[*] Encrypted Flag: ")
    ct = r.recvline(0).decode()
    return bytes.fromhex(ct)


def enc(pt, key):
    iv = b"hektoday"*2
    aes = AES.new(key.encode(), AES.MODE_CBC, iv=iv)
    return aes.encrypt(pt)

def dec(pt, key):
    iv = b"hektoday"*2
    aes = AES.new(key.encode(), AES.MODE_CBC, iv=iv)
    return aes.decrypt(pt)

def main():
    iv = "00"*16
    ct = encrypt(iv.encode(), b"00")
    ct = ct[16:]
    flag = b""
    for i in range(2):
        iv = ct[i*16:i*16+16].hex()
        pt = ct[i*16+16:i*16+32].hex()
        pflag = encrypt(iv.encode(), pt.encode())[16:32]
        flag += pflag
    print(flag)
    cek = flag[16:]
    ct = get()
    characters = ['0', '1']
    all_strings = [''.join(p) for p in itertools.product(characters, repeat=16)]
    assert len(all_strings) == pow(2,16) and len(ct) == 48
    for i in all_strings:
        tampung.append(enc(cek,i))
    for i in all_strings:
        print(i)
        mid = dec(ct[:16],i)
        if mid in tampung:
            j = tampung.index(mid)
            print(flag[:16]+dec(dec(ct,i),all_strings[j]))
            break
    return 0



if __name__ == "__main__":
    main()
    r.close()