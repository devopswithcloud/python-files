#TCP server

import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost",9999))
server.listen(1)
print("Server listing..")
conn,addr =server.accept()
print(f"connected by {addr}")

while True:
    data =conn.recv(1024)
    if not data:
        break
    print("Received",data.decode())
    conn.send(data.upper())

conn.close()