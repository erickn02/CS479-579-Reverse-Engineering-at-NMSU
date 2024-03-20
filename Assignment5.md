# Summary
in order to make our python scripts executables we need to use the follwing command just like in previous assignments...
```
chmod +x name.py
```

## Decryption Program - Ransomware1.zip
> On the first Ransomware simulation we need to go through a certain process to decrypt it, once taking a glance at the Ghidra decompilation we can denote that this program needs to work with the instruction of XOR, and the way it works is that it needs to perform XOR to all bytes with the value "4", we can see this from the code provided by Ghidra in the Function called "Decrypt". That is why we need a script to achieve this without doing it manually.
![Screenshot from 2024-03-20 13-36-56](https://github.com/erickn02/CS479-579-Reverse-Engineering-at-NMSU/assets/111537523/b7bf2ee8-664e-4e11-b76c-38e880281a3a)
![Screenshot from 2024-03-20 13-29-49](https://github.com/erickn02/CS479-579-Reverse-Engineering-at-NMSU/assets/111537523/5eb7ab61-5c68-4d2b-b804-25ad21cba93e)

### Decgen.py
```python

```

## Decryption Program - Ransomware2.zip
> On the second Ransomware simulation we need to go through a certain process to decrypt it as well, we have to denote that this program also needs to work with the instruction of XOR, and the way it works on this one is that it needs to perform XOR to all bytes with the string "1337", wthen you send this to the preferred file, we are going to use the same program from thr first ransomware since both ransomware simulations can be executed with the same program, except this second one will need more specification. bytearray() helps us to store decrypted bytes prior to writing them in the .txt file.
![Screenshot from 2024-03-20 13-36-26](https://github.com/erickn02/CS479-579-Reverse-Engineering-at-NMSU/assets/111537523/c111820c-f3d4-43a3-ba48-7e61615d0d82)
![Screenshot from 2024-03-20 13-44-37](https://github.com/erickn02/CS479-579-Reverse-Engineering-at-NMSU/assets/111537523/be5b9a74-350a-46ba-89d5-32724009d0cd)
