import math
fl_g = """flag{flag}"""
def x(text, key):
    return ''.join([chr(ord(c) ^ key) for c in text])
def a(text, value):
    return ''.join([chr(ord(c) + value) for c in text])
def m(text, value):
    return ''.join([chr(ord(c) * value) for c in text])
def s(text, value):
    return ''.join([chr(ord(c) - value) for c in text])
def e(fl_g):
    enigma1 = x(fl_g, 0x55)
    enigma2 = a(enigma1, 10)
    enigma3 = m(enigma2, 2)
    enigma4 = s(enigma3, 5)
    enigma5 = x(enigma4, 0xAA)
    enigma6 = m(enigma5, 3)
    enigma7 = a(enigma6, 15)
    return enigma7
encoded_fl_g = e(fl_g)
print("Encoded Flag:")
print(encoded_fl_g)
