import sys
import socket

DEFAULT_PORT = 69
ip = sys.argv[1]

# https://www.rfc-editor.org/rfc/rfc1350
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    socket.sendto("WRQ", (ip, DEFAULT_PORT))
except Exception as e:
    print(f"Exception: {e}")
    sys.exit(1)
