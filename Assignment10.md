# Control Flow Integrity Violation

## Summary of the assignment
Before we started this assignment we had to do some preliminary tasks to get started...

* Install pwntools.
* Download the victim program "pizza".
* Attempt to run and crash the program successfully or get the "segmentation fault".
* Open the victim program and analyze it in Ghidra.

Then we can start to write a Python transcript from the sample in order to crash the code and analyze the core dump.

## Script and Explanation

### Python Script
```
#!/usr/bin/env python3

from pwn import *

#context.log_level = 'error'

# Executable and Linkable Format
elf = ELF("./pizza")

context(arch='amd64', os='linux', endian='little', word_size=64)

#getname_address = elf.symbols["getname"]

#shellcode = asm(shellcraft.amd64.linux.sh())

#print(f"Shellcode: {shellcode.hex().upper()}")
#print(len(shellcode))

input1 = b"Cantinflas"

victim = process("./pizza")
#print(str(victim.recvline(), "latin-1"))
#victim.recvline()
#victim.sendline(b"10")

#victim.sendline(payload)
#victim.wait()
victim.interactive()
#core = victim.corefile
#rsp = core.rsp
#rbp = core.rbp
#rip = core.rip
```

### Explanation and Screenshots
In order to crash the victim program we had to...
