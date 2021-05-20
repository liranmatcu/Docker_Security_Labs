FROM alpine:3.12
WORKDIR /opt

# Change environmental variables
ENV PS1="\u@\h: \w $ "

RUN apk update && apk upgrade && \
apk add aircrack-ng pciutils && \
apk add bash
