FROM alpine:3.10.2

# Change environmental variables
ENV PS1="\u@\h: \w $ "

RUN apk update && apk upgrade && \
apk add ipsec-tools && \
apk add openssl && \
apk add net-tools && \
apk add tcpdump && \
apk add iputils && \
apk add vim && \
apk add openrc && \
apk add bash

COPY *.conf  /etc
COPY p1_up_down  /etc
COPY psk.txt /etc
RUN chmod 600 /etc/psk.txt