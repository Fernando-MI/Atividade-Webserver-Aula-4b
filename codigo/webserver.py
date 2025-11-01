#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
usedPort = 65534
serverSocket.bind(('', usedPort))
serverSocket.listen(5)
#Prepare a sever socket

#Fill in start
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    print(f"on 'http://localhost:{usedPort}/pagina.html'")
    connectionSocket, addr = serverSocket.accept()
    try:
        message =  connectionSocket.recv(1024).decode()

        filename = message.split()[1] 
        f = open(filename[1:], errors="ignore", encoding="UTF-8") 
        outputdata = f.read()
        #Send one HTTP header line into socket
        connectionSocket.send(b"HTTP/1.1 200 OK\ncontent-Type: text/html\n\n")
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)): 
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        f = open("superErro3000.html", encoding="UTF-8")
        outputdata = f.read()
        connectionSocket.send(b"HTTP/1.1 404 ERROR\ncontent-Type: text/html\n\n")

        for i in range(0, len(outputdata)): 
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode()) 
        connectionSocket.close()
        break

    
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data 