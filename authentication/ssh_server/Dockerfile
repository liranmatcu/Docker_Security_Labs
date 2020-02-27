FROM alpine
ENTRYPOINT ["/entrypoint.sh"]
EXPOSE 22
COPY rootfs /

RUN apk add --no-cache openssh bash && \
  sed -i s/#PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config && \
  sed -i s/AllowTcpForwarding.*/AllowTcpForwarding\ yes/ /etc/ssh/sshd_config && \
  sed -i s/#HostbasedAuthentication.*/HostbasedAuthentication\ yes/ /etc/ssh/sshd_config && \
  sed -i s/#IgnoreRhosts.*/IgnoreRhosts\ no/ /etc/ssh/sshd_config && \
  echo "ssh-client" >> /etc/ssh/shosts.equiv && \
  echo "172.17.0.2" >> /etc/ssh/shosts.equiv && \
  echo "ssh-client,172.17.0.2" >> /etc/ssh/ssh_known_hosts && \
  echo "root:password" | chpasswd && \
  adduser -D -s /bin/bash student && \
  echo "student:password" | chpasswd && \
  echo PS1=\"\\u@\\h:\\W \$ \" >> /home/student/.bashrc && \
  chown -R student:student /home/student && \
  adduser -D -s /bin/bash instructor && \
  echo "instructor:password" | chpasswd && \
  echo PS1=\"\\u@\\h:\\W \$ \" >> /home/instructor/.bashrc && \
  chown -R instructor:instructor /home/instructor && \
  sed -i s/export\ PS1.*// /etc/profile && \
  echo export PS1=\"\\u@\\h:\\W \$ \" >> /etc/profile 