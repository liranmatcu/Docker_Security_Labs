FROM alpine:3.10.3 as builder

ARG GIT_ETTERCAP=https://github.com/Ettercap/ettercap.git

# Prepare building
WORKDIR /root
RUN apk add --no-cache --update             \
         git                                \
         libc-dev                           \
         make                               \
         gcc                                \
         bash                               \
         flex                               \
         bison                              \
         cmake                              \
         patch                              \
   && git clone ${GIT_ETTERCAP} ./ettercap

# Prepare deps and it devel
RUN apk add --no-cache --update             \
         libpcap-dev                        \
         libnet-dev                         \
         openssl-dev                        \
         zlib-dev                           \
         geoip-dev                          \
         pcre-dev                           \
         ncurses-dev                        \
         curl-dev                           \
         alpine-sdk                         \
         libpthread-stubs                   \
         iptables-dev                       \
         libltdl

# Configure buildment
WORKDIR /root/ettercap
RUN mkdir -p build              \
   && cd build                  \
   && cmake -DENABLE_GTK=OFF ..

# Bug fixes
COPY ./patch /patch
RUN cat /patch | patch -p0 /root/ettercap/src/interfaces/curses/widgets/wdg.h

# Build
WORKDIR /root/ettercap/build
RUN make && make install

# Collect it
RUN mkdir -p                                \
         /output/usr/local/bin              \
         /output/usr/local/lib              \
         /output/etc                        \
         /output/usr/local/share/ettercap   \
   && cp -r                                 \
         /usr/local/bin/etter*              \
         /output/usr/local/bin/             \
   && cp -r                                 \
         /usr/local/lib/libetter*           \
         /usr/local/lib/etter*              \
         /output/usr/local/lib/             \
   && cp -r                                 \
         /etc/ettercap*                     \
         /output/etc/                       \
   && cp -r                                 \
         /usr/local/share/ettercap/*        \
         /output/usr/local/share/ettercap/

FROM alpine:3.10.3

COPY --from=builder /output /

# Install deps
RUN apk add --update                        \
         libpcap                            \
         libnet                             \
         openssl                            \
         zlib                               \
         geoip                              \
         libltdl                            \
         pcre                               \
         ncurses                            \
         libpthread-stubs                   \
         iptables                           \
         curl                               \
         bash                               \
   && rm -rf /var/cache/apk/*

ENTRYPOINT ["/usr/local/bin/ettercap"]

# CMD ["ettercap", "-TbqM", "arp" "-i" "ens32"]
# ettercap -TbqM arp -i ens32