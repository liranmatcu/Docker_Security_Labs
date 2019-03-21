FROM alpine

RUN apk update && apk add bash zsh iputils net-tools gcc && \
  echo "root:password" | chpasswd && \
  adduser -D -s /bin/bash student && \
  echo "student:password" | chpasswd && \
  adduser -D -s /bin/bash instructor && \
  echo "instructor:password" | chpasswd && \
  echo PS1=\"\\u@\\h:\\W \$ \" >> /root/.bashrc && \
  echo PS1=\"\\u@\\h:\\W \$ \" >> /home/student/.bashrc && \
  echo PS1=\"\\u@\\h:\\W \$ \" >> /home/instructor/.bashrc && \
  sed -i s/export\ PS1.*// /etc/profile && \
  echo export PS1=\"\\u@\\h:\\W \$ \" >> /etc/profile && \
  chown -R instructor:instructor /home/instructor && \
  chown -R student:student /home/student