import socket
import json
import select
import logging
import random
from client.settings import *
from .settings import LOGGING_LEVEL
import sys
from typing import Dict, Any
from client.square import *


logging.basicConfig(format="[SERVER] %(levelname)s: %(message)s", level=LOGGING_LEVEL)

square = Square()


class UDPServer:
    def __init__(self, addr: str, port: int) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((addr, port))

        # setblocking(False) makes the socket non-blocking or async
        # This means that things like recv(1024) won't synchronously block the execution of the program.
        self.sock.setblocking(False)

        self.addr = addr
        self.port = port

        # Keep track of players by username
        self.players: Dict[str, Dict[str, Any]] = {}

    def process_data(self, raw_data: bytes, addr: Any) -> None:
        # Convert data from bytes to str to dict
        data: dict = json.loads(raw_data.decode())
        logging.debug(f"Received {data} from {addr}")

        if data["message"] == "JOIN":
            # Make sure the username isn't already present
            if self.players.get(data["username"]) is not None:
                err = {"message": "ERROR", "desc": "Username already present"}
                self.sock.sendto(json.dumps(err).encode(), addr)
    
            computed_pos = f"{random.randint(0, DISPLAY_WIDTH-SQUARE_WIDTH)},{random.randint(0, DISPLAY_HEIGHT-SQUARE_WIDTH)}"
            self.players[data["username"]] = {"pos": computed_pos, "addr": addr}
            logging.info(f"{data['username']} joined")
            logging.debug(f"Players: {self.players}")

            # Send this message with position as confirmation
            res = {
                "message": "JOIN",
                "pos": computed_pos,
            }
            self.sock.sendto(json.dumps(res).encode(), addr)

        elif data["message"] == "LEAVE":
            # Make sure that the username is present
            if self.players.get(data["username"]) is None:
                err = {"message": "ERROR", "desc": "Username not found"}
                self.sock.sendto(json.dumps(err).encode(), addr)

            del self.players[data["username"]]
            # Echo as confirmation
            self.sock.sendto(raw_data, addr)
            logging.info(f"{data['username']} left")
            logging.debug(f"Players: {self.players}")
        
        elif data["message"] == "MOVED":

            
            exsist = False
            if self.players.get(data["username"]) is None: 
                err = {"message": "ERROR", "desc": "Username not found"}
            
            self.players[data["username"]] = {"pos": square.posx, square.posy}
            exsist = True
        
        elif data["message"] == "UPDATE":

            if self.players.get(data["username"]) is None and exsist == True:
                err = {"message": "ERROR", "desc": "Username not found and Original data for MOVED has not been created yet"}
            
            self.players[data["username"]] = {"pos": square.posx, square.posy}
            


    def start(self) -> None:
        logging.info(f"Started server on {self.addr}:{self.port}")
        logging.info("Press Ctrl+C to stop server")
        try:
            while True:
                # 1st parameter - sockets to be monitored for reading data
                # 2nd parameter - sockets to be monitored for writing data
                # 3rd parameter - sockets to be monitored for exceptions
                # 4th parameter - timeout to not let select run forever
                r_socks, _, _ = select.select([self.sock], [], [], 1)

                # When self.sock is ready to be read, len(r_socks) won't be 0
                if len(r_socks) != 0:
                    raw_data, addr = self.sock.recvfrom(1024)
                    self.process_data(raw_data, addr)

        except KeyboardInterrupt:  # When Ctrl+C is pressed
            self.sock.close()
            sys.exit()
