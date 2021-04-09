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
    assert res == {"message": "JOIN", "pos": "0,0"}


def test_leaving():
    data = {"message": "LEAVE", "username": "user-1"}
    sock.sendto(json.dumps(data).encode(), (ADDR, PORT))
    res, _ = sock.recvfrom(1024)
    res = json.loads(res.decode())
    assert res == data
