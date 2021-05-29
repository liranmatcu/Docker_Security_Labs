# Source
https://github.com/openwrt/docker
https://hub.docker.com/r/openwrtorg/rootfs
https://openwrt.org/docs/guide-user/virtualization/docker_openwrt_image

# Run our customized OpenWrt image in a Docker container 
docker-compose build
docker run --rm -it -p 80:80 --hostname Eureka eureka-openwrt
## docker-compose run --rm openwrt 
## ssh would work, but not http; not 0.0.0.0:80->80/tcp

# Run basic OpenWrt image via Docker run with web interface
docker run --rm -it -p 80:80 --hostname Eureka openwrtorg/rootfs:x86-64
## Web interface installation
opkg update
opkg install luci
## WPA3 installation
opkg install wpad-openssl
## After this step, it is equivalent to docker-compose run


# To exit from the Docker instance
halt

exit
Crtl+d or Crtl+c