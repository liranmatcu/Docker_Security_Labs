FROM alpine:3.10.2

WORKDIR /root

# Change environmental variables
ENV PS1="\u@\h: \w $ "

RUN apk update && apk upgrade && \
apk add openssl && \
apk add openvpn && \
apk add easy-rsa && \
apk add net-tools && \
apk add tcpdump && \
apk add iputils && \
apk add vim && \
apk add openrc && \
apk add bash

COPY hosts /etc/
# copy all the certs and the conf file
COPY *.* /etc/openvpn/
# COPY client.conf /etc/openvpn/