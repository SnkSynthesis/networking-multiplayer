from server.settings import *
import socket
import json


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1)


def test_joining():
    data = {"message": "JOIN", "username": "user-1"}
    sock.sendto(json.dumps(data).encode(), (ADDR, PORT))
    res, _ = sock.recvfrom(1024)
    res = json.loads(res.decode())
    assert res["message"] == "JOIN"
    assert len(res["pos"].split(",")) == 2


def test_leaving():
    data = {"message": "LEAVE", "username": "user-1"}
    sock.sendto(json.dumps(data).encode(), (ADDR, PORT))
    res, _ = sock.recvfrom(1024)
    res = json.loads(res.decode())
    assert res == data

def test_moving():
    data = {"message": "UPDATE", "username": "user-1", "pos": [0, 0]}
    sock.sendto(json.dumps(data).encode(), (ADDR, PORT))
    res, _ = sock.recvfrom(1024)
    res = json.loads(res.decode())
    assert res["message"] == "UPDATE"
    assert len(res["players"]) != 0
    for player in res["players"]:
        assert player.get("pos") is not None
        assert isinstance(player["pos"], list)
        assert isinstance(player["pos"][0], int)
        assert isinstance(player["pos"][1], int)
        assert len(player["pos"]) == 2
