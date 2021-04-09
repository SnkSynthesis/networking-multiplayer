from .settings import *
import socket
import json


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ADDRESS, PORT))

print(f"Started server on {ADDRESS}:{PORT}")

while True:
    raw_data, address = sock.recvfrom(1024)
    data = json.loads(raw_data.decode())
    print(f"{data} from {address}")
    sock.sendto(raw_data, address)
