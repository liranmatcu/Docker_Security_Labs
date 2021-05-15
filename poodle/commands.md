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