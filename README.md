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
    "pos": "0,0"
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