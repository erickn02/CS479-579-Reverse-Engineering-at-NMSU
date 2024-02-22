# x86 Assembly Review Exercises, IDA and Ghidra

## Assembly Review Exercises
---
1. What is the difference between machine code and assembly?
>Machine code and assembly are both low-level programming languages. Machine code is a binary representation of instructions while assembly is a symbolic representation. Assembly gets translated into machine code by the assembler.

2. If the ESP register is pointing to memory address `0x00000000001270A4` and I execute a `pushq rax` instruction, what address will `rsp` now be pointing to?
> ```0x000000000012709C```
> rsp registers decrements by 8 bytes and points to the memory address.

3. What is a stack frame?
>The stack frame or activation record is a data structure to manage function calls and data associated with them. The stack frame contains a return address, saved registers, function parameters and local variables, previous stack frame pointer.

4. What would you find in a data section?
>  In the data section we would typically find...
>   * Global Variables
>   * Static Variables
>   * Constants
>   * Strings and initialized arrays

5. What is the heap used for?
>  The heap is used for dynamic memory allocation, dynamic data structures, data persistence, dynamic string and arrays, and dynamic memory management.

6. What is in the code section of a program's virtual memory space?
>  text or `.text` section is the part of a program's virtual memory space that contains the executable machine code instructions.

7. What does the `inc` instruction do, and how many operands does it take?
>  The `inc` or increment instruction just like the instruction's name says increments by one the value of a specific operand.

8. If I perform a `div` instruction, where would I find the remainder of the binary division (modulo)?
>  In x86 assembly language, the result is stored in two registers, the quotient in the destination register specified as the operand of the `div` instruction and the remainder in the `edx` register.

9. How does `jz` decide whether to jump or not?
>  The `jz` instruction in x86 assembly language is a conditional jump instruction that stands for "jump if zero.", In order to decide if it will jump or not it will check the zero flag in the CPU's status register.

10. How does `jne` decide whether to jump or not?
>  The `jne` instruction in x86 assembly language is also another conditional jump that stands for "jump if not equal", just like `jz`, it will check the zero flag to determine its execution.

11. What does a `mov` instruction do?
>  This instruction serves the purpose of moving data from one location to another. 

12. What does the `TF` flag do, and why is it useful for debugging?
>  The trap flag enables the single-step mode. This allows developers to step through code, analyze control flow, inspect register and memory values, and detect timing-dependent issues.

13. Why would an attacker want to control the RIP register inside a program they want to take control of?
>  The memory address of an instruction to be executed in stored in the RIP or Instruction Pointer Register. Attackers that want to take advantage of a program have to get managing access to the RIP register to control the program's control flow and reroute execution to any address.

14. What is the `ax` register and how does it relate to `rax`?
>  The `ax` register is a 16-bit register and it belongs to the lower 16 bits of the `eax` register.
>  In 64-bit mode, `ax` represents the lowest 16 bits of the `rax` register. Alternatively, the higher and lower 8 bits of the ax register are denoted by ah and al.

15. What is the result of the instruction `xor rax, rax` and where is it stored?
>  The `xor rax, rax` instruction effectively sets all of the bits in `rax` to zero.
To put it another way, it clears the rax register's contents.

16. What does the `leave` instruction do in terms of registers to leave a stack frame?
>  The leave instruction in x86 assembly language is used to clean up the current stack frame before returning from a function.

17. What `pop` instruction is `retn` equivalent to?
>  When you use `retn`, it pops a value from the stack and transfers control to that address. This value is pushed onto the stack by a preceding call instruction. Essentially, `retn` acts as a return statement in assembly language, transferring control back to the instruction immediately following the corresponding call instruction.

18. What is a stack overflow?
>  A program encounters a stack overflow error when its call stack becomes overloaded. The call stack is a part of the memory used by a program to manage function calls, store local variables, and return addresses.

19. What is a segmentation fault (a.k.a. a segfault)?
>  A program can encounter a segmentation fault when it goes beyond limits, which happens when it tries to access memory that it is not authorized to access.

20. What are the RSI and RDI registers for that gives them their name?
>  In the x86-64 architecture, the general-purpose registers RSI and RDI are frequently utilized for memory addressing and data manipulation. Their names come from their historical roles in addressing source (RSI) and destination (RDI) data during string operations, as well as from their conventional usage in the Intel x86 assembly language.
>  * RSI ->  The RSI register is  used as the source index during string operations. It holds the memory address of the source data when performing operations.
>  * RDI ->  The RDI register is  used as the destination index during string operations. It holds the memory address of the destination data where data is being written or copied during string operations.

---
# Crack me

## SCREENSHOTS 
WILL GO HERE ONCE SCREENSHOT ATTACH IS FIGURED OUT...

## How you solved it, and what the solution was.
>  I started this Crack Me by creating a Ghidra project and loading the Crack Me into it, once that was done I proceeded with decompiling it to start the analysis, since Ghidra assumes a lot of the code I had to change a few of the names to help myself keep track of what was doing what.Once I identified the function that validates the key I compared it with examples that I have seen in forums while researching the topic and realized some variable types were wrong and that it had some inconsistencies, but ultimately   I recognized that the key could work with either decimals or hex as long as the result of modulo was zero. The correct key should be 1223.
    
## Whether Ghidra or IDA was more helpful to you, and why.
>  I preferably feel more confident with Ghidra, to me it seems easier to use and the interface makes me see things better. I also like the fact that it gave me less trouble for this crack me and from an unexperienced Ghidra user I would say that it comes on top of IDA even though both are very similar but also very unique in their own way, I feel like the complexity in user-friendly interfaces is huge for me at least, it must be mentioned that both get the job done but I prefer Ghidra because it allows me to learn a bit more even though I am still fairly new to all these tools and topics, the animations in Ghidra are cool too.
