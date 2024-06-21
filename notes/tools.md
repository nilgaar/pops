# [Mimikatz](https://github.com/gentilkiwi/mimikatz/tree/master/modules)
PTH, PassTheHash, kerberos, golden ticket, ticket, PTK, PassTheTicket, windows, NTLM, PassTheTicket, PtT, kerberos

## Module `sekurlsa`
### `ekurlsa::tickets`
Get all tickets from a system using the Mimikatz module `sekurlsa::tickets /export`.
It will safe the tickets in files with `.kirbi` format.
The tickets that end with $ correspond to the computer account, which needs a ticket to interact with the Active Directory.
Tickets for service `krbtgt` are the TGTs.
### `sekurlsa::ekeys` needed to craft custom tickets
Dump users Kerberos encryption keys

# [Invoke-TheHash](https://github.com/Kevin-Robertson/Invoke-TheHash)
PTH, PassTheHash, WMI, SMB, windows, NTLM

# [Reverse Shell Generator](https://www.revshells.com/)
Shell, reverseShell

# [Impacket](https://github.com/fortra/impacket)
command, commandInjection, credentialDumping, protocols, ip, tcp, udp, icmp, igmp, arp, nmb, smb, smb1, smb2, smb3, msrpc, ntlm, kerberos, tds, mssql (partial), ldap (partial)

# [CrackMapExec](https://github.com/byt3bl33d3r/CrackMapExec) _weird repo status_
postExploitation, ActiveDirectory, AD, passwordSpray

# [Evil-WinRM](https://github.com/Hackplayers/evil-winrm)
PTH, PassTheHash, SMB, RDP

# [Rubeus]()
PtT, PassTheTicket, kerberos
## `dump`
Dump all tickets, must run as Administrator.


# [HashId](https://github.com/psypanda/hashID)
hash, hashId, hashIdentifier, hashType, hashFormat

# [HashCat](https://hashcat.net/hashcat/)

# [PowerView/SharpView](https://github.com/PowerShellMafia/PowerSploit/blob/master/Recon/PowerView.ps1 / https://github.com/dmchell/SharpView)
AD, ActiveDirectory, domain, Kerberoasting, ASREPRoasting

# [BloodHound](https://github.com/BloodHoundAD/BloodHound)
AD, ActiveDirectory, domain, domainController, domainAdmin, domainUser, domainGroup, domainPolicy, domainTrust

# [SharpHound](https://github.com/BloodHoundAD/BloodHound/tree/master/Collectors)
AD, ActiveDirectory, domain,ACLs, GPOs

# `realm`
AD, ActiveDirectory, ADonLinux
Get the domain name of the current user

# `sssd`
AD, ActiveDirectory, ADonLinux

# `winbind`
AD, ActiveDirectory, ADonLinux