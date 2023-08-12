#!/usr/bin/python3

import sys
import random
from string import printable

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

char_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
dict = {}

def generate():
  for i in printable:
    length = 5
    temp = random.choices(char_list, k=length)
    while temp in dict.values():
      temp = random.choices(char_list, k=length)
    dict[i] = ''.join(temp)
      
def encrypt(msg):
    hehe = ""
    for i in msg:
      hehe += dict[i]
    return hehe

def main():
    flag = open("flag.txt", "r").read().strip()
    while True:
      generate()
      try:
          print("please input a text")
          masuk = input("> ")
          print(f"ciphertext: {encrypt(masuk) + encrypt(flag)}\n")
      except:
          print("\nsomething error")
          break

if __name__ == "__main__":
    main()