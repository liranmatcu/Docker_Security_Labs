FROM alpine
RUN apk --no-cache add openssh-client openssh openssh-keysign bash && \
  sed -i s/#\ \ \ HostbasedAuthentication.*/HostbasedAuthentication\ yes/ /etc/ssh/ssh_config && \
  sed -i "/HostbasedAuthentication.*/a EnableSSHKeysign yes" /etc/ssh/ssh_config && \
  echo "root:password" | chpasswd && \
  adduser -D -s /bin/bash student && \
  passwd -u student && \
  adduser -D -s /bin/bash instructor && \
  passwd -u instructor && \
  echo PS1=\"\\u@\\h:\\W \$ \" >> /root/.bashrc && \
  echo PS1=\"\\u@\\h:\\W \$ \" >> /home/student/.bashrc && \
  echo PS1=\"\\u@\\h:\\W \$ \" >> /home/instructor/.bashrc && \
  sed -i s/export\ PS1.*// /etc/profile && \
  echo export PS1=\"\\u@\\h:\\W \$ \" >> /etc/profile && \
  chown -R instructor:instructor /home/instructor && \
  chown -R student:student /home/student && \
  ssh-keygen -A
