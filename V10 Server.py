##9/8/2022
##Server now chooses a port systematically given 1 port is taken
##V11 Server

import socket
from threading import Thread

#UserCount = int(input("Enter maximum number of users"))
UserCount = 2
UserOnline = 0

HostName = socket.gethostname()

IP = '192.168.1.138'
Ports = [1234, 5023, 5050]

for Port in Ports:
    try:
        s = socket.socket()
        s.bind((IP, Port))
        print("[Server] Server Hosted with " + str(UserCount) +
              " space(s) on Port " + str(Port))
        break
    except OSError:
        print("[Server] Port " + str(Port) + " not available")

s.listen()

global Clients
Clients = []

global Users
Users = []

def Broadcast(Message):
    print("[Client] " + Message)
    for Client in Clients:
        Client.send(Message.encode())

def Listen(ClientSocket):
    while True:
        Message = ClientSocket.recv(1024).decode()
        if Message:
            Broadcast(Message)

for i in range(UserCount):
    global ClientSocket
    ClientSocket, Address = s.accept()
    Clients.append(ClientSocket)

    Username = ClientSocket.recv(1024).decode()
    Users.append(Username)

    Message = Username + " has connected"
    Broadcast(Message)

    UserOnline += 1
    print("[Server] " + str(UserOnline) +
          " of " + str(UserCount) +
          " space(s) are taken")

    ListeningThread = Thread(target = Listen, args = [ClientSocket])
    ListeningThread.start()




