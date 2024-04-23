# Malware Behavior

## njRAT Anti-viruz Program
The njRAT remover I have created has a simple functionality, what it does is that it takes predetermined information from the malware and sets the parameters for the anti-virus to look for them, this means, we define the following files to look for and it makes sure to look for both on startup files and also task manager, as well as files created by njRAT.

* > njq8.exe
* > njRAT.exe
* > windows.exe
* > windows.exe.tmp
* > ecc7c8c51c0850c1ec247c7fd3602f20.exe

Starting by giving the program locations to look for, we allow the program to look here before it jumps to the task manager or processes of the computer.
```python
    for root_file in root_files:
        if os.path.exists(os.path.join("C:\\", root_file)):
            programs_found.append(root_file[:-4])
        if os.path.exists(os.path.join(startup_folder, root_file)):
            programs_found.append(root_file[:-4])
        if os.path.exists(os.path.join(temp_folder, root_file)):
            programs_found.append(root_file[:-4])
```

After that, the program proceeded to find and remove files upon button interaction if any declared files were found. A restart might or might not be expected depending on the resources dedicated to the VM, but once the program displays " No Programs found" then it means that the run of the program did not find any recognizable names either on processes or startup apps. The A/V system is designed to only look and only remove upon request, even though automation could be developed.

https://github.com/erickn02/CS479-579-Reverse-Engineering-at-NMSU/assets/111537523/4dda752d-ecbc-4002-8ecd-d4cd2b8ee8f7

