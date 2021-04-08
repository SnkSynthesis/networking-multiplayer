from .settings import *
import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ADDR, PORT))

print(f"Started server on {ADDR}:{PORT}")

while True:
    message, addr = sock.recvfrom(1024)
    print(f"{message} from {addr}")
