FROM fedora

RUN yum install -y zsh gcc libtool glibc-devel iputils net-tools util-linux-user nmap tcpdump vim wget

RUN useradd student && useradd instructor
RUN chown -R instructor:instructor /home/instructor
RUN chown -R student:student /home/student
RUN echo "student:password" | chpasswd

ADD ./c_programs  /home/student/

