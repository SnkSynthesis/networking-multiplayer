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
    assert len(res["pos"]) == 2
    for item in res["pos"]:
        assert isinstance(item, int)
    assert res.get("color") is not None
    assert len(res["color"]) == 3
    for item in res["color"]:
        assert isinstance(item, int)


def test_moving():
    data = {"message": "UPDATE", "username": "user-1", "pos": [0, 0]}
    sock.sendto(json.dumps(data).encode(), (ADDR, PORT))
    res, _ = sock.recvfrom(1024)
    res = json.loads(res.decode())
    assert res["message"] == "UPDATE"
    assert len(res["players"]) != 0
    for player in res["players"].values():
        assert player.get("pos") is not None
        assert player.get("addr") is not None
        assert len(player["pos"]) == 2
        assert len(player["color"]) == 3
        for item in player["color"]:
            assert isinstance(item, int)


def test_leaving():
    data = {"message": "LEAVE", "username": "user-1"}
    sock.sendto(json.dumps(data).encode(), (ADDR, PORT))
    res, _ = sock.recvfrom(1024)
    res = json.loads(res.decode())
    assert res == data
