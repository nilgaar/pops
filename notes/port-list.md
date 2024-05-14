|PORT|PROTOCOL|SERVICE|EXAMPLE|RESOURCES|
|---|---|---|---|---|
|20|TCP|FTP|||
|21|TCP|FTP|||
|22|TCP|SSH|||
|23|TCP|Telnet|||
|25|TCP|SMTP - Simple Mail Transfer Protocol|||
|53|TCP|DNS - Zone Transfer||
|67|UDP|DHCP|||
|68|UDP|DHCP|||
|69|UDP|TFTP|||
|79|TCP|_Finger_|||
|80|TCP|HTTP|||
|88|UDP|Kerberos|||
|110|TCP|POP3|||
_|111|TCP/UDP|SUNRPC|||_
|111|TCP|NFS - Network File System | `rpcbind  2-4 (RPC #100000)` | https://academy.hackthebox.com/module/112/section/1068|
|135|TCP/UDP|MS RPC|||
|139|TCP/UDP|NB Session|||
|161|UDP|SNMP - Simple Network Management Protocol|||
|162|UDP|SNMP - Simple Network Management Protocol|||
|137|TCP|SMB - Samba|||
|138|TCP|SMB - Samba|||
|139|TCP|SMB - Samba|||
|161|UDP|SNMP|||
|162|UDP|SNMP Trap|||
|389|TCP|LDAP|||
|443|TCP|SSL|||
|445|TCP|SMB - Samba (over IP)|||
|465|TCP|SMTP - Simple Mail Transfer Protocol|||
|514|UDP|Syslog|||
|587|TCP|SMTP - Simple Mail Transfer Protocol|||
|1433|TCP|MS-SQL|||
|2049|TCP|NFS - Network File System | `nlockmgr 1-4 (RPC #100021)` `mountd  1-3 (RPC #100005)` | https://academy.hackthebox.com/module/112/section/1068|
|3389|TCP|RDP - Remote Desktop Protocol | `ms-wbt-server Microsoft Terminal Services` | https://academy.hackthebox.com/module/112/section/1242 | 



# Enumerate
## NFS
`nmap XXX -sV -sC -p 111,2049 --script=nfs*`

`showmount -e 10.129.202.41`


pg 113