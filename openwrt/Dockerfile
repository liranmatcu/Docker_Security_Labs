FROM openwrtorg/rootfs:x86-64

USER root

EXPOSE 80

RUN mkdir /var/lock && \ 
    opkg update && \
    opkg install luci luci-ssl && \
    opkg install wpad-openssl
