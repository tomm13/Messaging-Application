##2/9/2022
##V13 Beta

import socket
from threading import Thread
import time
import random

s = socket.socket()

UserCount = 1000
UserOnline = 0
ModOnline = 0
SpaceRemaining = UserCount

Hostname = socket.gethostname()
IP = socket.gethostbyname(Hostname)
#IP = ''
Port = 49125

# Clients and Mods are lists of ClientSockets, whereas Users and ModUsers is a list of Usernames
Clients = []
Users = []
Mods = []
ModUsers = []

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
            # print("[Server] Public Key =", (e, N))
            break

    for k in range(1, 2 * Maximum):
        if (k * PhiN + 1) % e == 0:
            if not (k * PhiN + 1) // e == e:
                global d
                d = (k * PhiN + 1) // e
                break

    print("[Private] Private Key =", (d, N))

    Connect()

def VoteKick(Message, ClientSocket):
    # ClientSocket is the mod socket
    # Username requested to kick
    # UserKickSocket is the user socket
    # UserToKick is the user to be kicked
    try:
        Index = Clients.index(ClientSocket)
        Username = Users[Index]

        UserToKick = Message[6:]
        Index = Users.index(UserToKick)
        UserKickSocket = Clients[Index]

        if UserToKick not in ModUsers:
            # If the person a mod is trying to kick is not a mod
            if Username in ModUsers:
                # If the person kicking is a mod
                if len(Mods) == 1:
                    PublicCommand((Username + " is kicking " + UserToKick))
                    RemoveUser(UserToKick, UserKickSocket)

                if len(Mods) > 1:
                    PrivateCommand("You cannot kick at this time", ClientSocket)
            else:
                PrivateCommand("You do not have the power to execute this action", ClientSocket)
        else:
            PrivateCommand("You cannot kick a mod", ClientSocket)
    except:
        PrivateCommand("You cannot kick this person as they do not exist", ClientSocket)

def ModSelection(Message, Username, ClientSocket):
    global Mods, ModUsers, ModOnline
    # ClientSocket = User who should have mod giving someone else mod
    # Or User who doesn't have mod but is the first online, or first
    # to apply for mod.

    # ModSocket = User who should not have mod but is being applied by
    # a User who does have mod.

    try:
        ModCandidate = Message[5:]
        Index = Users.index(ModCandidate)
        ModSocket = Clients[Index]

        Index = Clients.index(ClientSocket)
        Username = Users[Index]

        if UserOnline == 1:
            if not ModSocket in Mods:
                print("[Mod] Mod Assigned to", Username, "as there was only 1 user online")
                Mods.append(ClientSocket)
                ModUsers.append(Username)
                PrivateBroadcast(Message, ClientSocket)
                PrivateCommand((Username + " is now a mod "), ClientSocket)
                ModOnline += 1
            else:
                PrivateCommand("You are already a mod", ClientSocket)

        elif ModOnline == 0:
            if not ModSocket in Mods:
                print("[Mod] Mod Assigned to", ModCandidate, "as there were no mods online")
                Mods.append(ModSocket)
                ModUsers.append(ModCandidate)
                PrivateBroadcast(Message, ModSocket)
                PublicCommand((ModCandidate + " is now a mod"))
                ModOnline += 1
            else:
                PrivateCommand("You are already a mod", ClientSocket)

        elif ClientSocket in Mods:
            if not ModSocket in Mods:
                print("[Mod] Mod Assigned by", Username, "to", ModCandidate)
                Mods.append(ModSocket)
                ModUsers.append(ModCandidate)
                PrivateBroadcast(Message, ModSocket)
                PublicCommand((Username + " gave " + ModCandidate + " mod"))
                ModOnline += 1

            else:
                if ModSocket == ClientSocket:
                    PrivateCommand("You are already a mod", ClientSocket)
                else:
                    PrivateCommand("Your moderator candidate is already a mod", ClientSocket)
        else:
            PrivateCommand("You do not have the power to execute this action", ClientSocket)
    except ValueError:
        PrivateCommand("Your moderator candidate is not a valid user", ClientSocket)

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
    s.bind((IP, Port))
    print("[Server] Server Hosted on " + str(IP) + " with Port " + str(Port))

def Broadcast(Message):
    # Sends a Public Message to all Connected Clients, not for Animating Purposes
    time.sleep(0.1)
    print("[Client] " + Message)

    Message = RSAEncrypt(Message)
    for Client in Clients:
        Client.send(Message.encode())

def PublicCommand(Message):
    # Sends "/display", which tells every Client to Animate it's banner
    time.sleep(0.1)
    Message = "/display " + Message
    Message = RSAEncrypt(Message)
    for Client in Clients:
        Client.send(Message.encode())

def PrivateBroadcast(Message, ClientSocket):
    # Sends a Private Message to 1 Specfic Client, not for Animating Purposes.
    time.sleep(0.1)

    Message = RSAEncrypt(Message)
    ClientSocket.send(Message.encode())

def PrivateCommand(Message, ClientSocket):
    # Sends "/display", which tells 1 specific Client to Animate it's banner
    time.sleep(0.1)
    Message = "/display " + Message
    Message = RSAEncrypt(Message)
    ClientSocket.send(Message.encode())

def RemoveUser(Username, ClientSocket):
    try:
        global UserOnline, Clients, Users, ModOnline
        if ClientSocket in Mods:
            Mods.remove(ClientSocket)
            ModUsers.remove(Username)
            ModOnline -= 1

        Message = "/remove " + Username
        Broadcast(Message)

        Clients.remove(ClientSocket)
        Users.remove(Username)

        UserOnline -= 1
    except:
        "[Server] Failed to remove user"

def Listen(ClientSocket):
    global UserOnline, Clients, Users
    while True:
        try:
            Index = Clients.index(ClientSocket)
            Username = Users[Index]

            Message = ClientSocket.recv(1024).decode()
            UnifiedMessage = Username + ": " + Message

            if Message:
                if Message[0] == "/":
                    if Message == "/leave":
                        if ClientSocket in Clients:
                            RemoveUser(Username, ClientSocket)

                        break
                    else:
                        Command(Message, Username, ClientSocket)
                else:
                    Broadcast(UnifiedMessage)

        except:
            RemoveUser(Username, ClientSocket)
            break

def Command(Message, Username, ClientSocket):
    if Message == "/space":
        PrivateCommand(str(UserCount), ClientSocket)
    elif Message == "/online":
        PrivateCommand(str(UserOnline), ClientSocket)
    elif Message == "/users":
        if len(Users) == 1:
            PrivateCommand(str(Users[0]), ClientSocket)
        else:
            for User in Users:
                PrivateCommand(str(User), ClientSocket)
                time.sleep(0.1)
    elif Message == "/mods":
        if len(ModUsers) == 1:
            PrivateCommand(str(ModUsers[0]), ClientSocket)
        else:
            for ModUser in ModUsers:
                PrivateCommand(str(ModUser), ClientSocket)
                time.sleep(0.1)
    elif Message == "/spaceleft":
        PrivateCommand(str(SpaceRemaining), ClientSocket)
    elif Message == "/ip":
        if not IP == "":
            PrivateCommand(str(IP), ClientSocket)
        else:
            PrivateCommand("35.242.179.43", ClientSocket)
    elif Message == "/port":
        PrivateCommand(str(Port), ClientSocket)
    elif Message == "/key":
        PrivateCommand(str((d, N)), ClientSocket)
    elif Message == "/theme":
        PrivateBroadcast("/theme", ClientSocket)
    elif Message[0:6] == "/color":
        PrivateBroadcast(Message, ClientSocket)
    elif Message[0:5] == "/save":
        PrivateBroadcast(Message, ClientSocket)
    elif Message[0:4] == "/mod":
        if Message == "/modonline":
            PrivateCommand(str(ModOnline), ClientSocket)
        else:
            ModSelection(Message, Username, ClientSocket)
    elif Message[0:5] == "/kick":
        VoteKick(Message, ClientSocket)
    else:
        PrivateCommand("Your command is unknown", ClientSocket)

def Connect():
    global UserOnline, SpaceRemaining, Users, Clients
    GeneratePort()
    s.listen()
    for i in range(UserCount):
        try:
            global ClientSocket
            ClientSocket, Address = s.accept()
            Clients.append(ClientSocket)

            Username = ClientSocket.recv(1024).decode()
            Users.append(Username)

            Message = "/add " + " ".join(Users)
            Broadcast(Message)

            UserOnline += 1
            SpaceRemaining -= 1

            ListeningThread = Thread(target=Listen, args=[ClientSocket])
            ListeningThread.start()

        except:
            RemoveUser(Username, ClientSocket)
            pass

GetKey()