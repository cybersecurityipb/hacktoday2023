#!/usr/bin/env python3

import time
from secret import get_all_key


def bytes2bin(msg: bytes):
    return bin(int.from_bytes(msg, "big"))[2:]


def bin2bytes(msg: bytes):
    return int(msg, 2).to_bytes((int(msg, 2).bit_length() + 7) >> 3, "big") or b"\x00"


class KeyGen:
    def __init__(self, x: int, m: int, c: int, n: int):
        self.m = m
        self.c = c
        self.n = n
        self.state = x % n
        self.bitstate = bin(self.state)[2:]

    def update_state(self):
        self.state = (self.state * self.m + self.c) % self.n
        self.bitstate = bin(self.state)[2:]
        time.sleep(1)

    def get_bit(self):
        b = self.bitstate[-1]
        self.bitstate = self.bitstate[:-1]
        if not self.bitstate.isdigit():
            self.update_state()
        return int(b)


class StreamCipher:
    def __init__(self):
        m, c, n, x = get_all_key()
        self.keygen = KeyGen(x, m, c, n)

    def encrypt(self, msg: bytes):
        return bin2bytes(
            "".join([str(int(b) ^ self.keygen.get_bit()) for b in bytes2bin(msg)])
        )


def menu():
    print("""[1] Encrypt a message\n[2] Get an encrypted flag\n[3] Exit""")


def main():
    print("Loading... Please wait.")
    cipher = StreamCipher()
    fl4g = open("flag.txt", "rb").read()
    enc_fl4g = cipher.encrypt(fl4g)
    print("Welcome!")
    start = time.time()
    while start - time.time() <= 7:
        menu()
        opcode = input("[>] ").strip()
        if opcode == "3":
            break
        elif opcode == "1":
            msg = input("Message to encrypt : ").strip().encode()
            ct = cipher.encrypt(msg)
        elif opcode == "2":
            ct = enc_fl4g
        else:
            print("Maksud?")
            continue
        if len(msg) == 0:
            print("Invalid message.")
            continue
        print("Encrypted message :", ct.hex())
    return 0


if __name__ == "__main__":
    main()
