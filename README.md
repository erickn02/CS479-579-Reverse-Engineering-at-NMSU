# CS479-579-Reverse-Engineering-at-NMSU

Welcome to this repository dedicated to gathering reports on the reverse engineering of malware samples, based on the content of the book "Practical Malware Analysis." Within this collection, you will find various reports from malware analysis as the semester of spring 2024 progresses in the Class of Reverse Engineering at NMSU.

My goal for these reports is for them to serve as a landscape of what has been done not only in the class but also as the learning curve in this field of study.

## System Setup

Setting up your reverse engineering system is not an easy task, there are several factors and procedures to be done in order to have a functional system to work with.

### System Isolation and System Network

For our system isolation, we have to be working from either Linux or macOS, this will allow us to use a Windows Virtual Machine and work with the malware inside that Virtual Machine. The reason for using a different operating system is to use the host operating system differently than the malware file to prevent the malware from escaping outside that environment. By doing so, we have a backup in case the malware exits from the Virtual Machine, this is also why we are taking other precautions.

Other precautions we are taking are the System network
