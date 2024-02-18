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
            connectionSocket.send(outputData.encode())
        except IOError:
            errorMessage = 'File not found'
            connectionSocket.send(errorMessage.encode())
        finally:
            connectionSocket.close()

if __name__ == "__main__":
    webServer(13331)