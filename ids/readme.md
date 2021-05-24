
git clone https://github.com/liranmatcu/Docker_Security_Labs.git
cd  Docker_Security_Labs/ids/


# Pentesting agent
docker-compose run --rm pentester bash
## namp scan
nmap snort
## tcpdump capture
tcpdump -i any -vvnn port 80





# Snort
docker-compose build snort
docker-compose run --rm snort bash
snort -T -i eth0 -c /etc/snort/snort.conf

