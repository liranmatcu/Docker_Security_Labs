FROM alpine:3.10.2
WORKDIR /root

# Change environmental variables
ENV PS1="\u@\h: \w $ "

RUN apk update && apk upgrade && \
apk add gnupg && \
apk add pinentry && \
apk add bash
