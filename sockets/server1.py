import socket

port = ("127.0.0.1", 11111)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(port)

print("Binded to port: " + str(port))

sock.listen(1)
conn1, addr1 = sock.accept()

print("connected by: " + str(addr1))

