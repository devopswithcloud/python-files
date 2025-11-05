#udp client 
import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.sendto(b"Hello UDPServer",("localhost",9998))
data,server =client.recvfrom(1024)
print("server says",data.decode())
client.close()