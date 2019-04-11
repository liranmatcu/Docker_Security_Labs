FROM fedora

# Updating dependencies, installing Apache and cleaning dnf caches to reduce container size
RUN dnf -y update && dnf -y install httpd iptables iptables-services && dnf clean all

# Creating placeholder file to be served by apache
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