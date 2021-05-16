FROM nginx:1.10.2

RUN useradd eureka 
ADD ./code /tmp
RUN chmod 0404 /tmp/root-data-file 

WORKDIR /tmp

USER root
CMD ["nginx", "-g", "daemon off;"]



