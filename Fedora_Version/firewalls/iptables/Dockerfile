#
# Dockerfile for iptables
#

FROM alpine

RUN apk update && apk add iproute2 openssh-client curl nmap bash && \
    echo PS1=\"\\u@\\h:\\W \$ \" >> /root/.bashrc && \
    ln -s /usr/lib/tc /lib/tc
# iproute2 includes iptables
# echo "root:password" | chpasswd && \

ENV LIMIT_PORT 8388
ENV LIMIT_CONN 5
ENV TCP_PORTS 22,80
ENV UDP_PORTS 53
ENV RATE 1mbit
ENV BURST 1kb
ENV LATENCY 50ms
ENV INTERVAL 60

CMD iptables -F \
    && iptables -A INPUT -p tcp -m state --state NEW --dport $LIMIT_PORT -m connlimit --connlimit-above $LIMIT_CONN -j DROP \
    && iptables -A OUTPUT -p tcp -m state --state NEW -m multiport --dports $TCP_PORTS -j DROP \
    && iptables -A OUTPUT -p icmp --icmp-type 8 -j DROP \
    && tc qdisc add dev eth0 root tbf rate $RATE burst $BURST latency $LATENCY \
    && watch -n $INTERVAL tc -s qdisc ls dev eth0 

# && iptables -A OUTPUT -p udp -m state --state NEW -m multiport ! --dports $UDP_PORTS -j DROP \
# ifconfig eth0 mtu 900
