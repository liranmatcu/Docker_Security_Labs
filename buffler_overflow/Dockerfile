FROM ubuntu:12.04
# erwinchang/ubuntu-12.04-32bit-build
# iqmi/ubuntu-12.04-base

RUN apt-get update \
    && apt-get install -y --force-yes --no-install-recommends supervisor \
        gcc zsh sudo vim-tiny wget 

RUN adduser student 
RUN chown -R student:student /home/student
RUN echo "student:password" | chpasswd

ADD ./c_programs  /home/student/

