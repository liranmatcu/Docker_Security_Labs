FROM alpine
ENTRYPOINT ["/entrypoint.sh"]
EXPOSE 22
COPY rootfs /

RUN apk add --no-cache openssh && \
  sed -i s/#PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config && \
  echo "root:password" | chpasswd && \
  adduser -D -s /bin/ash student && \
  passwd -u student && \
  chown -R student:student /home/student && \
  adduser -D -s /bin/ash instructor && \
  passwd -u instructor && \
  chown -R instructor:instructor /home/instructor
