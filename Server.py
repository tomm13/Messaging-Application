##21/9/2022
##V13 Beta

import socket
from threading import Thread
import time
import random


class Security:
    def __init__(self):
        pass

    def generateKey(self):
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
                    d = (k * PhiN + 1) // e
                    break

        print("[Private] Private Key =", (d, N))

        self.d = d
        self.e = e
        self.N = N

    def generatePort(self):
        while True:
            try:
                connectionInstance.socket.bind((connectionInstance.host, connectionInstance.port))
                print("[Server] Server Hosted on " + str(connectionInstance.host) + " with Port " + str(connectionInstance.port))
                break

            except ConnectionError:
                connectionInstance.port = random.randint(49125, 65536)

    def encrypt(self, message):
        RSAEncryptedmessage = []
        for Letter in message:
            Index = ord(Letter)
            NewIndex = pow(Index, e, N)
            RSAEncryptedmessage.append(str(NewIndex))
            RSAEncryptedmessage.append(" ")

        message = str("".join(RSAEncryptedmessage))
        return message

class Actions:
    def __init__(self):
        self.modOnline = 0
        self.mods = []
        self.modUsers= []
        self.voteActive = False

    def vote(self, message, clientSocket):
        if message[5:] == "kick":
            self.voteActive = True

    def mod(self, message, clientSocket):
        modSocket = clientSocket
        index = connectionInstance.clients.index(modSocket)
        modUsername = connectionInstance.users[index]

        username = message[5:]
        index = connectionInstance.users.index(username)
        clientSocket = connectionInstance.clients[index]

        if clientSocket not in self.mods and username not in self.modUsers:
            if self.modOnline == 0:
                self.modUsers.append(username)
                self.mods.append(clientSocket)
                self.modOnline += 1

                action = "/mod " + username
                sendInstance.privateBroadcast(action, clientSocket)

                message = username + " is now a mod"
                sendInstance.broadcastDisplay(message)

            elif modSocket in self.mods and modUsername in self.modUsers:
                self.modUsers.append(username)
                self.mods.append(clientSocket)
                self.modOnline += 1

                action = "/mod " + username
                sendInstance.privateBroadcast(action, clientSocket)

                message = username + " is now a mod"
                sendInstance.broadcastDisplay(message)

            else:
                sendInstance.privateBroadcastDisplay("You need to be a mod to do this", modSocket)
        else:
            sendInstance.privateBroadcastDisplay("You are already a mod", clientSocket)

class Send:
    def broadcast(self, message):
        # Send a public message to every client, not for animating purposes.
        time.sleep(0.1)
        print("[Client] " + message)

        message = securityInstance.encrypt(message)
        for client in connectionInstance.clients:
            client.send(message.encode())

    def broadcastDisplay(self, message):
        # Send "/display" + a message to every client.
        time.sleep(0.1)
        print("[PublicDisplay] " + message)

        message = "/display " + message
        message = securityInstance.encrypt(message)

        for client in connectionInstance.clients:
            client.send(message.encode())

    def privateBroadcast(self, message, clientSocket):
        # Send a private message to 1 specific client, not for animating purposes.
        time.sleep(0.1)
        print("[Private] "+ message)

        message = securityInstance.encrypt(message)
        clientSocket.send(message.encode())

    def privateBroadcastDisplay(self, message, clientSocket):
        # Send "/display" + a message to 1 specific client.
        time.sleep(0.1)
        print("[PrivateDisplay] " + message)

        message = "/display " + message
        message = securityInstance.encrypt(message)
        clientSocket.send(message.encode())

    def command(self, message, clientSocket):
        # Ues list to prevent doubled code
        if message == "/space":
            sendInstance.privateBroadcastDisplay(str(connectionInstance.spaceRemaining), clientSocket)
        elif message == "/online":
            sendInstance.privateBroadcastDisplay(str(connectionInstance.userOnline), clientSocket)
        elif message == "/users":
            for user in connectionInstance.users:
                sendInstance.privateBroadcastDisplay(str(user), clientSocket)
                time.sleep(0.1)
        elif message == "/ip":
            sendInstance.privateBroadcastDisplay(str(connectionInstance.host), clientSocket)
        elif message == "/port":
            sendInstance.privateBroadcastDisplay(str(connectionInstance.port), clientSocket)
        elif message == "/key":
            sendInstance.privateBroadcastDisplay(str(securityInstance.d) + ", " + str(securityInstance.N), clientSocket)
        elif message == "/theme":
            sendInstance.privateBroadcast("/theme", clientSocket)
        elif message[0:6] == "/color":
            sendInstance.privateBroadcast(message, clientSocket)
        elif message[0:5] == "/save":
            sendInstance.privateBroadcast(message, clientSocket)
        elif message[0:4] == "/mod":
            actionsInstance.mod(message, clientSocket)
        elif message[0:5] == "/kick" or message[0:5] == "/vote":
            actionsInstance.vote(message, clientSocket)
        elif message == "/filler":
            sendInstance.privateBroadcast(message, clientSocket)
        elif message[0:5] == "/rate":
            sendInstance.privateBroadcast(message, clientSocket)
        else:
            sendInstance.privateBroadcastDisplay("Your command is unknown", clientSocket)


class Connection:
    def __init__(self):
        self.socket = socket.socket()
        self.host = "192.168.1.138"
        self.port = random.randint(49125, 65535)
        self.userOnline = 0
        self.spaceRemaining = 1000
        self.users = []
        self.clients = []

    def connect(self):
        securityInstance.generatePort()
        securityInstance.generateKey()

        self.socket.listen()

        for i in range(self.spaceRemaining):
            # The main thread listens for incoming connections and accepts it

            clientSocket, Address = self.socket.accept()
            self.clients.append(clientSocket)

            username = clientSocket.recv(1024).decode()
            if username in self.users:
                sendInstance.privateBroadcast("/disconnect", clientSocket)
                self.clients.remove(clientSocket)

            else:
                self.users.append(username)

                message = "/add " + " ".join(self.users)
                sendInstance.broadcast(message)

                self.userOnline += 1
                self.spaceRemaining -= 1

                listeningThread = Thread(target=self.listen, args=[clientSocket])
                listeningThread.start()

    def listen(self, clientSocket):
        index = self.clients.index(clientSocket)
        username = self.users[index]
        while True:
            try:
                message = clientSocket.recv(1024).decode()
                unifiedmessage = username + ": " + message

                if message:
                    if message[0] == "/":
                        if message == "/leave":
                            if clientSocket in self.clients:
                                self.removeUser(username, clientSocket)
                            break
                        else:
                            sendInstance.command(message, clientSocket)
                    else:
                        sendInstance.broadcast(unifiedmessage)
            except ConnectionResetError:
                self.removeUser(username, clientSocket)
                break

    def removeUser(self, username, clientSocket):
        try:
            if clientSocket in actionsInstance.mods and username in actionsInstance.modUsers:
                actionsInstance.mods.remove(clientSocket)
                actionsInstance.modUsers.remove(username)

                actionsInstance.modOnline -= 1

            message = "/remove " + username
            sendInstance.broadcast(message)

            connectionInstance.clients.remove(clientSocket)
            connectionInstance.users.remove(username)

            clientSocket.close()

            self.userOnline -= 1
        except Exception as e:
            print("[Server] Failed to remove user: " + str(e))


sendInstance = Send()
securityInstance = Security()
actionsInstance = Actions()
connectionInstance = Connection()
Connection.connect(connectionInstance)
