from socket import *

serverName = 'servername'
serverPort = 12000

# AF_INET: network uses IPv4 || SOCK_DGRAM: socket uses UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input("write here something all lowercase: ")

# we don't decide the clientPort (OS does this for us)
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print(modifiedMessage.decode())
clientSocket.close()
