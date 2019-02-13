FROM fedora

RUN dnf -y install openssh-clients && \
dnf -y install wget john && \
dnf -y install passwd && \
dnf -y install sudo && \
dnf -y install vim

RUN adduser student
RUN adduser instructor

RUN echo -e "password\npassword" | passwd root
RUN echo -e "password\npassword" | passwd student
RUN echo -e "password\npassword" | passwd instructor

ENTRYPOINT ["/usr/sbin/init"]
CMD ["/bin/bash"]
