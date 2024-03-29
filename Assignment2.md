#  RE Report


##  Summary
---
Summary goes here

###  Type of Malware
---
It was discovered during the virus's dissection that the Windows operating system is its primary target due to the PE32 Executable.

Though it is similar to viruses in that it encrypts data and demands money, it also shows certain characteristics of a worm, which we are using to determine that this is a worm that also inhibits ransomware that seeks to scam cryptocurrency.

It also seems like a loader virus, which suggests that it can install and run libraries—a feature shared by many ransomware variants. Moreover, there are hints that this malware may have more than one function, possibly even a Remote Access Trojan (RAT).

This would make it easier for it to have access to the system for encryption purposes and might even give it control. These features also imply the existence of keylogging features that allow for the recording of private keystrokes.

###  Signatures
---
In the field of reverse engineering, comparing the hash value of the malware under analysis with its analysis is an often-used approach for detection. 

By using this method, analysts can save time by determining whether the virus has already been tested and reverse-engineered. 

We speed up the process by utilizing hash values, which may reveal modifications made by the malware to improve its evasive strategies.

>The SHA-256 Hash of the analyzed file is...       ```35B067642173874BD2766DA0D108401B4CF45D6E2A8B3971D95BF474BE4F6282```

>The SHA-1 Hash of the analyzed file is...       ```D9BEB50B51C30C02326EA761B5F1AB158C73B12C```

>The MD5 Hash of the analyzed file is...       ```6999C944D1C98B2739D015448C99A291```

###  Indicators of Compromise
---
Concerning this ransomware variant, it's expected that upon infection, a file will be generated, likely in the form of a ZIP archive containing the data held hostage from the victim's system. This operation typically involves the malware altering a registry key to grant itself unrestricted access to the files, thereby facilitating its malicious activities.

Regarding the ransom process, it's conceivable that the malware may or may not establish communication with the scammer. If communication is established, it would necessitate an active internet connection. However, in this instance, it's more probable for the ransomware to adopt a passive stance, awaiting the victim's initiative to contact the scammer and initiate the process of file retrieval. 

Consequently, there's no requirement for port openings, VPN connections, or wire guard setups. While such measures aren't essential, they may serve to augment the capabilities of the malware creator and enhance the effectiveness of the scam. Some of these found capabilities are...


* Access to the ```Control Panel``` of the computer.
* Deleting of certain registries.
* Shell terminal creation.
* Mouse manager access.
* Initialization of modules.
* Stopping and removing services.
* Screen message printing or window creation.


###  Clues about Origin
---
One clue about the origin is that this file was created in April 2019, this might be the creation of the file or the modification for analysis.

The command and control structure is...

This malware was found...

This malware is similar to some specific malware threat actor...
