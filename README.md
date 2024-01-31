# CS479-579-Reverse-Engineering-at-NMSU

Welcome to this repository dedicated to gathering reports on the reverse engineering of malware samples, based on the content of the book "Practical Malware Analysis." Within this collection, you will find various reports from malware analysis as the semester of spring 2024 progresses in the Class of Reverse Engineering at NMSU.

The goal of these reports is to serve as a landscape of what has been done not only in the class but also as the learning curve in this field of study.

### System Setup
---
> Setting up your reverse engineering system is not an easy task, there are several factors and procedures to be done in order to have a functional system to work with.

For this setup, a Windows-based computer is used, but in order to work without any risk of malware exposure we are going to install a dual boot with the Linux system, more specifically Debian. Once this is done we will be working from the Linux boot and only then we can install a Windows virtual machine and get all our tools, IDEs, and test subjects to prepare for malware analysis. It must be mentioned that there are different ways of getting your dual boot to work, one of the easier ones is creating a partition in your drive for the new system, but we are going to be using and implementing an external SSD drive as our booting drive, this way it will only boot in Linux when that external hard drive is physically connected to the computer.

> Remember that once you have your setup with the desired software and the hypervisor or virtual machine working we must create a snapshot of that state of the system, this will allow us to go back to that saved state of the system if necessary.

### System Isolation and System Network
---
For our system isolation, we have to be working from either Linux or macOS, this will allow us to use a Windows Virtual Machine and work with the malware inside that Virtual Machine. The reason for using a different operating system is to use the host operating system differently than the malware file to prevent the malware from escaping outside that environment. By doing so, we have a backup plan in case the malware exits from the Virtual Machine, allowing us to stop the malware execution with the incompatible system. 

>This is also why we are taking other precautions, like the following...

Another precaution we are taking is the System Network isolation, with this precaution we are going to prevent the malware from communicating with the internet or any other network. This action will also prevent us from connecting to the network hence we are going to be using a host OS to do googling or downloading files and then use the host to transfer files to the Virtual Machine or Hypervisor since they are assisting us with the network isolation. In conclusion, we are taking all these precautions to ensure that our main system does not even have the possibility of being reachable by the malware since the other operating systems like Linux or macOS will stop the spread immediately due to the incompatibility.

### Windows Defender
---
To disable Windows Defender for this part of the assignment we need to first boot in the minimal safe mode to make changes, this is due to the great implementation of Windows Defender and its capabilities of persistence upon unwanted disable. After that is done you need to enter a few registry edits to make sure Windows Defender doesn't start new services. After that, we have to boot into normal mode and disable a few tasks that make Windows Defender work. This is to ensure everything will be blocked from starting Windows Defender. We must check Windows Defender to ensure that our changes had their effect.

  > Here are the services to turn off once you boot back into normal mode.
  * Windows Defender Cache Maintenance
  * Windows Defender Cleanup
  * Windows Defender Scheduled Scan
  * Windows Defender Verification

  > Registry edits to prevent any of Windows Defender's services from starting.
  ```bash
reg add "HKLM\System\CurrentControlSet\Services\WdFilter" /v "Start" /t REG_DWORD /d "4" /f
reg add "HKLM\System\CurrentControlSet\Services\WdNisDrv" /v "Start" /t REG_DWORD /d "4" /f
reg add "HKLM\System\CurrentControlSet\Services\WdNisSvc" /v "Start" /t REG_DWORD /d "4" /f
reg add "HKLM\System\CurrentControlSet\Services\WinDefend" /v "Start" /t REG_DWORD /d "4" /f
reg add "HKLM\System\CurrentControlSet\Services\Sense" /v "Start" /t REG_DWORD /d "4" /f
reg add "HKLM\System\CurrentControlSet\Services\WdBoot" /v "Start" /t REG_DWORD /d "4" /f
```

### Tools For Analysis
---
***   Progress as the semester goes...    ***
