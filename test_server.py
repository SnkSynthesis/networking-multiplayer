from server.settings import *
import socket
import json


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def test_joining():
    data = {"message": "JOIN", "name": "user-1"}
    sock.sendto(json.dumps(data).encode(), (ADDR, PORT))
    res, addr = sock.recvfrom(1024)
    res = json.loads(res.decode())
    print(f"{res} from {addr}")
    assert data == res
