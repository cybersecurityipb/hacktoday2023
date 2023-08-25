#!/usr/bin/env python3

from Crypto.Util.number import bytes_to_long, long_to_bytes, inverse
from sympy import primefactors
from itertools import permutations
from pwn import *

r = remote('localhost', 18000, level = 'debug')

e = 65537
full_password = []

while True:
	cek = r.recvuntil(b'= ')
	if cek == b'\nInput Full Password = ':
		break
	n = int(r.recvline(0))
	r.recvuntil(b'= ')
	c = int(r.recvline(0))

	factor = primefactors(n)
	p = factor[0]
	q = factor[1]
	phi = (p-1)*(q-1)
	d = inverse(e,phi)
	m = pow(c,d,n)
	message = long_to_bytes(m)

	if b'happy_birthday' not in message:
		full_password.append(message)

for kata in permutations(full_password):
	if kata[0].endswith(b'_') and kata[2].startswith(b'_'):
		password = b''.join(kata)
		r.sendline(password)
		r.recvall()
