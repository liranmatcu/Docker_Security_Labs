# Start Aircrack-ng
docker-compose run aircrack bash
docker-compose run --rm aircrack bash


# WEP key in hex is
69:6e:6a:65:63:74:69:6f:6e:66:61:73:74

# Crack WPA-PSK key
aircrack-ng -a 2 -w ./WPA/password-file.txt ./WPA/4-way-handshake.pcap

# Cannot access Mac's wireless NIC yet