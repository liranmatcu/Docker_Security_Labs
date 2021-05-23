
# GitHub Repo 
https://github.com/ethereum/go-ethereum

# Docker hub
https://hub.docker.com/r/ethereum/client-go/

https://geth.ethereum.org/docs/install-and-build/installing-geth
docker pull ethereum/client-go
docker run -it -p 30303:30303 ethereum/client-go

The image has the following ports automatically exposed:

8545 TCP, used by the HTTP based JSON RPC API
8546 TCP, used by the WebSocket based JSON RPC API
8547 TCP, used by the GraphQL API
30303 TCP and UDP, used by the P2P protocol running the network

# Docker quick start

docker run -d --name ethereum-node -v "$PWD"/alice/ethereum:/root \
           -p 8545:8545 -p 30303:30303 \
           ethereum/client-go


          