#!/bin/bash
while true
	do
 		# Use 'man curl' to see what -vk is for.
 		curl -vk web-server
 		# if web-server cannot be resolved to an IP, replace web-server with its IP instead
 		# sleep 5
	done
exit 0
