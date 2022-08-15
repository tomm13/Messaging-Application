##15/8/2022
##V12

import socket
from threading import Thread
import time
import random

#UserCount = int(input("Enter maximum number of users"))
UserCount = 1000
UserOnline = 0
SpaceRemaining = UserCount

#HostName = socket.gethostname()
#IP = socket.gethostbyname(HostName)

IP = '192.168.1.138'
Ports = [1234, 5023, 5050]
Clients = []
Users = []

def GetKey():
    global Minimum, Maximum
    Minimum = 10
    Maximum = 350
    Primes = []
    PrimeCandidates = []
    for Number in range(Minimum, Maximum):
        IsPrime = True
        for Factor in range(2, Number):
            if Number % Factor == 0:
                IsPrime = False
        if IsPrime:
            Primes.append(Number)

    for Prime in range(2):
        Max = len(Primes) - 1
        RandomNum = random.randint(0, Max)
        PrimeCandidates.append(Primes[RandomNum])
        Primes.pop(RandomNum)

    global P, Q, N, PhiN
    P = PrimeCandidates[0]
    Q = PrimeCandidates[1]
    N = P * Q
    PhiN = (P - 1) * (Q - 1)

    eList = []
    for eCandidate in range(2, PhiN):
        eList.append(eCandidate)

    global e

    for e in eList:
        PhiNFactors = []
        NFactors = []
        eFactors = []
        for Factor in range(1, e + 1):
            if e % Factor == 0:
                eFactors.append(Factor)

        for Factor in range(1, N + 1):
            if N % Factor == 0:
                NFactors.append(Factor)

        for Factor in range(1, PhiN + 1):
            if PhiN % Factor == 0:
                PhiNFactors.append(Factor)

        if 1 in eFactors and 1 in PhiNFactors and 1 in NFactors:
            PhiNFactors.remove(1)
            NFactors.remove(1)
            eFactors.remove(1)

        if len(eFactors) == 1 and eFactors[0] not in PhiNFactors and eFactors[0] not in NFactors:
            #print("[Server] Public Key =", (e, N))
            break

    for k in range(1, 2 * Maximum):
        if (k * PhiN + 1 ) % e == 0:
            if not (k * PhiN + 1) // e == e:
                global d
                d = (k * PhiN + 1) // e
                break

    print("[Private] Private Key =", (d, N))

    Connect()

def RSAEncrypt(Message):
    RSAEncryptedMessage = []
    for Letter in Message:
        Index = ord(Letter)
        NewIndex = pow(Index, e, N)
        RSAEncryptedMessage.append(str(NewIndex))
        RSAEncryptedMessage.append(" ")

    Message = str("".join(RSAEncryptedMessage))
    return Message

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
            pass

def Broadcast(Message):
    time.sleep(0.1)
    print("[Client] " + Message)

    Message = RSAEncrypt(Message)
    for Client in Clients:
        Client.send(Message.encode())

def ServerBroadcast(Message):
    time.sleep(0.1)
    Message = "[Server] " + Message
    print(Message)

    Message = RSAEncrypt(Message)
    for Client in Clients:
        Client.send(Message.encode())

def RemoveUser(ClientSocket, Username):
    global UserOnline, Clients, Users
    LeavingUser = Username
    Clients.remove(ClientSocket)
    Users.remove(Username)

    UsersList = "/remove " + LeavingUser
    Broadcast(UsersList)

    Broadcast((LeavingUser + " has disconnected"))
    UserOnline -= 1

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
    elif Message == "/spaceleft":
        ServerBroadcast(str(SpaceRemaining))
    else:
        ServerBroadcast("Unknown Command")

def Connect():
    global UserOnline, SpaceRemaining
    GeneratePort()
    s.listen()
    for i in range(UserCount):
        global ClientSocket
        ClientSocket, Address = s.accept()
        Clients.append(ClientSocket)

        Username = ClientSocket.recv(1024).decode()
        Users.append(Username)

        UsersList = "/add " + " ".join(Users)
        Broadcast(UsersList)

        Message = Username + " has connected"
        Broadcast(Message)

        UserOnline += 1
        SpaceRemaining -= 1

        ListeningThread = Thread(target = Listen, args = [ClientSocket])
        ListeningThread.start()

GetKey()
