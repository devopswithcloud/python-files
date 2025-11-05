#udp server
import socket

server= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("localhost",9998))
print("UDP server listiening")
while True:
    data,addr = server.recvfrom(1024)
    print(f"Message from {addr}:{data.decode()}")
    server.sendto(data.upper(),addr)