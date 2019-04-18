FROM alpine

RUN apk update && \
  apk add --no-cache snort bash && \
  rm -f /tmp/* /etc/apk/cache/*

ENTRYPOINT ["snort"]
CMD ["--help"]
 
