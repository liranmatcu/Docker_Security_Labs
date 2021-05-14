# Start web server
docker-compose run --rm poodle
docker-compose run poodle bash

docker-compose run poodle2 sh

# Launch the attack
python3 parallelization-poodle.py