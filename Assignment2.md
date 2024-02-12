#  RE Report


##  Summary
Summary goes here

###  Type of Malware
This malware is very interesting, after looking at the dissection of this virus we have determined that it attacks the Windows OS. This malware falls into the virus category more than a worm, because even though we have to proceed with the analysis with no internet we see that this is ransomware that encrypts your data and then asks for money, but it could be a worm too that we haven't seen yet. It also looks like this is a loader virus that installs and runs or loads libraries, usually, ransomware are loader. Lastly, this malware might be a combination of things, it might have RAT since it needs to give itself access to encrypt and might also give control access to the system, this also allows this malware to be a keylogger and take control of those keys.

###  Signatures
A common way among reverse engineers is to check whether the malware they are working on has already been tested and reverse-engineered by their hash. Hash allows us to save time and check if malware has already been worked on and maybe if it has changed something to help itself be more clever to find.

The Hash of the analyzed file is...       ```35B067642173874BD2766DA0D108401B4CF45D6E2A8B3971D95BF474BE4F6282```

###  Indicators of Compromise

###  Clues about Origin
