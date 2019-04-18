FROM debian:jessie-slim

RUN apt-get update && \
  apt-get install -y slowhttptest && \
  rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["slowhttptest"]
CMD ["-h"]