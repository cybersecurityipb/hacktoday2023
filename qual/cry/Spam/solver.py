from Crypto.Util.number import bytes_to_long, long_to_bytes, inverse
from sympy import primefactors

with open('test.txt','r') as file:
	file = file.read().splitlines()

	e = 65537
	maju = 0
	full_password = []
	
	for idx in range(len(file)):
		teks = file[idx]
		
		if idx//2 == 9:
			maju = 1
		elif idx//2 == 99:
			maju = 2 

		teks = teks[5+maju:]
		
		if idx%2 == 0:
			n = int(teks)
		else:
			c = int(teks)
		
		if idx%2 == 0:
			continue

		factor = primefactors(n)

		p = factor[0]
		q = factor[1]
		phi = (p-1)*(q-1)
		d = inverse(e,phi)
		m = pow(c,d,n)
		message = long_to_bytes(m).decode()
		print(message)
		if 'happy_birthday' not in message:
			full_password.append(message)

	print(full_password)