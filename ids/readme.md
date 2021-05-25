
git clone https://github.com/liranmatcu/Docker_Security_Labs.git
cd  Docker_Security_Labs/ids/


# Pentesting agent
docker-compose run --rm pentester bash
## namp scan
nmap snort
## tcpdump capture
tcpdump -i any -vvnn port 80

ping snort (ping rule would alert)



# Snort
docker-compose build snort
docker-compose run --rm snort bash
## Testing configuration
snort -T -i eth0 -c /etc/snort/snort.conf
## Run snort
snort -i eth0 -c /etc/snort/snort.conf

snort -i eth0 -c /etc/snort/snort.conf -A console

### Add more rules in Step 7 and the /rules folder

Ref:
https://github.com/John-Lin/docker-snort
https://hub.docker.com/r/linton/docker-snort/