from pwn import *
from string import printable

# r = remote("34.101.175.204", 18020)
r = process("./server.py")

def send(msg):
    r.recvuntil(b"> ")
    r.sendline(msg)
    a = r.recvline_startswith(b"ciphertext")
    a = a.replace(b"ciphertext: ", b"")
    return a

def main():
    flag = ""
    pjg = 5
    while "}" not in flag:
        for i in printable:
            tmp = send(flag+i)
            if tmp[:len(flag)*pjg + pjg] == tmp[len(flag)*pjg + pjg:2*(len(flag)*pjg + pjg)]:
                flag = flag + i
                print(flag)
                break
    print(f"flag : {flag}")
    
if __name__ == "__main__":    
    main()
