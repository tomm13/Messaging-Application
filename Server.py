# 16/12/2022
# V13.2.5

import math
import socket
import time
import random
from threading import Thread


class Security:
    def __init__(self):
        self.d = None
        self.e = None
        self.N = None
        self.cipherKey = None
        self.encryptedCipherKey = None

    @staticmethod
    def generatePort():
        # Binds to an open port within the range 49125-65536
        while True:
            try:
                connectionInstance.socket.bind((connectionInstance.host, connectionInstance.port))
                break

            except ConnectionError:
                connectionInstance.port = random.randint(49125, 65536)

    def generateKey(self):
        # Uses algorithms in modular exponentiation to generate the RSA private, public
        # And cipher key
        e = 0
        d = 0
        N = 0
        P = 0
        Q = 0

        lower = 100
        upper = 9999

        primes = []
        coprimes = []

        print("[Server] Initialising generation of primes...")

        for prime in range(lower, upper):
            isPrime = True
            for factor in range(2, int(math.sqrt(prime) + 1)):
                if prime % factor == 0:
                    isPrime = False
            if isPrime:
                primes.append(prime)

        while not len(str(N)) == 6:
            # Generate 2 primes P and Q where the product N is 6 digits
            P = primes[random.randint(0, len(primes))]
            Q = primes[random.randint(0, len(primes))]

            # N is the 7-12th digits of either the public or private key
            N = P * Q
            phiN = (P - 1) * (Q - 1)

        print(f"[Server] Completed generation of primes")

        # Generate e such that e < phiN, 6 digits long, as well as coprime with phiN
        for coprime in range(100000, phiN):
            if math.gcd(coprime, phiN) == 1:
                coprimes.append(coprime)

        e = coprimes[random.randint(0, len(coprimes))]

        for k in range(1, upper ** 2):
            # Generate d such that d = e^-1 mod phiN and is 6 digits long
            if (k * phiN + 1) % e == 0:
                if not (k * phiN + 1) // e == e and len(str((k * phiN + 1) // e)) == 6:
                    d = (k * phiN + 1) // e
                    break

        self.e = e
        self.d = d
        self.N = N

        self.cipherKey = random.randint(1, 26)
        self.encryptedCipherKey = self.rsaEncrypt(self.cipherKey)

        print(f"[Server] Server hosted on {str(connectionInstance.host)} with port {str(connectionInstance.port)}")
        print(f"[Server] Public RSA key = {e}{N}")
        print(f"[Server] Private RSA key = {d}{N}")
        print(f"[Server] RSA encrypted cipher key = {self.encryptedCipherKey}")

    def rsaEncrypt(self, key):
        newKey = pow(key, self.e, self.N)

        return newKey

    def rsaDecrypt(self, key):
        newKey = pow(key, self.d, self.N)

        return newKey

    def caesarEncrypt(self, message):
        newMessage = ""
        for letter in message:

            if letter.isalpha():

                if letter.islower():
                    step = 97

                elif letter.isupper():
                    step = 65

                index = (ord(letter) + self.cipherKey - step) % 26

                newMessage += chr(index + step)

            else:
                newMessage += letter

        return newMessage

    def caesarDecrypt(self, message):
        newMessage = ""
        for letter in message:

            if letter.isalpha():

                if letter.islower():
                    step = 97

                elif letter.isupper():
                    step = 65

                index = (ord(letter) - self.cipherKey - step) % 26

                newMessage += chr(index + step)

            else:
                newMessage += letter

        return newMessage


class Actions:
    def __init__(self):
        self.voteTimeRemaining = 90
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

    def resetVote(self):
        self.voteTimeRemaining = 90
        self.userToKick = None
        self.userToKickSocket = None
        self.hasVoted = []
        self.hasVotedUsers = []
        self.voteActive = False

    def voteWaiter(self):
        # Executed in a thread, waits for a timer to end
        print("[Server] Started vote-timer thread")

        while self.voteTimeRemaining > 0:
            self.voteTimeRemaining -= 1
            time.sleep(1)

        if self.voteFor > self.voteAgainst:
            sendInstance.broadcastDisplay(f"{self.userToKick} will be kicked")
            connectionInstance.removeUser(self.userToKick, self.userToKickSocket)

        else:
            sendInstance.broadcastDisplay(f"{self.userToKick} will not be kicked")

        self.resetVote()

    def vote(self, message, clientSocket):
        # Called when a moderator is trying to kick a user, and depending on the number
        # of moderators online, the user is either kicked or a vote starts. Use /kick
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

                                Thread(target=self.voteWaiter).start()

                                sendInstance.broadcastDisplay(f"{modUsername} has started a vote to kick {username}")
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
                    sendInstance.broadcastDisplay(f"{self.userToKick} will be kicked")
                    connectionInstance.removeUser(self.userToKick, self.userToKickSocket)

                elif self.voteAgainst == self.voteTarget or self.voteFor + self.voteAgainst == self.voteTarget:
                    sendInstance.broadcastDisplay(f"{self.userToKick} will not be kicked")

                self.resetVote()

    def mod(self, message, clientSocket):
        # Called when a moderator converts other users into another moderator
        # Use /mod
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
        # Send a public message to every client
        time.sleep(0.1)
        print("[Client] " + message)

        message = securityInstance.caesarEncrypt(message)
        for client in connectionInstance.clients:
            client.send(message.encode())

    @staticmethod
    def broadcastDisplay(message):
        # Sends a public animated banner with {message} parameter
        time.sleep(0.1)
        print("[PublicDisplay] " + message)

        message = "/display " + message
        message = securityInstance.caesarEncrypt(message)

        for client in connectionInstance.clients:
            client.send(message.encode())

    @staticmethod
    def privateBroadcast(message, clientSocket):
        # Send a private message to 1 specific client
        time.sleep(0.1)
        print("[Private] " + message)

        message = securityInstance.caesarEncrypt(message)
        clientSocket.send(message.encode())

    @staticmethod
    def privateBroadcastDisplay(message, clientSocket):
        # Sends a private animted banner with {message} parameter
        time.sleep(0.1)
        print("[PrivateDisplay] " + message)

        message = "/display " + message
        message = securityInstance.caesarEncrypt(message)
        clientSocket.send(message.encode())

    @staticmethod
    def command(message, clientSocket):
        # Use list to prevent doubled code
        if message == "/online":
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
        elif message[0:5] == "/rate":
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
        self.host = socket.gethostbyname(socket.gethostname())
        self.port = random.randint(49125, 65535)
        self.userOnline = 0
        self.users = []
        self.clients = []

    def connect(self):
        securityInstance.generatePort()
        securityInstance.generateKey()

        self.socket.listen()

        while True:
            # The main thread listens for incoming connections and accepts it
            # This also broadcasts to other online users that a new user has connected.

            clientSocket, address = self.socket.accept()
            self.clients.append(clientSocket)

            username = clientSocket.recv(1024).decode()
            if username in self.users or username == "" or username == "Username" or " " in username or "[" in username\
                    or "]" in username or len(username) > 10 or username in self.users:
                sendInstance.privateBroadcast("/reject", clientSocket)
                self.clients.remove(clientSocket)

            else:
                self.users.append(username)

                message = "/accept "

                for user in self.users:
                    message += user + " "

                sendInstance.broadcast(message)

                self.userOnline += 1

                Thread(target=self.listen, args=[clientSocket]).start()

    def listen(self, clientSocket):
        # A listening thread linked to every unique client, and detects input from them
        index = self.clients.index(clientSocket)
        username = self.users[index]
        messagesSentRecently = 0
        lastMessageSentTime = time.time()
        warnUser = False

        while True:
            try:
                message = securityInstance.caesarDecrypt(clientSocket.recv(1024).decode())
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

                            if lastMessageSentTime + 1 > time.time():
                                messagesSentRecently += 1

                            elif messagesSentRecently > 0:
                                messagesSentRecently -= 1

                            lastMessageSentTime = time.time()

            except ConnectionResetError:
                self.removeUser(username, clientSocket)
                break

            except OSError:
                print("[Server] Closed a client thread")
                break

    def removeUser(self, username, clientSocket):
        # Called when a user has a duplicate username or more commonly, leaves
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


actionsInstance = Actions()
connectionInstance = Connection()
securityInstance = Security()
sendInstance = Send()

connectionInstance.connect()
