import socket
import sys


HOST, PORT= "localhost", 9999
data= " ".join(sys.argv[1:])

sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((HOST, PORT))
    sock.sendall("Hello World"+ "\n")
finally:
    sock.close()
