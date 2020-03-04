FROM alpine

COPY rootfs /root
EXPOSE 23

RUN apk update && apk add python

ENTRYPOINT ["python", "/root/ascii-telnet-server.py"]
CMD ["-f", "/root/sw1.txt"]

