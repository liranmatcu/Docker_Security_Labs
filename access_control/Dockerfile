from fedora:latest

RUN dnf install -y zsh gcc iputils net-tools && useradd instructor && useradd student && chown -R instructor:instructor /home/instructor && chown -R student:student /home/student
RUN setcap -r /bin/ping && chmod u+s /bin/ping
