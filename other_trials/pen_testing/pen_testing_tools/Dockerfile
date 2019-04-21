FROM ubuntu:16.04

# -------------------------------------

RUN apt-get update && \
    apt-get install -y python-pip && \
    apt-get install -y python3 && \
    apt-get install -y sqlmap && \
    apt-get install -y vim && \
    apt-get install -y wget && \
    apt-get install -y curl && \
    apt-get install -y nmap && \
    apt-get install -y nikto && \
    apt-get install -y git && \
    apt-get install -y dnsutils && \
    apt-get install -y iputils-ping && \
    apt-get install -y xprobe2 && \
    apt-get install -y whois

# dnsenum
RUN apt-get install -y build-essential && \
    apt-get install -y cpanminus && \
    git clone https://github.com/fwaeytens/dnsenum.git /home/dnsenum/ && \
    chmod +x /home/dnsenum/dnsenum.pl && \
    ln -s /home/dnsenum/dnsenum.pl /usr/bin/dnsenum && \
    cpanm String::Random && \
    cpanm Net::IP && \
    cpanm Net::DNS && \
    cpanm Net::Netmask && \
    cpanm XML::Writer

# digbit
RUN git clone https://github.com/szalek/digbit.git /home/digbit && \
    chmod +x /home/digbit/src/digbit.sh && \
    chmod +x /home/digbit/src/digbit.py && \
    ln -s /home/digbit/src/digbit.sh /usr/bin/digbit && \
    ln -s /home/digbit/src/digbit.py /usr/bin/digbit.py

# sqliv
RUN git clone https://github.com/Hadesy2k/sqlivulscan.git /home/sqlivulscan && \
    cd /home/sqlivulscan/ && \
    python setup.py -i


# Sn1per
RUN git clone https://github.com/szalek/Sn1per.git /home/Sn1per/ && \
    chmod +x /home/Sn1per/install.sh && \
    cd /home/Sn1per/ && \
    /bin/bash install.sh

# knock
RUN apt-get install -y python-dnspython && \
    cd home && \
    curl -LOk -o knock.tar.gz https://github.com/guelfoweb/knock/archive/4.1.0.tar.gz && \
    mv 4.1.0.tar.gz knock.tar.gz && \
    tar -xzf knock.tar.gz && \
    rm knock.tar.gz && \
    cd knock-4.1.0 && \
    python setup.py install

# webcomment
RUN git clone https://github.com/szalek/webcomment.git /home/webcomment && \
    chmod +x /home/webcomment/webcomment.py && \
    ln -s /home/webcomment/webcomment.py /usr/bin/webcomment


# haveibeenpwned
RUN git clone https://github.com/szalek/haveibeenpwned.git /home/haveibeenpwned && \
    chmod +x /home/haveibeenpwned/haveibeenpwned.sh && \
    ln -s /home/haveibeenpwned/haveibeenpwned.sh /usr/bin/haveibeenpwned

# paskto
RUN apt-get install -y sudo && \
    apt-get install -y curl && \
    apt-get install -y git && \
    curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - && \
    apt-get install -y nodejs && \
    git clone https://github.com/szalek/paskto /home/paskto && \
    chmod +x /home/paskto/paskto.js && \
    /bin/sed -i '1s/^/#!\/usr\/bin\/env node\n/' /home/paskto/paskto.js && \
    ln -s /home/paskto/paskto.js /usr/bin/paskto

# exploit-database
RUN git clone https://github.com/offensive-security/exploit-database.git /opt/exploit-database && \
    ln -sf /opt/exploit-database/searchsploit /usr/local/bin/searchsploit

# Uniscan
RUN cd /home && \
    git clone https://github.com/szalek/Uniscan && \
    cd Uniscan && \
    export PERL_MM_USE_DEFAULT=1 && \
    ./install-modules.sh && \
    chmod +x /home/Uniscan/run.sh && \
    ln -sf /home/Uniscan/run.sh /usr/local/bin/uniscan

# wpscan
RUN apt-get install -y libcurl4-openssl-dev libxml2 libxml2-dev libxslt1-dev ruby-dev build-essential libgmp-dev zlib1g-dev && \
    git clone https://github.com/wpscanteam/wpscan.git && \
    cd wpscan && \
    gem install bundler && bundle install --without test && \
    ln -sf /home/wpscan/wpscan.rb /usr/local/bin/wpscan

# passwords
RUN cd /home && \
    git clone https://github.com/szalek/get_passwords.git && \
    cd /home/get_passwords && \
    chmod +x get_passwords.sh && \
    ln -sf /home/get_passwords/get_passwords.sh /usr/local/bin/get_passwords

# ncrack
RUN apt-get install -y libssl-dev && \
    cd /home && \
    wget -O ncrack.tar.gz https://github.com/nmap/ncrack/archive/v0.6.0.tar.gz && \
    tar -xzf ncrack.tar.gz && \
    cd ncrack-0.6.0 && \
    ./configure && \
    make && \
    make install && \
    cd /home && \
    rm ncrack.tar.gz

# wfuzz
RUN pip install wfuzz && \
    cd /home && \
    git clone https://github.com/xmendez/wfuzz.git

# Sublist3r
RUN cd /home && \
    git clone https://github.com/aboul3la/Sublist3r && \
    cd /home/Sublist3r && \
    pip install -r requirements.txt && \
    ln -sf /home/Sublist3r/sublist3r.py /usr/local/bin/sublist3r

# massdns
RUN cd /home && \
    git clone https://github.com/blechschmidt/massdns.git && \
    cd /home/massdns && \
    make && \
    ln -sf /home/massdns/bin/massdns /usr/local/bin/massdns

# xsssniper
RUN cd /home && \
    apt-get install -y python-pip && \
    pip install mechanize && \
    pip install lxml && \
    git clone https://github.com/gbrindisi/xsssniper.git && \
    cd /home/xsssniper && \
    ln -sf /home/xsssniper/xsssniper.py /usr/local/bin/xsssniper

# arachni
RUN wget https://github.com/Arachni/arachni/releases/download/v1.5.1/arachni-1.5.1-0.5.12-linux-x86_64.tar.gz && \
        tar xzvf arachni-1.5.1-0.5.12-linux-x86_64.tar.gz > /dev/null && \
        mv arachni-1.5.1-0.5.12 /usr/local && \
        ln -s /usr/local/arachni-1.5.1-0.5.12/bin/* /usr/local/bin/