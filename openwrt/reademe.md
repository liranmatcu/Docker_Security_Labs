# Source
https://github.com/openwrt/docker
https://hub.docker.com/r/openwrtorg/rootfs
https://openwrt.org/docs/guide-user/virtualization/docker_openwrt_image

# Run our customized OpenWrt image in a Docker container 
docker-compose run --rm openwrt
## Basic image with Docker run 
docker run --rm -it --hostname Eureka openwrtorg/rootfs:x86-64
## with web interface
docker run --rm -it -p 80:80 --hostname Eureka openwrtorg/rootfs:x86-64

# Web interface installation
opkg update
opkg install luci


# To exit from the Docker instance
exit
Crtl+d or Crtl+c