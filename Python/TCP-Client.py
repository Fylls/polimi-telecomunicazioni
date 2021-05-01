from socket import *

serverName = 'servername'
serverPort = 12000

# AF_INET: network uses IPv4 || SOCK_STREAM: socket uses TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

# Initializing TCP connection
# (TCP is a connection-oriented protocol) -> three way handshake
clientSocket.connect((serverName, serverPort))
debugString = f"TCP Connection established with {serverName} on port {serverPort}\n\n"
print(debugString)

message = input("write here something all lowercase: ")

# we don't decide the clientPort (OS does this for us)
# we have established a socket-connection, no need to specity who to send to
clientSocket.send(message.encode())
modifiedMessage = clientSocket.recvfrom(1024)

print("\n\nmessage from server" + modifiedMessage.decode())
clientSocket.close()
