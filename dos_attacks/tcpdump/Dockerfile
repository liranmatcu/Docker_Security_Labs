FROM alpine:3.10.2

# COPY .bashrc /root/.bashrc

RUN apk --no-cache --update --verbose add grep bash tcpdump && \
    rm -rf /var/cache/apk/* /tmp/* /sbin/halt /sbin/poweroff /sbin/reboot

ENTRYPOINT ["/usr/sbin/tcpdump"]