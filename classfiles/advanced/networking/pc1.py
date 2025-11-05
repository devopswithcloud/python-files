import socket

host = "example.com"
port = 80
request = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"

# Create TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send(request.encode())

response = s.recv(4096)
print(response.decode(errors="ignore"))
s.close()
