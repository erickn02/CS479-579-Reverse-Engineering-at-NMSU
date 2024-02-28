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
KEYGEN GOES HERE
```
> SUMMARY GOES HERE
---
---
---
# controlflow1-1.zip

## KeyGen4
```python
KEYGEN GOES HERE
```
> SUMMARY GOES HERE
---
---
---
# controlflow2-1.zip

## KeyGen5
```python
KEYGEN GOES HERE
```
> SUMMARY GOES HERE

