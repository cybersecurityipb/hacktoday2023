from Crypto.Util.number import bytes_to_long, long_to_bytes, inverse
from sympy import primefactors
from itertools import permutations

with open('test.txt','r') as file:
	file = file.read().splitlines()

	e = 65537
	maju = 0
	full_password = []
	
	for indeks in range(0,len(file),2):
		if indeks//2 == 9:
			maju = 1
		if indeks//2 == 99:
			maju = 2 

		n = int(file[indeks][5+maju:])
		c = int(file[indeks+1][5+maju:])

		factor = primefactors(n)

		p = factor[0]
		q = factor[1]
		phi = (p-1)*(q-1)
		d = inverse(e,phi)
		m = pow(c,d,n)
		message = long_to_bytes(m).decode()
		if 'happy_birthday' not in message:
			full_password.append(message)

	for kata in permutations(full_password):
		if kata[0].endswith('_') and kata[2].startswith('_'):
			print(''.join(kata))