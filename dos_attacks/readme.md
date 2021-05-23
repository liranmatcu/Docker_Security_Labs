git clone https://github.com/liranmatcu/Docker_Security_Labs.git
cd  Docker_Security_Labs/dos_attacks/

# Start all docker instances
docker-compose up -d


# DDoS Blackhole is a real-time distributed denial of service (DDoS) detection and mitigation tool. The software receives a continuous stream of telemetry from standard sFlow agents embedded in network devices, detects distributed denial of service attacks (DDoS), and pushes BGP remote triggered blackhole messages to block the attack upstream.

https://hub.docker.com/r/sflow/ddos-blackhole

docker run -p 6343:6343/udp -p 8008:8008 sflow/ddos-blackhole