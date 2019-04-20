FROM ubuntu:12.04
# erwinchang/ubuntu-12.04-32bit-build
# iqmi/ubuntu-12.04-base

RUN apt-get update \
    && apt-get install -y --force-yes --no-install-recommends supervisor \
        gcc zsh sudo vim-tiny wget 

RUN useradd -ms /bin/bash student
USER student
WORKDIR /home/student

ADD ./c_programs  /home/student/

