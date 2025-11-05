#file server
import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost",8888))
server.listen(1)
print("Server listing..")
conn,addr =server.accept()
print(f"connected by {addr}")

with open("sample.txt","rb") as f:
    data =f.read(1024)
    while data:
        conn.send(data)
        data =f.read(1024)

conn.close()