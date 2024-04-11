# Dynamic Analysis


# OSINT Investigation

### Wikipedia
For this OSINT investigation, we want to start things by using Wikipedia, it's a good place to start but we are going to back up everything we find with different sources. 
Wikipedia says that " njRAT, also known as Bladabindi, is a remote access tool (RAT) with user interface or trojan which allows the holder of the program to control the end-user's computer. It was first found in June 2013 with some variants traced to November 2012." 

* [Wikipedia Source](https://en.wikipedia.org/wiki/NjRAT)

### Cyborg Security
While Wikipedia gave us a good understanding of this RAT, Cyborg Security gives us more details and maybe more accurate dates for this remote access trojan. The site does say that this RAT has been observed since 2013 and that it might have been developed since 2010, one other thing this site mentions is some of the RAT's capabilities, and the text appears just as shown below...

> "The RAT features a number of features which are characteristic of other Remote Administration Tools, including keylogging, remote control of the system, access to the command line of the compromised system, access to the victim’s camera, and file, process, and registry management. The RAT is also capable of exfiltrating credentials from browsers. Another unique characteristic of the RAT is that the authors, and other actors, have created extensive documents and tutorials to teach prospective users how to use njRAT."

* [Cyborg Security Source](https://www.cyborgsecurity.com/threats/emerging-threats/njrat/)

### CheckPoint
On this site, we get more details as to how this RAT spreads and what are possible ways to be the unlucky user that gets infected with this.
> NJRat has the ability to spread itself in a few different ways. While its primary infection vectors are phishing attacks and drive-by downloads, it also has the ability to spread itself via infected USB drives. The choice of propagation method can be set using the malware’s command and control (C2) software.
Once installed on a target system, the malware is designed to allow the attacker to remotely access and control that system.

* [CheckPoint Source](https://www.checkpoint.com/cyber-hub/threat-prevention/what-is-malware/what-is-njrat-malware/)

  This is also an activity statistic done by Gridinsoft...
  ![njrat_activityStats](https://github.com/erickn02/CS479-579-Reverse-Engineering-at-NMSU/assets/111537523/95e09d2d-61d6-4606-8902-8175cfed4499)
* [Gridinsoft Source](https://gridinsoft.com/backdoor/njrat)

# RegShot
There were a lot of registries changed and a few things that were added and deleted, some of these give NjRAT permissions that allow it to be persistent according to my assumption of these keys changed.

>> HKLM\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\FirewallRules\{E675A880-8829-4D38-8B13-2215124449B8}

I assume it gives itself permission to get past the firewall for an indefinite time.
I couldn't find more that were precise, the rest have multiple keys changed but I can't pinpoint what they do. They all look very similar.

I do understand that the firewall can help the RAT either get past it or at least not be detected, but I feel like a good way to detect this RAT in your computer can be if the keys have increased, decreased, or changed, this can be easily detected since windows keep a record of when was the last update to the keys in case they did change but were not replaced.

There are also files that could get created and if spotted then you can realize that they were not created or downloaded by you, I must say this only works if you are a person that keeps their computer in check, but a good antivirus can help detect this files for you and ask if you were involved in their creation.

# FakeNet
During class, we noticed that after running FakeNet NjRAT tried to make a DNS connection to the domain ```zaaptoo.zapto.org```, sadly after looking at the rest of the activity I couldn't get any more suspicious activity besides possible reconnection trials to the same page.

After some digging, it seemed to be a legitimate service of a remote access dynamic DNS, but with the twist of it being used for this Remote Access Trojan.

