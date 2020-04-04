FROM alpine:3.10.2

ENV PS1="\u@web-server: \w $ "

# Updating dependencies, installing Apache
RUN apk update && apk upgrade && \
    apk add iproute2 apache2 tcpdump bash

# Creating placeholder file to be served by apache
RUN mkdir /var/www/html/
RUN touch /var/www/html/index.html
RUN echo "<header><h1>DoS Attack Lab</h1></header>" >> /var/www/html/index.html
RUN echo "<img src="loading.jpg">" >> /var/www/html/index.html
RUN echo "<img src="loading.jpg">" >> /var/www/html/index.html

# We open 80 port, the default one for HTTP for Apache server to listen on
EXPOSE 80

# Simple startup script to avoid some issues observed with container restart 
ADD run-apache.sh /run-apache.sh
RUN chmod -v +x /run-apache.sh

ADD loading.jpg /var/www/html/

CMD ["/run-apache.sh"]