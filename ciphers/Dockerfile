FROM alpine:3.10.2
WORKDIR /root

ENV PS1="\u@ciphers: \w $ "

RUN apk update && apk upgrade && \
apk add openssh-server && \
apk add openssh-client && \
apk add openssl && \
apk add python python3 && \
apk add wget && \
apk add vim && \
apk add perl && \
apk add bash && \
apk add curl


ADD feistel /root/feistel
ADD wiki /root/wiki
ADD rsa /root/rsa
ADD ecb /root/ecb
ADD rc4 /root/rc4