FROM alpine:3.6
ENTRYPOINT ["/entrypoint.sh"]
EXPOSE 22
COPY rootfs /

RUN apk add --no-cache openssh bash && \
  sed -i s/#PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config && \
  sed -i s/#HostbasedAuthentication.*/HostbasedAuthentication\ yes/ /etc/ssh/sshd_config && \
  sed -i s/#IgnoreRhosts.*/IgnoreRhosts\ no/ /etc/ssh/sshd_config && \
  echo "root:password" | chpasswd && \
  adduser -D -s /bin/ash student && \
  echo "student:password" | chpasswd && \
  chown -R student:student /home/student && \
  adduser -D -s /bin/ash instructor && \
  echo "instructor:password" | chpasswd && \
  chown -R instructor:instructor /home/instructor