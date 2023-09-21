#!/usr/bin/python3
from hashlib import sha256
import math
import random
import os
import sys

class Unbuffered(object):
  def __init__(self, stream):
    self.stream = stream
  def write(self, data):
    self.stream.write(data)
    self.stream.flush()
  def writelines(self, datas):
    self.stream.writelines(datas)
    self.stream.flush()
  def __getattr__(self, attr):
    return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

LENGTH = 128

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

def check(num : int):
    i = 0
    while True:
        if pow(2,i)-1 >= i + num:
            break
        i+=1
    return i

def fun(a,b):
    temp = 0
    for i in range(1,len(b)+check(len(b))+1):
        if math.log2(i)%1 != 0 and (bin(i)[2:]).zfill(check(len(b)))[-a] == '1':
            temp ^= int(b[i-math.ceil(math.log2(i))-1])
    return str(temp)

def encrypt(msg):
    binary = bytes2bin(msg)[::-1]
    count = 0
    enc = ""
    for i in range(1,len(binary)+check(len(binary))+1):
        if math.log2(i)%1 == 0:
            enc += fun(int(math.log2(i))+1, binary)
        else:
            enc += binary[count]
            count += 1
    enc = flip(enc,random.randrange(0,len(enc)))
    return bin2bytes(enc[::-1])

def gen():
    temp = os.urandom(LENGTH)
    return temp, encrypt(temp)

def main():
    flag = open("flag.txt", "r").read()
    key1, enc1 = gen()
    key2, enc2 = gen()
    print(f"secret : {encrypt(enc1+enc2).hex()}")
    inp = input('give me your answer : ')
    if inp == sha256(key1+key2).digest().hex():
        print("Congratss, here's your flag")
        print(flag)
    else:
        print("Wrong, bye")
    
    
if __name__ == '__main__':
    main()