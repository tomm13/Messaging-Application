##15/8/2022
##V13 RC2 Server

import socket
from threading import Thread
import time
import random

s = socket.socket()

#UserCount = int(input("Enter maximum number of users"))
UserCount = 1000
UserOnline = 0
SpaceRemaining = UserCount

HostName = socket.gethostname()
IP = socket.gethostbyname(HostName)
#IP = '192.168.1.123'
Port = 0000

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
    for PortTest in range(49125, 65535):
        try:
            global Port
            s.bind((IP, PortTest))
            Port = PortTest
            print("[Server] Server Hosted on " + str(IP) + " with Port " + str(Port))
            break
        except OSError:
            pass

def DisplayBroadcast(Message):
    time.sleep(0.1)
    Message = "/display " + Message
    print("[Display] " + Message)

    Message = RSAEncrypt(Message)
    for Client in Clients:
        Client.send(Message.encode())

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

def PrivateBroadcast(Message, ClientSocket):
    time.sleep(0.1)
    Message = "/display " + Message
    print("[Private] " + Message)

    Message = RSAEncrypt(Message)
    ClientSocket.send(Message.encode())

def RemoveUser(ClientSocket, Username):
    global UserOnline, Clients, Users
    LeavingUser = Username
    Clients.remove(ClientSocket)
    Users.remove(Username)

    Message = "/remove " + LeavingUser
    Broadcast(Message)

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
                if Message[0] == "/":
                    if Message == "/leave":
                        RemoveUser(ClientSocket, Username)
                        break
                    else:
                        Command(Message, ClientSocket)
                else:
                    Broadcast(UnifiedMessage)

        except ConnectionResetError:
            RemoveUser(ClientSocket, Username)
            break

def Command(Message, ClientSocket):
    if Message == "/space":
        PrivateBroadcast(str(UserCount), ClientSocket)
    elif Message == "/online":
        PrivateBroadcast(str(UserOnline), ClientSocket)
    elif Message == "/users":
        if len(Users) == 1:
            PrivateBroadcast(str(Users[0]), ClientSocket)
        else:
            for User in Users:
                PrivateBroadcast(str(User), ClientSocket)
                time.sleep(3)

    elif Message == "/spaceleft":
        PrivateBroadcast(str(SpaceRemaining), ClientSocket)
    elif Message == "/ip":
        PrivateBroadcast(str(IP), ClientSocket)
    else:
        PrivateBroadcast("Unknown Command", ClientSocket)

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

        Message = "/add " + " ".join(Users)
        Broadcast(Message)

        UserOnline += 1
        SpaceRemaining -= 1

        ListeningThread = Thread(target = Listen, args = [ClientSocket])
        ListeningThread.start()

GetKey()
