# KDC Server Container
This container is a simplified version of [docker-kerberos](https://github.com/ist-dsi/docker-kerberos), it provides a standalone KDC server in a docker container, exposing default KDC ports: `749 TCP` and `88 UDP`. The default realm is `EXAMPLE.COM`. Additionally, a default KDC admin principal `kadmin/admin@EXAMPLE.COM` and a no permissions principal are setup `noPermissions@EXAMPLE.COM`, these may be used for KDC functionality testing such as `kadmin` commands. For a more admin client-server focused scenario, see [this docker kerberos project](https://github.com/ist-dsi/docker-kerberos).
https://www.confluent.io/blog/containerized-testing-with-kerberos-and-ssh/

## Starting
docker-compose up kdc-server

## Usage
Once the container started, switch into the container 
docker exec -it kdc-server bash

Use `kadmin.local` for the KDC amdmin interafce. From there you can start adding principals and keytabs. 

kadmin.local:  listprincs
K/M@EUREKA.LABS
kadmin/admin@EUREKA.LABS
kadmin/changepw@EUREKA.LABS
kadmin/kdc-server@EUREKA.LABS
krbtgt/EUREKA.LABS@EUREKA.LABS
noPermissions@EUREKA.LABS

addprinc -randkey host/ssh-server@EUREKA.LABS
ktadd -k /sshserver.keytab host/ssh-server@EUREKA.LABS

addprinc -randkey student
or
addprinc student


Once the service and user principals are created, copy the keytab file(s) from the KDC container to your local machine. The sshserver.keytab will need to be copied to the SSH server, and if you are using the keytab Method 1 above, the sshuser.keytab to the SSH client.
docker cp kdc-server:/ssh-server.keytab ./ssh-server.keytab
docker cp kdc-server:/student.keytab ./student.keytab



docker cp ./ssh-server.keytab ssh-server:/etc/krb5.keytab



docker cp ./student.keytab ssh-client:/student.keytab
kinit student -k -t student.keytab

klist

[libdefaults]
    default_realm = EUREKA.LABS
    forwardable = TRUE

[realms]
        EUREKA.LABS = {
                kdc_ports = 88,750
                kadmind_port = 749
                kdc = kdc-server
                admin_server = kdc-server
        }
        
[domain_realm]
        host.docker.internal = EUREKA.LABS



