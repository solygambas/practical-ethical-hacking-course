import socket

HOST = '127.0.0.1'
PORT = 7777
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # af_inet is the address family for ipv4, sock_stream is the socket type for tcp
s.connect((HOST, PORT))

# on kali linux, you can use "nc -nlvp 7777" to listen on port 7777


