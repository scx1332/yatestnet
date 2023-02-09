# yatestnet
Testnet chain for Golem Network


## How to run

* Generate main account and signer key

```
pip install web3
python gen_env.py > .env
```

* Make sure genesis folder is empty or nonexistent

```
docker-compose up
```

Genesis folder should now contain chaindata and files

```
chain987789
genesis987789.json
password987789.json
```

987789 is selected chain id
genesis987789.json can be used to spawn additional node of the same chain.
password987789.json is used to unlock signer on main node.
chain987789 contains local node chain data.

## Setup gas scanner

Clone yablockscout repo 
https://github.com/scx1332/yablockscout

go to docker-compose directory and run docker-compose build
docker-compose run -d

## Setup gas fixer

Gas fixer is needed to generate non zero gas prices on the network that has almost no transactions.
https://github.com/scx1332/blockchain_price_fixer.git




