FROM fedora:20

RUN yum install -y zsh gcc iputils net-tools util-linux-user nmap tcpdump vim wget

RUN useradd student && useradd instructor
RUN chown -R instructor:instructor /home/instructor
RUN chown -R student:student /home/student
RUN echo "student:password" | chpasswd
RUN echo 0 > /proc/sys/kernel/randomize_va_space

ADD ./c_programs  /home/student/

