FROM fedora

RUN dnf -y install openssh-server openssh-clients && \
dnf -y install openssl-* && \
dnf -y install httpd-* && \
dnf -y install mod_ssl && \
dnf -y install python python3 && \
dnf -y install wget && \
dnf -y install passwd && \
dnf -y install sudo && \
dnf -y install vim

RUN adduser student

RUN adduser instructor

RUN echo -e "password\npassword" | passwd root
RUN echo -e "password\npassword" | passwd student
RUN echo -e "password\npassword" | passwd instructor

RUN gpasswd wheel -a student
RUN gpasswd wheel -a instructor

ENTRYPOINT ["/usr/sbin/init"]
CMD ["/bin/bash"]
