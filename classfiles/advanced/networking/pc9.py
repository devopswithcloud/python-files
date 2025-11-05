#file client
import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("localhost",8888))

with open("received_file.txt","wb") as f:
    while True:
        data =client.recv(1024)
        if not data:
            break
        f.write(data)

client.close()