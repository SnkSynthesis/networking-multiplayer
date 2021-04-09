import socket
import json
import select
import logging
import random
from .settings import LOGGING_LEVEL
import sys


logging.basicConfig(format="[SERVER] %(levelname)s: %(message)s", level=LOGGING_LEVEL)


class UDPServer:
    def __init__(self, addr, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((addr, port))
        self.sock.setblocking(False)
        self.addr = addr
        self.port = port
        self.players = {}

    def process_data(self, raw_data, addr):
        data = json.loads(raw_data.decode())
        logging.debug(f"Received {data} from {addr}")

        if data["message"] == "JOIN":
            if self.players.get(data["username"]) is not None:
                err = {"message": "ERROR", "desc": "Username already present"}
                self.sock.sendto(json.dumps(err).encode(), addr)

            self.players[data["username"]] = {"pos": "0,0", "addr": addr}
            logging.info(f"{data['username']} joined")
            logging.debug(f"Players: {self.players}")

            res = {"message": "JOIN", "pos": "0,0"}
            self.sock.sendto(json.dumps(res).encode(), addr)

        elif data["message"] == "LEAVE":
            if self.players.get(data["username"]) is None:
                err = {"message": "ERROR", "desc": "Username not found"}
                self.sock.sendto(json.dumps(err).encode(), addr)

            del self.players[data["username"]]
            self.sock.sendto(raw_data, addr)
            logging.info(f"{data['username']} left")
            logging.debug(f"Players: {self.players}")

    def start(self):
        logging.info(f"Started server on {self.addr}:{self.port}")
        logging.info("Press Ctrl+C to stop server")
        try:
            while True:
                r_socks, _, _ = select.select([self.sock], [], [], 1)
                if len(r_socks) != 0:
                    raw_data, addr = self.sock.recvfrom(1024)
                    self.process_data(raw_data, addr)

        except KeyboardInterrupt:
            self.sock.close()
            sys.exit()
