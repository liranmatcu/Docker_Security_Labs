FROM alpine
ENTRYPOINT ["/entrypoint.sh"]
EXPOSE 22
# COPY rootfs /
COPY rootfs/entrypoint.sh /
COPY rootfs/vsftpd.sh /usr/sbin/

ENV FTP_USER=foo \
    FTP_PASS=foo123 \
    PASV_ADDRESS=eurekalabs.net \
    PASV_MIN=21100 \
    PASV_MAX=21110

RUN apk update && apk upgrade && apk add --no-cache openssh vsftpd bash && \
  sed -i s/#PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config && \
  echo "root:password" | chpasswd 

RUN echo "local_enable=YES" >> /etc/vsftpd/vsftpd.conf \
  && echo "chroot_local_user=YES" >> /etc/vsftpd/vsftpd.conf \
  && echo "allow_writeable_chroot=YES" >> /etc/vsftpd/vsftpd.conf \
  && echo "background=NO" >> /etc/vsftpd/vsftpd.conf \
  && echo "ftpd_banner=Welcome to FTP Server" >> /etc/vsftpd/vsftpd.conf \
  && echo "dirmessage_enable=YES" >> /etc/vsftpd/vsftpd.conf \
  && echo "max_clients=10" >> /etc/vsftpd/vsftpd.conf \
  && echo "max_per_ip=5" >> /etc/vsftpd/vsftpd.conf \
  && echo "write_enable=YES" >> /etc/vsftpd/vsftpd.conf \
  && echo "local_umask=022" >> /etc/vsftpd/vsftpd.conf \
  && echo "passwd_chroot_enable=yes" >> /etc/vsftpd/vsftpd.conf \
  && echo "pasv_enable=Yes" >> /etc/vsftpd/vsftpd.conf \
  && echo "listen_ipv6=NO" >> /etc/vsftpd/vsftpd.conf \
  && echo "seccomp_sandbox=NO" >> /etc/vsftpd/vsftpd.conf \
  && sed -i "s/anonymous_enable=YES/anonymous_enable=NO/" /etc/vsftpd/vsftpd.conf

RUN chmod +x /entrypoint.sh
RUN chmod +x /usr/sbin/vsftpd.sh

# CMD /usr/sbin/vsftpd.sh
# CMD /entrypoint.sh