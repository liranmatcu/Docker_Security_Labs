FROM alpine:3.10.2
WORKDIR /root

ENV PS1="\u@hash: \w $ "

RUN apk update && apk upgrade && \
apk add openssh-client && \
apk add openssl && \
apk add python && \
apk add bash


ADD hash /root/hash