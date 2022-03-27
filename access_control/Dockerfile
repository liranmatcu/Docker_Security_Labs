FROM alpine:3.10.2
CMD ["/bin/bash"]

RUN apk update && apk add bash shadow acl zsh iputils net-tools gcc vim which && \
  echo "root:password" | chpasswd && \
  adduser -D -s /bin/bash student && \
  echo "student:password" | chpasswd && \
  adduser -D -s /bin/bash instructor && \
  echo "instructor:password" | chpasswd && \
  echo 'export PS1="\u@access-control: \W $ "' >> /root/.bashrc && \
  echo 'export PS1="\u@access-control: \W $ "' >> /home/student/.profile && \
  echo 'umask 002' >> /home/student/.profile && \
  echo 'umask 002' >> /home/student/.bashrc && \
  echo 'export PS1="\u@access-control: \W $ "' >> /home/instructor/.profile && \
  echo 'umask 002' >> /home/instructor/.profile && \
  echo PS1=\"zsh-%n@access-control: %/ $\" >> /root/.zshenv && \
  echo PS1=\"zsh-%n@access-control: %/ $\" >> /home/student/.zshenv && \
  echo PS1=\"zsh-%n@access-control: %/ $\" >> /home/instructor/.zshenv && \
  echo "alias ll='ls -al'" >> /root/.bashrc && \
  echo "alias c='clear'" >> /root/.bashrc && \
  echo "alias ll='ls -al'" >> /home/student/.profile && \
  echo "alias c='clear'" >> /home/student/.profile && \
  echo "alias ll='ls -al'" >> /home/instructor/.profile && \
  echo "alias c='clear'" >> /home/instructor/.profile && \
  sed -i s/export\ PS1.*// /etc/profile && \
  echo export PS1=\"\\u@\\h:\\W \$ \" >> /etc/profile && \
  chown -R instructor:instructor /home/instructor && \
  chown -R student:student /home/student
