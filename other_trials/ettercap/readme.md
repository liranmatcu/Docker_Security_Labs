git clone https://github.com/liranmatcu/Docker_Security_Labs.git
cd  Docker_Security_Labs/arp/

https://hub.docker.com/r/mrecco/ettercap
https://github.com/MrEcco/docker-ettercap


# Start all docker instances
docker-compose build
docker-compose up -d


docker run --rm -it           \
      --cap-add SYS_ADMIN     \
      --cap-add NET_ADMIN     \
      eureka-ettercap         \
      -TbqM arp               \
      -oi eth0