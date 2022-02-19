
# Start IPsec-VPN server
docker-compose run --name server --rm ipsec-server
ipv4_address: 10.0.103.2
  ## Start IPsec VPN service on server container
  setkey -f /etc/setkey.conf
  racoon -Fd

# Start IPsec-VPN client
docker-compose run --name client --rm ipsec-client
ipv4_address: 10.0.103.3
  ## Start IPsec VPN service on client container
  setkey -f /etc/setkey.conf
  racoon -Fd


# Other helpful commands
docker network prune
docker container prune


# Notes
All the configurations have been updated to match the 10.0.103.0/24 subnet, and IP addresses of server and client.
Still having issues when the server and the client are trying to negotiate Security Associations.


# docker-compose.yml network related settings
networks:
  lab:
    name: ipc-vpn-network
    internal: true
    driver: bridge
    ipam:
      config:
        - subnet: 10.0.103.0/24