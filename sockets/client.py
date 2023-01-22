import socket

port = ("127.0.0.1", 11111)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(port)
