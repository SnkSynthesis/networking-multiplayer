import socket
from .player import Player
from .square import Square
from .settings import *
import json
from typing import Dict, Any
import pygame


def check_response(res: Dict[str, Any], expected_msg: str) -> None:
    if res["message"] != expected_msg:
        raise Exception(f"Unexpected response: {res}")


class UDPServerConnection:
    def __init__(self, addr: str, port: int) -> None:
        self.addr = addr
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.settimeout(5)

    def update(self, player: Player, surface: pygame.surface.Surface):
        # Update player position
        data = {"message": "UPDATE", "username": player.username, "pos": [player.posx, player.posy]}
        self.sock.sendto(json.dumps(data).encode(), (self.addr, self.port))
        raw_res, _ = self.sock.recvfrom(1024)
        res = json.loads(raw_res.decode())
        check_response(res, "UPDATE")
        
        # Render other players
        for username, pl_data in res["players"].items():
            pl = Square(username, pl_data["pos"][0], pl_data["pos"][1], pl_data["color"])
            pl.draw(surface)
        
    def join(self, username: str) -> Player:
        data = {"message": "JOIN", "username": username}
        self.sock.sendto(json.dumps(data).encode(), (self.addr, self.port))
        raw_res, _ = self.sock.recvfrom(1024)
        res = json.loads(raw_res.decode())
        check_response(res, "JOIN")
        player = Player(username, res["color"])
        return player

    def leave(self, player: Player):
        data = {"message": "LEAVE", "username": player.username}
        self.sock.sendto(json.dumps(data).encode(), (self.addr, self.port))
        raw_res, _ = self.sock.recvfrom(1024)
        res = json.loads(raw_res.decode())
        check_response(res, "LEAVE")
