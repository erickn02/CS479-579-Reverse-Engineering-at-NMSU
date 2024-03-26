# Crackme # Solution ([Crackme 3](http://crackmes.cf/users/twistedtux/first_keygenme/download/keygenme.tgz))
To solve this crackme, you need to...

My solution is...
```python
#!/usr/bin/env python3

print("This is the answer!")
```
## How I did it using Ghidra...


> Screenshots and explanation here Screenshots and explanation here Screenshots and explanation here


---
---
# Crackme # Solution ([Crackme 1](http://crackmes.cf/users/seveb/crackme05/download/crackme05.tar.gz))
To solve this crackme, you need to insert a series of numbers with a lenght of 19. You also need a hyphen ('-') in positions 5, 10, and 15. It must also be noted that no symbols allowed, only letters and numbers.Positions 7, 8, 12, 13 are unbinded with the inclusion of ASCII. Position 1 is (char_14 xor char_6) + 48, position 4 is (char_11 xor char_9) + 48, position 16 is (char_11 xor char_9) + 48, and position 19 is (char_14 xor char_6) + 48.

My solution is...
```python
#!/usr/bin/env python3

print("This is the answer!")
```
## How I did it using Ghidra...

> Upon opening Ghidra and choosing to run an analysis in this file, we can see the main function with the primary structure of the crack me. Then we see a few other functions like rock, scissors, paper, decraycray, cracker. There i also another function called bomb that does a few calls to ultimately close the program. Rock function does check all 19 positions to be correct while paper checks positions "1, 4, 9, 11, 14, 16, 19", scisssors "2, 3, 17, 18", and cracker "5, 10, 15".

SCREENSHOTS HERE...
