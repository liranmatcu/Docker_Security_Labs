FROM alpine:3.10.2

RUN apk add bash iputils net-tools curl && \
  apk add hping3 --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing && \
  echo PS1=\"\\u@\\h:\\W \$ \" >> /root/.bashrc && \
  apk add python3

ADD dos-attacks-curl.sh /dos-attacks-curl.sh
ADD slowloris.py /slowloris.py
RUN chmod +x /dos-attacks-curl.sh
RUN chmod +rw /slowloris.py

# CMD ["/dos-attacks-curl.sh"]
