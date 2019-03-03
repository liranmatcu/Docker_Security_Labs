FROM alpine

RUN apk update && apk add bash iputils net-tools && \
  echo "root:password" | chpasswd && \
  adduser -D -s /bin/ash student && \
  passwd -u student && \
  chown -R student:student /home/student && \
  adduser -D -s /bin/ash instructor && \
  passwd -u instructor && \
  chown -R instructor:instructor /home/instructor
