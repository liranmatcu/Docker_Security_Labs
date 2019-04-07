#!/bin/bash
while true
do
 #Please use 'man curl' to see what -vk is for, also -X command can be useful too.
 curl -vk web-server
 ping  web-server  -i 0.001 -s 1500
 #sleep 5
done
exit 0
