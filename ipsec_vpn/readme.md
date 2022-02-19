
# Start IPsec-VPN server
docker-compose run --name server --rm ipsec-server
ipv4_address: 10.0.103.2


# Start IPsec-VPN client
docker-compose run --name client --rm ipsec-client
ipv4_address: 10.0.103.3


# Other helpful commands
docker network prune
docker container prune


# Notes
Still having issues when the server and the client are negotiating Security Associations.


# docker-compose.yml network related settings
networks:
  lab:
    name: ipc-vpn-network
    internal: true
    driver: bridge
    ipam:
      config:
        - subnet: 10.0.103.0/24