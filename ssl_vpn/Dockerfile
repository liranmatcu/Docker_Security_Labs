FROM alpine:3.10.2

WORKDIR /root

# Change environmental variables
ENV PS1="\u@\h: \w $ "

RUN apk update && apk upgrade && \
apk add openssh-server && \
apk add openssh-client && \
apk add openssl && \
apk add openvpn && \
apk add easy-rsa && \
apk add net-tools && \
apk add tcpdump && \
apk add iputils && \
apk add vim && \
apk add openrc && \
apk add bash
