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
print(s)
