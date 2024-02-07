# Code

```assembly

#Erick Nevarez
#Assignment 1

.text
.global _start
_start:
    lea den(%rip), %rdi

    xor %rsi, %rsi
    xor %rdx, %rdx
    movb $0x3b, %al
    syscall
den:
    .string "/bin/sh"
```



# Explanation
Overall explanation here

> This code loads the address of the address "/bin/sh" string into %rdi,
> sets both %rsi and %rdx to zero, sets %al to 0x3b or 59 in decimal(the
> system call number for execve), and triggers the execve system call to
> execute "/bin/sh". This essentially spawns a shell.

## Step by step

On this instruction, we set up our code with the instructions that label the start of the program.

```assembly
.text
.global _start
_start:
```

This instruction calculates the address and stores it in the %rdi register.

```assembly
    lea den(%rip), %rdi
```

On this instruction, we are simply setting both of these registers to zero.

```assembly
    xor %rsi, %rsi
    xor %rdx, %rdx
```

With this instruction, we are storing the value 59 by "moving" the equivalent value of '0x3b' into the register %al.

```assembly
    movb $0x3b, %al
```

this line is just triggering syscall,  it performs the execve system call, which executes a program.



```assembly
    syscall
```

On this instruction we are using a label we created, the next directive defines a null-terminated string containing "/bin/sh", which is what we are aiming for.
```assembly
    den:
        .string "/bin/sh"
```


## Size
> The size of this code is 25 bytes in total, I must mention that it can still be programmed into a lighter version.

> The ASCII bytes are here...
```assembly
            48 8d 3d 0a 00 00 00 48 31 f6 48 31 d2 b0 3b 0f 05 2f 62 69 6e 2f 73 68 00
```
