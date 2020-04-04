FROM alpine:3.10.2

RUN set -x \
    # Install Squid.
 && apk add --no-cache squid \
    # Install dumb-init (to handle PID 1 correctly).
    # https://github.com/Yelp/dumb-init
 && wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.2/dumb-init_1.2.2_amd64 \
 && chmod +x /usr/local/bin/dumb-init

EXPOSE 3128

ENTRYPOINT ["dumb-init"]
CMD ["squid", "-N"]
