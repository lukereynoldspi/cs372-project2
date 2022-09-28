import socket
import sys

if len(sys.argv) >= 3:
    host = str(sys.argv[1])
    port = int(sys.argv[2])
else:
    print("No host or port specified, using default values")
    host = "example.com"
    port = 80

s = socket.socket()
s.connect((host, port))

get = ("GET / HTTP/1.1\r\nHost: {}\r\nConnection: close\r\n\r\n").format(host)
s.sendall(get.encode("ISO-8859-1"))
d = s.recv(4096)  # Receive up to 4096 bytes
if len(d) == 0:
    s.close
