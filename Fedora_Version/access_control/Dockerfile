FROM fedora:latest

RUN dnf install -y passwd zsh gcc iputils net-tools util-linux-user sudo procps

RUN useradd student && useradd instructor
RUN chown -R instructor:instructor /home/instructor
RUN chown -R student:student /home/student
RUN echo "student:password" | chpasswd
# RUN echo "instructor:password" | chpasswd
RUN echo "password" | passwd --stdin instructor
# RUN echo -e "password\npassword" | passwd instructor

RUN setcap -r /bin/ping && chmod u+s /bin/ping
