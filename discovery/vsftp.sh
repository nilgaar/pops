#!/bin/bash
echo "========================================"
echo "=========== vsFTPd Discovery ==========="
echo "========================================"
# Check if this machines is running vsFTPd
if [ -z "$(ps aux | grep vsftpd | grep -v grep)" ]; then
    echo "vsFTPd is not running"
fi

# Check if the vsFTPd configuration file exists
if [ ! -f "/etc/vsftpd.conf" ]; then
    echo "vsFTPd configuration file does not exist"
else
    echo "vsFTPd configuration file exists"
    echo "Checking if the configuration file allows anonymous login"
    if [ -z "$(grep -i "anonymous_enable=YES" /etc/vsftpd.conf)" ]; then
        echo "Anonymous login is not allowed"
    else
        echo "Anonymous login is allowed"
        echo "Try: ftp <IP>"
        echo "Login: anonymous"
    fi
    echo "Checking if the configuration file allows local users to login"
    if [ -z "$(grep -i "local_enable=YES" /etc/vsftpd.conf)" ]; then
        echo "Local users are not allowed to login"
    else
        echo "Local users are allowed to login"
    fi
    echo "Checking if the configuration file allows FTP users to write to the filesystem"
    if [ -z "$(grep -i "write_enable=YES" /etc/vsftpd.conf)" ]; then
        echo "FTP users are not allowed to write to the filesystem"
    else
        echo "FTP users are allowed to write to the filesystem"
    fi
    echo "Checking if the configuration file allows FTP users to upload files"
    if [ -z "$(grep -i "anon_upload_enable=YES" /etc/vsftpd.conf)" ]; then
        echo "FTP users are not allowed to upload files"
    else
        echo "FTP users are allowed to upload files"
    fi
fi

# Check ftpusers file
# /etc/ftpusers : this file is used to deny certain users access to the FTP service
if [ ! -f "/etc/ftpusers" ]; then
    echo "ftpusers file does not exist"
else
    echo "ftpusers file exists"
    echo "Checking if the ftpusers file contains any users"
    if [ -z "$(cat /etc/ftpusers)" ]; then
        echo "No users are denied access to the FTP service"
    else
        echo "The following users are denied access to the FTP service:"
        cat /etc/ftpusers
    fi
fi

echo "========================================"
echo "========================================"
