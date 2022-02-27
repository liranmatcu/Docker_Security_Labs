# KDC Server Container
This container is a simplified version of [docker-kerberos](https://github.com/ist-dsi/docker-kerberos), it provides a standalone KDC server in a docker container, exposing default KDC ports: `749 TCP` and `88 UDP`. The default realm is `EXAMPLE.COM`. Additionally, a default KDC admin principal `kadmin/admin@EXAMPLE.COM` and a no permissions principal are setup `noPermissions@EXAMPLE.COM`, these may be used for KDC functionality testing such as `kadmin` commands. For a more admin client-server focused scenario, see [this docker kerberos project](https://github.com/ist-dsi/docker-kerberos).

## Starting
docker-compose up kdc-server

## Usage
Once the container started, switch into the container 
docker exec -it kdc-server bash

Use `kadmin.local` for the KDC amdmin interafce. From there you can start adding principals and keytabs. 

