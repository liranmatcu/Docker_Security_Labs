
# Start TLS-VPN server
docker-compose run --name server tls-vpn-server
ipv4_address: 10.0.103.2


# Start TLS-VPN client
docker-compose run --name client --rm tls-vpn-client
ipv4_address: 10.0.103.3


# Other helpful commands
docker network prune
docker container prune


# Notes
Passed an initial test; need to have a comprehensive test.


# docker-compose-yml network related settings
networks:
  lab:
    name: tls-vpn-network
    internal: true # can be false
    driver: bridge
    ipam:
      config:
        - subnet: 10.0.103.0/24