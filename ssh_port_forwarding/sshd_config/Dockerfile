FROM alpine:3.7

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

EXPOSE 22

RUN apk update && apk upgrade && apk add --no-cache openssh tcpdump bash && \
  sed -i s/#PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config && \
  sed -i s/AllowTcpForwarding.*/AllowTcpForwarding\ yes/ /etc/ssh/sshd_config && \
  echo "root:password" | chpasswd && \
  echo PS1=\"\\u@\\h:\\W \$ \" >> /root/.bashrc 

ENTRYPOINT ["/entrypoint.sh"]