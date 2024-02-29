# Summary of assignment
> SUMMARY GOES HERE, include chmod +x myscript.py

# ezcrackme1.zip

## KeyGen1
```python
#!/usr/bin/env python3

import random
import string
key = "picklecucumberl337"
print(key)
```
> For the first crack me I conducted a simple assembly language analysis, we did this example in class but I still found another way to find the answer, when I imported the crack me into Ghidra I started to make a quick analysis of the both the assembly and programmed code. While conducting this I realized that in the assembly code there was a string of the password needed to crack this crack me, then I proceeded to hardcode it into the KeyGen and succesfully complete this CrackMe.

![Screenshot from 2024-02-28 14-14-00](https://github.com/erickn02/CS479-579-Reverse-Engineering-at-NMSU/assets/111537523/fc6920e8-fb36-4d85-91a8-4dfe075b78fd)
![Screenshot from 2024-02-28 14-18-21](https://github.com/erickn02/CS479-579-Reverse-Engineering-at-NMSU/assets/111537523/f2176ed0-93ba-4cbb-a2da-044f73e10c50)


---
---
---
# ezcrackme2.zip

## KeyGen2
```python
#!/usr/bin/env python3

import random
import string
key = "artificialtree"
print(key)
```
> For the second CrackMe I followed the same process, before trying any Source and Sink I conduct a preliminary analysis of the Assembly and programming code provided by Ghidra. After some scrolling in the code I encountered this string of the password that I tried manually and succesfully worked.It seemed to be stored in RSI too. Then I hardcoded it into the KeyGen and properly executed it.

![Screenshot from 2024-02-28 14-26-28](https://github.com/erickn02/CS479-579-Reverse-Engineering-at-NMSU/assets/111537523/c632c58e-8f5a-422d-b228-8c9fa165e25c)


---
---
---
# ezcrackme3.zip

## KeyGen3
```python
#!/usr/bin/env python3

import random
import string
key = "strawberrykiwi"
print(key)
```

> For the third CrackMe I tried using the same method of first analysing the Assembly and programming code provided by Ghidra, by doing this I found the string ```strawberry``` , which I tried by itself manually but it did not work. After that I had to use the Source and Sink method, by doing so I followed the path from the Sink to the Source, but I was lucky to realize midway that the password was partitioned into two variables, ```FIRST_PASSWORD1``` and ```FIRST_PASSWORD2``` . When I analized this I came to the conclusion that I was missing a part of the password, so it either had to be " item + strawberry" or "strawberry + item". Once I looked where to find the missing string I found the address and I hover the mouse on top of it, then it created a quick pop-up that told me the answer and the corresponding part of it, just like shown in the following two pictures. After that I just put the password together and hardcoded it into the KeyGen.

![Screenshot from 2024-02-28 14-43-33](https://github.com/erickn02/CS479-579-Reverse-Engineering-at-NMSU/assets/111537523/a28e1ae4-890d-4ac3-81eb-b8d90d0160aa)
![Selected photo](https://github.com/erickn02/CS479-579-Reverse-Engineering-at-NMSU/assets/111537523/2f6460d2-21e5-4108-9c1a-952a5e8bce75)



---
---
---
# controlflow1-1.zip

## KeyGen4
```python
KEYGEN GOES HERE
```
> For the first Control Flow we have to discover its parameters, just like we saw in class this Control Flow needs the following...
> * A key with a lenght of 16 characters.
> * A key that has fixed the following positions [ A , 6 , ~ , 2 , ~ , ~ , ~ , % , ~ , ~ , ~ , ~ , ~ , ~ , ~ , * ]
> * Empty spots to randomize are represented as "~".

![Screenshot from 2024-02-28 17-28-42](https://github.com/erickn02/CS479-579-Reverse-Engineering-at-NMSU/assets/111537523/03fbc19a-e17f-487e-8131-cfd84e1502c9)


---
---
---
# controlflow2-1.zip

## KeyGen5
```python
KEYGEN GOES HERE
```
> SUMMARY GOES HERE

