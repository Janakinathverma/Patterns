import socket
hostname=socket.gethostname()
ipaddress=socket.gethostbyname (hostname)
print(ipaddress)