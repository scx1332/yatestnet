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