FROM alpine:3.10.2
CMD ["/bin/bash"]
COPY ./dict_files/password-2011.lst /usr/share/john/password.lst

# Add dependencies
RUN apk update && apk upgrade && \
apk add john && \
apk add wget && \
apk add vim && \
apk add bash && \
apk add findutils

# Add users and changes their passwords
RUN echo "root:password" | chpasswd && \
adduser -D -s /bin/bash user1 && \
echo -e "user1:Hello" | chpasswd && \
adduser -D -s /bin/bash user2 && \
echo -e "user2:123" | chpasswd && \
adduser -D -s /bin/bash user3 && \
echo -e "user3:Flower" | chpasswd && \
adduser -D -s /bin/bash user4 && \
echo -e "user4:Dragon" | chpasswd && \
adduser -D -s /bin/bash user5 && \
echo -e "user5:Hellodragon" | chpasswd && \
adduser -D -s /bin/bash user6 && \
echo -e "user6:123Hello" | chpasswd

# Set PS1 variable
RUN echo 'export PS1="\u@password-crack: \W $ "' >> /root/.bashrc && \
  echo 'export PS1="\u@password-crack: \W $ "' >> /home/user1/.bash_profile && \
  echo 'export PS1="\u@password-crack: \W $ "' >> /home/user2/.bash_profile && \
  echo 'export PS1="\u@password-crack: \W $ "' >> /home/user3/.bash_profile && \
  echo 'export PS1="\u@password-crack: \W $ "' >> /home/user4/.bash_profile && \
  echo 'export PS1="\u@password-crack: \W $ "' >> /home/user5/.bash_profile && \
  echo 'export PS1="\u@password-crack: \W $ "' >> /home/user6/.bash_profile

RUN ln -s /usr/share/john/ john && \
    cp /etc/john/john.conf john.conf
