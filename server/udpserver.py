import socket


class UDPServer:

    def __init__(self, address, port):
        self.address = address
        self.port = port
    
    def start(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((self.address, self.port))


            




