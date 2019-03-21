FROM alpine
RUN apk update && apk add openssh-client openssh bash && \
  echo "root:password" | chpasswd && \
  adduser -D -s /bin/bash student && \
  passwd -u student && \
  adduser -D -s /bin/bash instructor && \
  passwd -u instructor && \
  echo PS1=\"\\u@\\h:\\W \$ \" >> /root/.bashrc && \
  echo PS1=\"\\u@\\h:\\W \$ \" >> /home/student/.bashrc && \
  echo PS1=\"\\u@\\h:\\W \$ \" >> /home/instructor/.bashrc && \
  chown -R instructor:instructor /home/instructor && \
  chown -R student:student /home/student
