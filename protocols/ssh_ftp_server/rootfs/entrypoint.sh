#!/bin/ash

# generate host keys if not present
ssh-keygen -A

# FTP parameters
echo "pasv_max_port=$PASV_MAX" >> /etc/vsftpd/vsftpd.conf 
echo "pasv_min_port=$PASV_MIN" >> /etc/vsftpd/vsftpd.conf 
echo "pasv_address=$PASV_ADDRESS" >> /etc/vsftpd/vsftpd.conf 

addgroup -g 433 -S $FTP_USER
adduser -u 431 -D -G $FTP_USER -h /home/$FTP_USER -s /bin/false  $FTP_USER

echo "$FTP_USER:$FTP_PASS" | /usr/sbin/chpasswd
chown $FTP_USER:$FTP_USER /home/$FTP_USER/ -R

# Start the ftpd process
/usr/sbin/vsftpd.sh &


# Start the sshd process
# do not detach (-D), log to stderr (-e), passthrough other arguments
exec /usr/sbin/sshd -D -e "$@"

