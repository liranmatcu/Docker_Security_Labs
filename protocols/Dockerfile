FROM alpine:3.10.2

# Change environmental variables
ENV PS1="\u@protocols: \w $ "

RUN apk update && apk upgrade && \
apk add gnupg && \
apk add pinentry && \
apk add openssh-server && \
apk add openssh-client && \
apk add ipsec-tools && \
apk add openssl && \
apk add openvpn && \
apk add easy-rsa && \
apk add net-tools && \
apk add tcpdump && \
apk add iputils && \
apk add vim && \
apk add vsftpd && \
apk add openrc && \
apk add bash
