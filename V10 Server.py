##8/8/2022
##V10 Server

import socket
from threading import Thread

#UserCount = int(input("Enter maximum number of users"))
UserCount = 2
UserOnline = 0

HostName = socket.gethostname()

IP = '192.168.1.138'
Port = 1234

s = socket.socket()
s.bind((IP, Port))
print("[Server] Server Hosted with " + str(UserCount) + " space(s)")

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




