FROM ubuntu

ADD . /tmp

RUN apt-get update -y && apt-get install -y python3.6 python3-pip vim && \ 
pip3 install flask && \
pip3 install pyOpenSSL

