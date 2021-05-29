FROM openwrtorg/rootfs:x86-64

USER root

RUN echo "nameserver 8.8.8.8" | tee -a /etc/resolv.conf

RUN opkg update 

RUN opkg install luci luci-ssl && \
    opkg install wpad-openssl
