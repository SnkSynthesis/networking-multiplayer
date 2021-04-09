from server.settings import *
import socket
import json


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def test_sending_join():
    data = {"message": "JOIN", "name": "user-1"}
    sock.sendto(json.dumps(data).encode(), (ADDRESS, PORT))
    res, address = sock.recvfrom(1024)
    res = json.loads(res.decode())
    print(f"{res} from {address}")
    assert data == res
