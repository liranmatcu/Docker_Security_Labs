FROM alpine

RUN apk add bash iputils net-tools curl && \
  apk add hping3 --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing && \
  echo PS1=\"\\u@\\h:\\W \$ \" >> /root/.bashrc

ADD dos-attacks-curl.sh /dos-attacks-curl.sh
ADD dos-attacks-ping.sh /dos-attacks-ping.sh

# CMD ["/dos-attacks-curl.sh"]
 