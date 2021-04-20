# Networking Multiplayer
This is a multiplayer game using Python, UDP, and Pygame

* Install dependencies: `pip install -r requirements.txt`
* To run client: `python -m client`
* To run server: `python -m server`


## Server

### Joining

Send:
```json
{
    "message": "JOIN",
    "username": "example-username",
}
```



Expected Response (`pos` is random):
```json
{
    "message": "JOIN", 
    "pos": [0, 0]
}
```

### Updating

Send:
```json
{
    "message": "UPDATE",
    "username": "example-username",
    "pos": [100, 235]
}
```

Expected Response (Should be the data of all the players):
```json
{
    "message": "UPDATE",
    "players": {
        "user-1": {
            "pos": [0, 0],
            "addr": ["127.0.0.1", 60588]
        },
        "user-2": {
            "pos": [0, 100],
            "addr": ["127.0.0.1", 60587],
        },
        "example-username": {
            "pos": [100, 235],
            "addr": ["127.0.0.1", 50587],
        }
    }
}
```


### Leaving

Send:
```json
{
    "message": "LEAVE",
    "username": "example-username"
}
```

Expected Response (Should be same the same as what was sent):
```json
{
    "message": "LEAVE",
    "username": "example-username"
}
```
