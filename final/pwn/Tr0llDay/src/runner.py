#!/usr/bin/env python3
import subprocess
import tempfile
import sys
import os

len = int(input('Program len: '))
print(f'Reading {len} bytes from stdin...')

prog = sys.stdin.buffer.read(len)

f = tempfile.NamedTemporaryFile()
f.write(prog)
f.flush()

os.chmod(f.name, 0o755)
subprocess.run(["./blink", "-m", f.name], input=b'')