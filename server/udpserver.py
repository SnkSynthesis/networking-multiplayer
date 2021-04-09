import socket
import socket
import json


class UDPServer:
    def __init__(self, addr, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((addr, port))
        self.addr = addr
        self.port = port

    def start(self):
        print(f"Started server on {self.addr}:{self.port}")
        while True:
            raw_data, addr = self.sock.recvfrom(1024)
            data = json.loads(raw_data.decode())
            print(f"{data} from {addr}")
            self.sock.sendto(raw_data, addr)
