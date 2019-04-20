FROM centos:6

ENV version 9.4.3

RUN yum -y update
RUN yum -y groupinstall "Development Tools"
RUN yum -y install kernel-devel kernel-headers
RUN yum -y install openssl-devel perl-Net-DNS wget bind-utils vim tar

RUN cd /usr/local/src && \
    wget ftp://ftp.isc.org/isc/bind9/${version}/bind-${version}.tar.gz && \
    tar zxvf bind-${version}.tar.gz && \
    mv bind-${version} bind
RUN cd /usr/local/src/bind && \
    ./configure --enable-syscalls --prefix=/var/named/chroot --enable-threads --with-openssl=yes --enable-openssl-version-check --enable-ipv6 --disable-linux-caps && \
    chown -R root:root /usr/local/src/bind && \
    make && \
    make install
RUN groupadd -g 25 bind && \
    useradd -u 25 -g bind -d /var/named -c "DNS BIND Named User" -s /sbin/nologin bind
RUN mkdir /var/named/chroot/dev && \
    mknod -m 666 /var/named/chroot/dev/null c 1 3 && \
    mknod -m 666 /var/named/chroot/dev/random c 1 8
RUN /var/named/chroot/sbin/rndc-confgen -a
RUN mkdir /var/named/chroot/data && \
    mkdir /var/named/chroot/var/log && \
    mkdir /var/named/chroot/var/run/named

ADD ./conf/named.conf /var/named/chroot/etc/named.conf
ADD ./conf/cache.db /var/named/chroot/etc/cache.db
RUN ln -s /var/named/chroot/etc/rndc.key /etc/rndc.key && \
    ln -s /var/named/chroot/etc/named.conf /etc/named.conf && \
    ln -s /var/named/chroot/etc/cache.db /etc/cache.db
ADD ./conf/named /etc/sysconfig/named

CMD ["/var/named/chroot/sbin/named", "-g", "-t", "/var/named/chroot", "-c", "/etc/named.conf"]