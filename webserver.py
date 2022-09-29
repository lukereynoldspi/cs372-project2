import socket
import sys
import re 

if len(sys.argv) >= 2:
    port = int(sys.argv[1])
else:
    port = 28333
s = socket.socket()
s.bind(('', port))
s.listen()
new_conn = s.accept()
new_socket = new_conn[0]  # This is what we'll recv/send on
while True:
    d = new_socket.recv(4096)
    if "\r\n\r\n" in d.decode("ISO-8859-1"):
        break
get = ("HTTP/1.1 \r\nContent-Type: text/plain\r\nContent-Length: 6\r\nConnection: close\r\n\r\nHello!")
s.sendall(get.encode("ISO-8859-1"))
new_socket.close()