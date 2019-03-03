FROM alpine

RUN apk update && apk add bash iputils net-tools && \
  echo "root:password" | chpasswd && \
  adduser -D -s /bin/ash student && \
  passwd -u student && \
  chown -R student:student /home/student && \
  adduser -D -s /bin/ash instructor && \
  passwd -u instructor && \
  chown -R instructor:instructor /home/instructor && \
  echo PS1=\"\\u@\\h:\\W \$ \" >> /root/.bashrc && \
  echo PS1=\"\\u@\\h:\\W \$ \" >> /home/student/.bashrc && \
  echo PS1=\"\\u@\\h:\\W \$ \" >> /home/instructor/.bashrc 
