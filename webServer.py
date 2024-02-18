# import socket module
from socket import *
import sys  

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(("", port))
    serverSocket.listen(1)
    print("The server is ready to receive")

    while True:
        print("Ready to serve...")
        connectionSocket, addr = serverSocket.accept()
        
        try:
            message = connectionSocket.recv(1024).decode()
            filename = message.split()[1]
            f = open(filename[1:], 'r')  
            outputData = f.read()  
            f.close()
            header = 'HTTP/1.1 200 OK\r\n'
            header += 'Content-Type: text/html; charset=UTF-8\r\n'
            header += 'Connection: close\r\n\r\n'  
            connectionSocket.send(header.encode() + outputData.encode())
            connectionSocket.close()

        except IOError:
            header = 'HTTP/1.1 404 Not Found\r\n'
            header += 'Content-Type: text/html; charset=UTF-8\r\n'
            header += 'Connection: close\r\n\r\n'
            errorMessage = '<html><body><h1>404 Not Found</h1></body></html>'
            connectionSocket.send(header.encode() + errorMessage.encode())
            connectionSocket.close()

if __name__ == "__main__":
    webServer(13331)
