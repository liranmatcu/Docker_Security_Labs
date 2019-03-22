FROM alpine

RUN apk add bash iputils net-tools && \
  apk add hping3 --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing && \
  echo PS1=\"\\u@\\h:\\W \$ \" >> /root/.bashrc
 