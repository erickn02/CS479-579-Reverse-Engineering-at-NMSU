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
![Screenshot from 2024-03-27 12-32-45](https://github.com/erickn02/CS479-579-Reverse-Engineering-at-NMSU/assets/111537523/c4e9483b-f480-4541-8410-2094289c7f35)
![Screenshot from 2024-03-27 12-32-58](https://github.com/erickn02/CS479-579-Reverse-Engineering-at-NMSU/assets/111537523/9fcfa997-c676-4d78-b220-3457c05bee84)
![Screenshot from 2024-03-27 12-33-11](https://github.com/erickn02/CS479-579-Reverse-Engineering-at-NMSU/assets/111537523/528064fe-d897-4f27-af16-721828ada5b8)
![Screenshot from 2024-03-27 12-33-29](https://github.com/erickn02/CS479-579-Reverse-Engineering-at-NMSU/assets/111537523/1cc38a2b-5158-4eea-b9a7-8d2aa4b81d85)
![Screenshot from 2024-03-27 12-33-39](https://github.com/erickn02/CS479-579-Reverse-Engineering-at-NMSU/assets/111537523/b0e5da3a-4ec2-4e70-bb83-968cffb42e11)
![Screenshot from 2024-03-27 12-33-51](https://github.com/erickn02/CS479-579-Reverse-Engineering-at-NMSU/assets/111537523/b1a4bbd3-ccb3-430f-b73e-08b4a1c31fe0)
![Screenshot from 2024-03-27 12-33-58](https://github.com/erickn02/CS479-579-Reverse-Engineering-at-NMSU/assets/111537523/c0a9f550-e943-4317-875f-b47b6b5fe211)
