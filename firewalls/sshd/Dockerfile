FROM alpine
ENTRYPOINT ["/entrypoint.sh"]
EXPOSE 22
COPY entrypoint.sh /


RUN apk update && apk add openssh bash && \
  sed -i s/#PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config && \
  echo "root:password" | chpasswd && \
  echo PS1=\"\\u@\\h:\\W \$ \" >> /root/.bashrc 
