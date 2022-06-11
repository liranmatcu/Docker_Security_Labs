
# GitHub repository
https://github.com/ethereum/go-ethereum


# Docker hub repository
https://hub.docker.com/r/ethereum/client-go/


# Start ethereum client
Ref: https://geth.ethereum.org/docs/install-and-build/installing-geth
docker pull ethereum/client-go
docker run -it -p 30303:30303 ethereum/client-go

## The image has the following ports automatically exposed:
8545 TCP, used by the HTTP based JSON RPC API
8546 TCP, used by the WebSocket based JSON RPC API
8547 TCP, used by the GraphQL API
30303 TCP and UDP, used by the P2P protocol running the network

## Volumes
Note, if you are running an Ethereum client inside a Docker container, you should mount a data volume as the client’s data directory (located at /root/.ethereum inside the container) to ensure that downloaded data is preserved between restarts and/or container life-cycles.

## Docker quick start
docker run -d --name ethereum-node -v "$PWD"/alice/ethereum:/root \
           -p 8545:8545 -p 30303:30303 \
           ethereum/client-go
### or
docker run -d --name ethereum-node -v "$PWD"/bob/ethereum:/root \
           -p 8545:8545 -p 30303:30303 \
           ethereum/client-go:stable
### This will start geth in fast-sync mode with a DB memory allowance of 1GB just as the above command does. It will also create a persistent volume in your home directory for saving your blockchain as well as map the default ports.

docker exec -it ethereum-node geth attach

The geth JavaScript console is started with the console or attach geth sub-commands. The console subcommands starts the geth node and then opens the console. The attach subcommand attaches to the console to an already-running geth instance.

# Using Geth
## common scenario is people wanting to simply interact with the Ethereum network: create accounts; transfer funds; deploy and interact with contracts. For this particular use-case the user doesn't care about years-old historical data, so we can fast-sync quickly to the current state of the network. To do so:
geth console

          