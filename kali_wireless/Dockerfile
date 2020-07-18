FROM kalilinux/kali-rolling
# FROM kalilinux/kali

WORKDIR /root


# Update
RUN apt-get -y update && apt-get -y dist-upgrade && apt-get -y autoremove && apt-get clean



# Install aircrack and some useful hardware packages
RUN apt-get -y install aircrack-ng pciutils usbutils net-tools kmod




# Install Kali Linux "Top 10" metapackage and a few useful tools
# RUN apt-get -y install vim kali-linux-top10 net-tools whois netcat exploitdb man-db dirb nikto wpscan 
# uniscan nodejs npm python3-pip 

