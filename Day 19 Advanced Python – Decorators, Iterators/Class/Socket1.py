import socket

# create a socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP Socket
# print("Socket Created")
# print(mysock)

# connect to a server
# mysock.connect(("www.google.com", 80))
# print("Socket Connected")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Waiting for a connection...")

try:
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    conn.sendall(b'Hello, Client!')
    conn.close()
exce