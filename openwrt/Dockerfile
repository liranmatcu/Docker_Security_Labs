FROM openwrtorg/rootfs:x86-64

USER root

EXPOSE 80

RUN mkdir /var/lock && \ 
    opkg update && \
    opkg install luci luci-ssl && \
    opkg install wpad-openssl

# using exec format so that /sbin/init is proc 1 (see procd docs)
CMD ["/sbin/init"]