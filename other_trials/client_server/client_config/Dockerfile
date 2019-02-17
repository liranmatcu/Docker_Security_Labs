FROM ubuntu

RUN apt-get update && apt-get install -y vim openssl apache2 wget passwd sudo

RUN adduser student

RUN adduser instructor

RUN echo -e "password\npassword" | passwd root
RUN echo -e "password\npassword" | passwd student
RUN echo -e "password\npassword" | passwd instructor

ADD run.sh /run.sh

RUN chmod 777 /run.sh

ENTRYPOINT /run.sh

CMD /run.sh
