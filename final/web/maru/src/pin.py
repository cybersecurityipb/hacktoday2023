#!/usr/bin/env python3

import os
import pwd
import random
from Crypto.Util.number import isPrime
random.seed(os.urandom(8))


def next_prime(n):
    n = n | 1
    while not isPrime(n):
        n += 2
    return n


def get_prime(n):
    p = random.randint(1 << (n - 1), 1 << n)
    p = next_prime(p)
    return p


def get_pin(n):
    e = 0x17
    m = pwd.getpwuid(os.getuid())[0].encode()
    print(m)
    m = int.from_bytes(m, "big")
    p = get_prime(n >> 1)
    q = get_prime(n >> 1)
    n = p * q
    pin = pow(m, e, n)
    return hex(pin)[2:]
