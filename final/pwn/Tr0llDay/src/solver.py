from pwn import *
from sys import *

p = process("./runner.py")
HOST = 'localhost'
PORT = 13337

cmd = """
b*main
"""
if(argv[1] == 'gdb'):
	gdb.attach(p,cmd)
elif(argv[1] == 'rm'):
	p = remote(HOST,PORT)


file = open("solver", "rb").read()
p.sendlineafter(b'len: ', str(len(file)))
sleep(1)
p.sendline(file)

p.interactive()