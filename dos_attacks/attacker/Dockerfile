FROM alpine

RUN apk add bash iputils net-tools curl && \
  apk add hping3 --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing && \
  echo PS1=\"\\u@\\h:\\W \$ \" >> /root/.bashrc

ADD dos-attacks.sh /usr/local/bin/dos-attacks.sh
CMD ["usr/local/bin/dos-attacks.sh"]
 