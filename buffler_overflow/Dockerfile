FROM fedora:latest

RUN dnf install -y zsh gcc iputils net-tools util-linux-user nmap vim

RUN useradd student && useradd instructor
RUN chown -R instructor:instructor /home/instructor
RUN chown -R student:student /home/student
RUN echo "student:password" | chpasswd

ADD ./c_prorgams  /home/student/

