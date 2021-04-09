from .settings import *
from .udpserver import UDPServer


server = UDPServer(ADDR, PORT)
server.start()
