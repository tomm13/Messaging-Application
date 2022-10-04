# 4/10/2022
# V13 Beta 2

import socket
import time
import random
from threading import Thread


class Security:
    def __init__(self):
        self.d = None
        self.e = None
        self.N = None

    def generateKey(self):
        N = 0
        while not len(str(N)) == 6:
            Minimum = 650
            Maximum = 1000
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

            P = PrimeCandidates[0]
            Q = PrimeCandidates[1]
            N = P * Q
            PhiN = (P - 1) * (Q - 1)

        eList = []
        for eCandidate in range(2, PhiN):
            eList.append(eCandidate)

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
                if not (k * PhiN + 1) // e == e and len(str((k * PhiN + 1) // e)) == 6:
                    d = (k * PhiN + 1) // e
                    break

        print("[Private] Private Key = " + str(d) + str(N))

        self.d = d
        self.e = e
        self.N = N

    @staticmethod
    def generatePort():
        while True:
            try:
                connectionInstance.socket.bind((connectionInstance.host, connectionInstance.port))
                print("[Server] Server Hosted on " + str(connectionInstance.host) + " with Port " +
                      str(connectionInstance.port))
                break

            except ConnectionError:
                connectionInstance.port = random.randint(49125, 65536)

    def encrypt(self, message):
        RSAEncryptedmessage = []
        for Letter in message:
            Index = ord(Letter)
            NewIndex = pow(Index, self.e, self.N)
            RSAEncryptedmessage.append(str(NewIndex))
            RSAEncryptedmessage.append(" ")

        message = str("".join(RSAEncryptedmessage))
        return message


class Actions:
    def __init__(self):
        self.modOnline = 0
        self.mods = []
        self.modUsers = []
        self.hasVoted = []
        self.hasVotedUsers = []
        self.voteTarget = 2
        self.voteFor = 0
        self.voteAgainst = 0
        self.voteActive = False
        self.userToKick = None
        self.userToKickSocket = None

    def vote(self, message, clientSocket):
        modSocket = clientSocket
        index = connectionInstance.clients.index(modSocket)
        modUsername = connectionInstance.users[index]

        if message[0:5] == "/kick":
            username = message[6:]

            if username in connectionInstance.users:
                index = connectionInstance.users.index(username)
                clientSocket = connectionInstance.clients[index]

                if modSocket in self.mods and modUsername in self.modUsers:
                    if clientSocket not in self.mods and username not in self.modUsers:
                        if not self.voteActive:
                            if self.modOnline == 1:
                                sendInstance.broadcastDisplay(modUsername + " has kicked " + username)
                                connectionInstance.removeUser(username, clientSocket)

                            else:
                                self.voteFor = 1
                                self.voteAgainst = 0
                                self.hasVoted.append(modSocket)
                                self.hasVotedUsers.append(modUsername)
                                self.userToKick = username
                                self.userToKickSocket = clientSocket
                                self.voteActive = True

                                message = modUsername + " has started a vote to kick " + username
                                sendInstance.broadcastDisplay(message)
                        else:
                            sendInstance.privateBroadcastDisplay("You cannot complete this action at this time",
                                                                 modSocket)
                    else:
                        sendInstance.privateBroadcastDisplay("You cannot kick a mod", modSocket)
                else:
                    sendInstance.privateBroadcastDisplay("You need to be a mod to kick", modSocket)
            else:
                sendInstance.privateBroadcastDisplay("You can't kick this person", modSocket)

        elif message[0:5] == "/vote":
            if self.voteActive:
                if message[6:] == "details":
                    sendInstance.privateBroadcastDisplay("Being kicked: " + self.userToKick, modSocket)

                    time.sleep(0.1)

                    if self.voteTarget - (self.voteFor + self.voteAgainst) == 1:
                        sendInstance.privateBroadcastDisplay(str(self.voteTarget - (self.voteFor + self.voteAgainst)) +
                                                             " vote needed", modSocket)
                    else:
                        sendInstance.privateBroadcastDisplay(str(self.voteTarget - (self.voteFor + self.voteAgainst)) +
                                                             " votes needed", modSocket)

                elif modSocket in self.mods and modUsername in self.modUsers:
                    if modSocket not in self.hasVoted and modUsername not in self.hasVotedUsers:
                        if message[6:] == "for":
                            self.hasVoted.append(modSocket)
                            self.hasVotedUsers.append(modUsername)
                            self.voteFor += 1

                        elif message[6:] == "against":
                            self.hasVoted.append(modSocket)
                            self.hasVotedUsers.append(modUsername)
                            self.voteAgainst += 1

                        else:
                            sendInstance.privateBroadcastDisplay("Your vote argument is unknown", modSocket)
                    else:
                        sendInstance.privateBroadcastDisplay("You have already cast your vote", modSocket)
                else:
                    sendInstance.privateBroadcastDisplay("You need to be a mod to vote", modSocket)
            else:
                sendInstance.privateBroadcastDisplay("You cannot do this as there is no ongoing vote", modSocket)

        if self.voteActive:
            if self.voteFor == self.voteTarget or self.voteAgainst == self.voteTarget or self.voteFor + \
                    self.voteAgainst == self.voteTarget:

                if self.voteFor == self.voteTarget:
                    sendInstance.broadcastDisplay(self.userToKick + " will be kicked")
                    connectionInstance.removeUser(self.userToKick, self.userToKickSocket)

                elif self.voteAgainst == self.voteTarget or self.voteFor + self.voteAgainst == self.voteTarget:
                    sendInstance.broadcastDisplay(self.userToKick + " will not be kicked")

                self.resetVote()

    def resetVote(self):
        self.userToKick = None
        self.userToKickSocket = None
        self.hasVoted = []
        self.hasVotedUsers = []
        self.voteActive = False

    def mod(self, message, clientSocket):
        modSocket = clientSocket
        index = connectionInstance.clients.index(modSocket)
        modUsername = connectionInstance.users[index]

        username = message[5:]

        if username in connectionInstance.users:
            index = connectionInstance.users.index(username)
            clientSocket = connectionInstance.clients[index]

            if clientSocket not in self.mods and username not in self.modUsers:
                if not actionsInstance.userToKickSocket == clientSocket and not actionsInstance.userToKick == username:
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
                    sendInstance.privateBroadcastDisplay("You cannot mod this person as they are under review",
                                                         modSocket)
            else:
                sendInstance.privateBroadcastDisplay("You are already a mod", modSocket)
        else:
            sendInstance.privateBroadcastDisplay("You cannot mod this person", modSocket)


class Send:
    @staticmethod
    def broadcast(message):
        # Send a public message to every client, not for animating purposes.
        time.sleep(0.1)
        print("[Client] " + message)

        message = securityInstance.encrypt(message)
        for client in connectionInstance.clients:
            client.send(message.encode())

    @staticmethod
    def broadcastDisplay(message):
        # Send "/display" + a message to every client.
        time.sleep(0.1)
        print("[PublicDisplay] " + message)

        message = "/display " + message
        message = securityInstance.encrypt(message)

        for client in connectionInstance.clients:
            client.send(message.encode())

    @staticmethod
    def privateBroadcast(message, clientSocket):
        # Send a private message to 1 specific client, not for animating purposes.
        time.sleep(0.1)
        print("[Private] " + message)

        message = securityInstance.encrypt(message)
        clientSocket.send(message.encode())

    @staticmethod
    def privateBroadcastDisplay(message, clientSocket):
        # Send "/display" + a message to 1 specific client.
        time.sleep(0.1)
        print("[PrivateDisplay] " + message)

        message = "/display " + message
        message = securityInstance.encrypt(message)
        clientSocket.send(message.encode())

    @staticmethod
    def command(message, clientSocket):
        # Use list to prevent doubled code
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
            sendInstance.privateBroadcastDisplay(str(securityInstance.d) + str(securityInstance.N), clientSocket)
        elif message == "/theme":
            sendInstance.privateBroadcast(message, clientSocket)
        elif message[0:6] == "/color":
            sendInstance.privateBroadcast(message, clientSocket)
        elif message[0:9] == "/savechat":
            sendInstance.privateBroadcast(message, clientSocket)
        elif message[0:4] == "/mod":
            actionsInstance.mod(message, clientSocket)
        elif message[0:5] == "/kick" or message[0:5] == "/vote":
            actionsInstance.vote(message, clientSocket)
        elif message == "/filler":
            sendInstance.privateBroadcast(message, clientSocket)
        elif message[0:5] == "/rate":
            sendInstance.privateBroadcast(message, clientSocket)
        elif message[0:13] == "/savesettings":
            sendInstance.privateBroadcast(message, clientSocket)
        elif message[0:13] == "/loadsettings":
            sendInstance.privateBroadcast(message, clientSocket)
        elif message[0:7] == "/border":
            sendInstance.privateBroadcast(message, clientSocket)
        elif message == "/previous":
            sendInstance.privateBroadcast(message, clientSocket)
        elif message == "/next":
            sendInstance.privateBroadcast(message, clientSocket)
        elif message == "/ldm":
            sendInstance.privateBroadcast(message, clientSocket)
        else:
            sendInstance.privateBroadcastDisplay("Your command is unknown", clientSocket)


class Connection:
    def __init__(self):
        self.socket = socket.socket()
        self.host = "10.28.205.230"
        self.port = random.randint(49125, 65535)
        self.userOnline = 0
        self.spaceRemaining = 50
        self.users = []
        self.clients = []
        self.recentMessages = []

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

            elif len(username) > 10:
                sendInstance.privateBroadcast("/disconnect", clientSocket)
                self.clients.remove(clientSocket)

            else:
                self.users.append(username)

                message = "/add " + " ".join(self.users)
                sendInstance.broadcast(message)

                self.userOnline += 1
                self.spaceRemaining -= 1

                if len(self.recentMessages) > 0:
                    for message in self.recentMessages:
                        sendInstance.privateBroadcast(message, clientSocket)

                listeningThread = Thread(target=self.listen, args=[clientSocket])
                listeningThread.start()

    def listen(self, clientSocket):
        index = self.clients.index(clientSocket)
        username = self.users[index]
        messagesSentRecently = 0
        lastMessageSentTime = time.time()
        warnUser = False
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
                        if messagesSentRecently >= 3:
                            if not warnUser:
                                sendInstance.privateBroadcastDisplay("You are sending messages too quickly",
                                                                     clientSocket)
                                warnUser = True

                            if time.time() > lastMessageSentTime + 5:
                                messagesSentRecently = 0
                                warnUser = False

                        else:
                            sendInstance.broadcast(unifiedmessage)
                            self.recentMessages.append(unifiedmessage)

                            if lastMessageSentTime + 1 > time.time():
                                messagesSentRecently += 1

                            elif messagesSentRecently > 0:
                                messagesSentRecently -= 1

                            if len(self.recentMessages) > 15:
                                self.recentMessages = self.recentMessages[1:]

                            lastMessageSentTime = time.time()

            except ConnectionResetError:
                self.removeUser(username, clientSocket)
                break

            except OSError:
                print("[Server] Closed a client thread")
                break

    def removeUser(self, username, clientSocket):
        connectionInstance.clients.remove(clientSocket)
        connectionInstance.users.remove(username)

        clientSocket.close()

        self.userOnline -= 1

        if clientSocket in actionsInstance.mods and username in actionsInstance.modUsers:
            actionsInstance.mods.remove(clientSocket)
            actionsInstance.modUsers.remove(username)
            actionsInstance.modOnline -= 1

            if actionsInstance.voteActive:
                actionsInstance.resetVote()

                sendInstance.broadcastDisplay("The vote has been called off as a mod has left")

        message = "/remove " + username
        sendInstance.broadcast(message)


sendInstance = Send()
securityInstance = Security()
actionsInstance = Actions()
connectionInstance = Connection()
Connection.connect(connectionInstance)
