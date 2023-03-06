# Reference
https://medium.com/scb-digital/running-a-private-ethereum-blockchain-using-docker-589c8e6a4fe8

Check the connectivity of the nodes:
curl --location --request POST 'localhost:8545' \
--header 'Content-Type: application/json' \
--data-raw '{
   "jsonrpc": "2.0",
   "id": 1,
   "method": "admin_peers",
   "params": []
}'


# GitHub repository
https://github.com/ethereum/go-ethereum


# Docker hub repository
https://hub.docker.com/r/ethereum/client-go/


# Start Ethereum client
Ref: https://geth.ethereum.org/docs/install-and-build/installing-geth
docker pull ethereum/client-go
docker run -it -p 30303:30303 ethereum/client-go

## The image has the following ports automatically exposed:
8545 TCP, used by the HTTP based JSON RPC API
8546 TCP, used by the WebSocket based JSON RPC API
8547 TCP, used by the GraphQL API
30303 TCP and UDP, used by the P2P protocol running the network

# Using Geth
## common scenario is people wanting to simply interact with the Ethereum network: create accounts; transfer funds; deploy and interact with contracts. For this particular use-case the user doesn't care about years-old historical data, so we can fast-sync quickly to the current state of the network. To do so:
geth console

          