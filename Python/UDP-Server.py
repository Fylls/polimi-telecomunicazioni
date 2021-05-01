from socket import *

serverPort = 12000

# AF_INET: network uses IPv4 || SOCK_DGRAM: socket uses UDP
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assignning port number to server (manually)
serverSocket.bind(('', serverPort))

print("Server is listening on port: " + str(serverPort))

# Core Application
while True:
    sentence, clientAddress = serverSocket.recvfrom(2048).decode()
    modifiedSentence = sentence.upper()
    serverSocket.sendto(modifiedSentence.encode(), clientAddress)


# UDP does not guarantee a secure and error-free connection
