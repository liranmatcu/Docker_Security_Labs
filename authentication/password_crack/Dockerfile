FROM fedora

RUN dnf -y install john && \
dnf -y install passwd && \
dnf -y install vim

RUN adduser user1
RUN adduser user2
RUN adduser user3
RUN adduser user4
RUN adduser user5
RUN adduser user6

RUN echo -e "password\npassword" | passwd root
RUN echo -e "Hello\nHello" | passwd user1
RUN echo -e "123\n123" | passwd user2
RUN echo -e "Flower\nFlower" | passwd user3
RUN echo -e "Dragon\nDragon" | passwd user4
RUN echo -e "Hellodragon\nHellodragon" | passwd user5
RUN echo -e "123Hello\n123Hello" | passwd user6
