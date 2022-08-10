##10/8/2022
##Make user define saving directory
##V12 RC

import socket
from threading import Thread

#UserCount = int(input("Enter maximum number of users"))
UserCount = 1
UserOnline = 0

HostName = socket.gethostname()

IP = '192.168.1.138'
Ports = [1234, 5023, 5050]

Clients = []
Users = []

def GeneratePort():
    for PortTest in Ports:
        try:
            global s, IP, Port
            s = socket.socket()
            s.bind((IP, PortTest))
            Port = PortTest
            print("[Server] Server Hosted with " + str(UserCount) +
                  " space(s) on Port " + str(Port))
            break
        except OSError:
            print("[Server] Port " + str(PortTest) + " not available")

def Broadcast(Message):
    print("[Client] " + Message)
    for Client in Clients:
        Client.send(Message.encode())

def ServerBroadcast(Message):
    Message = "[Server] " + Message
    print(Message)
    for Client in Clients:
        Client.send(Message.encode())

def Listen(ClientSocket):
    global UserOnline
    while True:
        Message = ClientSocket.recv(1024).decode()

        Index = Clients.index(ClientSocket)
        Username = Users[Index]

        if Message:
            UnifiedMessage = Username + ": " + Message
            Broadcast(UnifiedMessage)

        if Message[0] == "/":
            Command(Message)

def Command(Message):
    print("[Server] Command detected")
    if Message == "/space":
        ServerBroadcast(str(UserCount))
    elif Message == "/online":
        ServerBroadcast(str(UserOnline))
    elif Message == "/users":
        for User in Users:
            ServerBroadcast((User + "\n"))
    else:
        ServerBroadcast("Unknown Command")

def main():
    global UserOnline
    GeneratePort()
    s.listen()
    for i in range(UserCount):
        global ClientSocket
        ClientSocket, Address = s.accept()
        Clients.append(ClientSocket)

        Username = ClientSocket.recv(1024).decode()
        Users.append(Username)

        Message = Username + " has connected"
        Broadcast(Message)

        UserOnline += 1

        ListeningThread = Thread(target = Listen, args = [ClientSocket])
        ListeningThread.start()

main()



