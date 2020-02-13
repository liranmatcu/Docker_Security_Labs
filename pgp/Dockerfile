FROM alpine:3.10.2

# Change environmental variables
ENV PS1="\u@PGP: \w $ "

RUN apk update && apk upgrade && \
apk add gnupg && \
apk add pinentry && \
apk add net-tools && \
apk add tcpdump && \
apk add iputils && \
apk add vim && \
apk add bash
