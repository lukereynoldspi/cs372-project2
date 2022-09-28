import socket
import sys

if len(sys.argv) >= 2:
    port = int(sys.argv[1])
else:
    port = 28333

s = socket.socket()
s.bind(('', port))
s.listen()
new_conn = s.accept()
new_socket = new_conn[0]  # This is what we'll recv/send on
