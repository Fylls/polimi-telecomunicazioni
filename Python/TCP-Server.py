from socket import *

serverPort = 12000
MAX = 10

# AF_INET: network uses IPv4 || SOCK_STREAM: socket uses UDP
serverSocket = socket(AF_INET, SOCK_STREAM)

# Assignning port number to server (manually)
serverSocket.bind(('', serverPort))

# MAX refers to the number of connections in queue at once
serverSocket.listen(MAX)

print("Server is listening on port: " + str(serverPort) + "\n\n")

# Core Application
while True:
    connectionSocket, address = serverSocket.accept()  # newSocket
    sentence = connectionSocket.recvfrom(1024).decode()
    modifiedSentence = message.upper()
    connectionSocket.send(modifiedSentence.encode())
    connectionSocket.close()

# TCP does guarantee a secure and error-free connection
