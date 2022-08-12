##12/8/2022
##attempt at making server more independent
##V12 RC 3

import socket
from threading import Thread
import time

#UserCount = int(input("Enter maximum number of users"))
UserCount = 1000
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
            print("[Server] Port " + str(PortTest) + " is not available")

def Broadcast(Message):
    time.sleep(0.1)
    print("[Client] " + Message)
    for Client in Clients:
        Client.send(Message.encode())

def ServerBroadcast(Message):
    time.sleep(0.1)
    Message = "[Server] " + Message
    print(Message)
    for Client in Clients:
        Client.send(Message.encode())

def RemoveUser(ClientSocket, Username):
    global UserOnline, Clients, Users
    Clients.remove(ClientSocket)
    Users.remove(Username)
    UserOnline -= 1

    Broadcast((Username + " has disconnected"))

def Listen(ClientSocket):
    global UserOnline, Clients, Users
    while True:
        Index = Clients.index(ClientSocket)
        Username = Users[Index]

        try:
            Message = ClientSocket.recv(1024).decode()
            UnifiedMessage = Username + ": " + Message

            if Message:
                Broadcast(UnifiedMessage)
                if Message[0] == "/":
                    if Message == "/leave":
                        RemoveUser(ClientSocket, Username)
                        break
                    else:
                        Command(Message)

        except ConnectionResetError:
            RemoveUser(ClientSocket, Username)
            break

def Command(Message):
    if Message == "/space":
        ServerBroadcast(str(UserCount))
    elif Message == "/online":
        ServerBroadcast(str(UserOnline))
    elif Message == "/users":
        if len(Users) == 1:
            ServerBroadcast(Users[0])
        else:
            for User in Users:
                if User == Users[(len(Users) - 1)]:
                    ServerBroadcast((User))
                    break
                ServerBroadcast((User + ", "))

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



