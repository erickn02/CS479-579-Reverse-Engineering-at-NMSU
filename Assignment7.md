# DLL Injection Prove
>  In the two pictures provided below there is proof that there is indeed some DLL injection in this program and that it loads libraries that end in ".dll". Then in the other picture, we see that the program sets a DLL directory. We also understand from the rest of the program that this DLL injection needs first to allocate some memory to write on it.

> ![dll_proof2](https://github.com/erickn02/CS479-579-Reverse-Engineering-at-NMSU/assets/111537523/ee79a0e9-de96-451f-afe5-adf0d8978713)
> ![dll_proof](https://github.com/erickn02/CS479-579-Reverse-Engineering-at-NMSU/assets/111537523/1dd5add5-5c32-4ab0-9f8f-65595774c95f)

# Victim Program of DLL Injection
>  The victim seems to be explorer, there are a few 
> ## SCREENSHOT

# Entry point of the DLL Injection
>  here
> ## SCREENSHOT

# Process of Malware Looping. ( How often does malware do something?)
>  here
> ## SCREENSHOT

# Looping Function ( What does it do every time it loops?)
>  When the program loops what it does is it create windows or message boxes that to our assumption could either ask for something or inform the victim about any events.

> ![messageBox](https://github.com/erickn02/CS479-579-Reverse-Engineering-at-NMSU/assets/111537523/e1db8f18-77d4-44f8-ac12-3de363730aff)
> ![A7_windowCreation](https://github.com/erickn02/CS479-579-Reverse-Engineering-at-NMSU/assets/111537523/06034d56-2875-42cc-b2b4-5bfed37dfb17)



