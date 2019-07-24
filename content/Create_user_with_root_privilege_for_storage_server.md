Title: Create user with root privilege for storage server
Date: 2019-07-23 23:17
Category: DevOps
Tags: security
Authors: Ace Fei


[TOC]


### Qnap
1. Ensure SSH is enable on Qnap website . **ContrlPanel -> Network & File Services -> Telnet/SSH -> Allow SSH connection**

2.  ssh to Qnap server and run below cmd.

```
adduser --gid 0 admin-last
sed -i '/^admin/aadmin-last    ALL=(ALL)    ALL' /usr/etc/sudoers
passwd admin-last
```

### NetApp
1. Enable ssh on netapp website **Secure Admin ->  SSH -> Enable/Disable**

2. Add below into ~/.ssh/config
```
Host *
    KexAlgorithms +diffie-hellman-group1-sha1
    Ciphers +3des-cbc 
```

3. ssh to Netapp and run below cmd.

```
useradmin user add root-last -c "adminstrator for netapp last resort" -g Administrators
```
In NetApp ONTAP, it might be failed as "useradmin user add" is not supported: use the "security login create" command.
As the [NetApp ONTAP Documentation](https://docs.netapp.com/ontap-9/index.jsp?topic=%2Fcom.netapp.doc.dot-cm-cmpr-950%2Fsecurity__login__create.html),
We can use below cmd. 
```
# find current vserver name
cluster1::> security login show
cluster1::> security login create -vserver vserver-name -user-or-group-name admin-last -application ssh -authentication-method password -role admin
```



### FreeNAS
1. ssh to FreeNAS.
2. add user with root privilege (set the user group is wheel)
```
# adduser
Username: root-last
Full name:
Uid (Leave empty for default):
Login group [root-last]: wheel
Login group is wheel. Invite root-last into other groups? []:
Login class [default]:
Shell (sh csh tcsh bash rbash netcli.sh ksh93 mksh zsh rzsh scponly git-shell nologin) [sh]:
Home directory [/home/root-last]:
Home directory permissions (Leave empty for default):
Use password-based authentication? [yes]:
Use an empty password? (yes/no) [no]:
Use a random password? (yes/no) [no]:
Enter password:
Enter password again:
Lock out the account after creation? [no]:
Username   : root-last
Password   : *****
Full Name  :
Uid        : 1001
Class      :
Groups     : wheel
Home       : /home/root-last
Home Mode  :
Shell      : /bin/sh
Locked     : no
OK? (yes/no): yes

# echo "%wheel ALL=(ALL) ALL" >> /etc/local/sudoers
```
