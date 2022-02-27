FROM debian:jessie

EXPOSE 22

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -qq update
RUN apt-get -qq install openssh-server
RUN apt-get -qq install krb5-user
RUN apt-get -qq install vim tcpdump
RUN apt-get -qq clean

# configuration for the SSH server
COPY sshd_config /etc/ssh/sshd_config

# configuration for the SSH client
COPY ssh_config /etc/ssh/ssh_config 

# For both
COPY krb5.conf /etc/krb5.conf
COPY hosts /etc/hosts