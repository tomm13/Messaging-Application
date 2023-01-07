# 6/1/2023
# V13.3

import math
import socket
import time
import random
from threading import Thread


class Security:
    # Generates key and port, as well as encrypting and decrypting messages/ keys
    def __init__(self):
        self.d = None
        self.e = None
        self.N = None
        self.cipherKey = None
        self.encryptedCipherKey = None

    @staticmethod
    def getPort():
        return input("[Server] Failed to bind - Enter an IP to host "
                     "the server on\n")

    def generatePort(self):
        # Binds to an open port within the range 49125-65536
        while True:
            try:
                while connectionInstance.host == '127.0.0.1':
                    connectionInstance.host = self.getPort()
                connectionInstance.socket.bind((connectionInstance.host, connectionInstance.port))
                break

            except ConnectionError:
                connectionInstance.port = random.randint(49125, 65536)

            except OSError:
                connectionInstance.host = self.getPort()

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

        for prime in range(lower, upper):
            isPrime = True

            for factor in range(2, int(math.sqrt(prime) + 1)):
                if prime % factor == 0:
                    isPrime = False
                    break

            if isPrime is True:
                primes.append(prime)

        while len(str(N)) != 6:
            # Generate 2 primes P and Q where the product N is 6 digits
            P = primes[random.randint(0, len(primes) - 1)]
            Q = primes[random.randint(0, len(primes) - 1)]

            # N is the 7-12th digits of either the public or private key
            N = P * Q
            phiN = (P - 1) * (Q - 1)

        # Generate e such that e < phiN, 6 digits long, as well as coprime with phiN
        for coprime in range(100000, phiN):
            if math.gcd(coprime, phiN) == 1:
                coprimes.append(coprime)

        e = coprimes[random.randint(0, len(coprimes))]

        for k in range(1, upper ** 2):
            # Generate d such that d = e^-1 mod phiN and is 6 digits long
            if (k * phiN + 1) % e == 0:
                if (k * phiN + 1) // e != e and len(str((k * phiN + 1) // e)) == 6:
                    d = (k * phiN + 1) // e
                    break

        self.e = e
        self.d = d
        self.N = N

        self.cipherKey = random.randint(1, 26)
        self.encryptedCipherKey = self.rsaEncrypt(self.cipherKey)

        print(f"[Server] Server hosted on {str(connectionInstance.host)} on port {str(connectionInstance.port)}")
        print(f"[Server] Public key = {e}{N}")
        print(f"[Server] Private key = {d}{N}")
        print(f"[Server] Cipher key = {self.encryptedCipherKey}")

    def rsaEncrypt(self, key):
        newKey = pow(key, self.e, self.N)

        return newKey

    def rsaDecrypt(self, key):
        newKey = pow(key, self.d, self.N)

        return newKey

    def caesarEncrypt(self, message):
        newMessage = ""
        for letter in message:

            if letter.isalpha() is True:

                if letter.islower() is True:
                    step = 97

                elif letter.isupper() is True:
                    step = 65

                else:
                    raise ValueError("Invalid character")

                index = (ord(letter) + self.cipherKey - step) % 26

                newMessage += chr(index + step)

            else:
                newMessage += letter

        return newMessage

    def caesarDecrypt(self, message):
        newMessage = ""
        for letter in message:

            if letter.isalpha() is True:

                if letter.islower() is True:
                    step = 97

                elif letter.isupper() is True:
                    step = 65

                else:
                    raise ValueError("Invalid character")

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
                        if self.voteActive is False:
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
                    sendInstance.privateBroadcastDisplay(f"You need to be a mod to kick {username}", modSocket)
            else:
                sendInstance.privateBroadcastDisplay("You can't kick what doesn't exist", modSocket)

        elif message[0:5] == "/vote":
            if self.voteActive is True:
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

        if self.voteActive is True:
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
                if actionsInstance.userToKickSocket != clientSocket and actionsInstance.userToKick != username:
                    if self.modOnline == 0:
                        self.modUsers.append(username)
                        self.mods.append(clientSocket)
                        self.modOnline += 1

                        sendInstance.privateBroadcast(f"/mod {username}", clientSocket)
                        sendInstance.broadcastDisplay(f"{username} is now a mod")

                    elif modSocket in self.mods and modUsername in self.modUsers:
                        self.modUsers.append(username)
                        self.mods.append(clientSocket)
                        self.modOnline += 1

                        sendInstance.privateBroadcast(f"/mod {username}", clientSocket)
                        sendInstance.broadcastDisplay(f"{username} is now a mod")

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
        print(f"[Public] {message}")

        for client in connectionInstance.clients:
            client.send(securityInstance.caesarEncrypt(message).encode())

    @staticmethod
    def broadcastDisplay(message):
        # Sends a public animated banner with {message} parameter
        print(f"[PublicDisplay] {message}")

        for client in connectionInstance.clients:
            client.send(securityInstance.caesarEncrypt(f"/display {message}").encode())

    @staticmethod
    def privateBroadcast(message, clientSocket):
        # Send a private message to 1 specific client
        if clientSocket in connectionInstance.clients:
            print(f"[Private] {message}")

            clientSocket.send(securityInstance.caesarEncrypt(message).encode())

    @staticmethod
    def privateBroadcastDisplay(message, clientSocket):
        # Sends a private animted banner with {message} parameter
        if clientSocket in connectionInstance.clients:
            print(f"[PrivateDisplay] {message}")

            clientSocket.send(securityInstance.caesarEncrypt(f"/display {message}").encode())

    @staticmethod
    def command(message, username, clientSocket):
        # Use list to prevent doubled code
        if message == "/leave":
            connectionInstance.removeUser(username, clientSocket)
        elif message[0:4] == "/mod":
            actionsInstance.mod(message, clientSocket)
        elif message[0:5] in ["/kick", "/vote"]:
            actionsInstance.vote(message, clientSocket)
        elif message[0:6] == "/color" or message[0:7] == "/border" or message[0:9] == "/savechat":
            sendInstance.privateBroadcast(message, clientSocket)
        elif message in ["/theme", "/ldm", "/previous", "/next"]:
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

            clientSocket, Address = self.socket.accept()

            self.clients.append(clientSocket)

            username = securityInstance.caesarDecrypt(clientSocket.recv(1024).decode())

            # Criteria for a valid username: doesn't already exist, has no spaces, and is under 11 characters
            if self.validateUsername(username) is True:
                # Allows the user to join the chatroom, send and receive messages
                self.addUser(username)

                # Initialise an update thread given the username is valid
                Thread(target=self.listen, args=[username, clientSocket, True]).start()
                print(f"[Thread] Started {username}'s update thread. Username is valid")

            else:
                sendInstance.privateBroadcast("/reject", clientSocket)

                # Initialise an update thread given the username is invalid
                Thread(target=self.listen, args=[username, clientSocket, False]).start()
                print(f"[Thread] Started {username}'s update thread. Username is invalid")

    def listen(self, username, clientSocket, hasValidUsername):
        # A listening thread linked to every unique client, and detects input from them
        if hasValidUsername is False:
            while hasValidUsername is False and clientSocket in self.clients:
                try:
                    signal = securityInstance.caesarDecrypt(clientSocket.recv(1024).decode())

                    if signal:
                        if signal == "/leave":
                            # If the user quits after failing to input a valid username, remove them
                            self.removeUser(None, clientSocket)

                        if self.validateUsername(signal) is True:
                            self.addUser(signal)

                            hasValidUsername = True

                        else:
                            sendInstance.privateBroadcast("/reject", clientSocket)

                except (ConnectionResetError, OSError) as e:
                    print(f"[Thread] An error occured in {username}'s update thread before validtion completed. {e}")
                    self.removeUser(None, clientSocket)

        if clientSocket in self.clients:
            messagesSentRecently = 0
            lastMessageSentTime = 0
            warnUser = False
            detectSpam = True

            while username in self.users and clientSocket in self.clients:
                try:
                    signal = securityInstance.caesarDecrypt(clientSocket.recv(1024).decode())
                    unifiedmessage = f"{username}: {signal}"

                    if signal:
                        if signal[0] == "/":
                            sendInstance.command(signal, username, clientSocket)

                        else:
                            if detectSpam is True:
                                if messagesSentRecently >= 3:
                                    if warnUser is False:
                                        sendInstance.privateBroadcastDisplay("You are sending messages too quickly",
                                                                             clientSocket)
                                        warnUser = True

                                    if time.time() > lastMessageSentTime + 5:
                                        messagesSentRecently = 0
                                        warnUser = False

                                else:
                                    if self.validateMessageLength(unifiedmessage) is False:
                                        sendInstance.privateBroadcastDisplay("Your message is too long", clientSocket)

                                    else:
                                        sendInstance.broadcast(unifiedmessage)

                                    if lastMessageSentTime + 1 > time.time():
                                        messagesSentRecently += 1

                                    elif messagesSentRecently > 0:
                                        messagesSentRecently -= 1

                                    lastMessageSentTime = time.time()

                            else:
                                if self.validateMessageLength(unifiedmessage) is False:
                                    sendInstance.privateBroadcastDisplay("Your message is too long", clientSocket)

                                else:
                                    sendInstance.broadcast(unifiedmessage)

                except (ConnectionResetError, OSError) as e:
                    print(f"[Thread] An error occured in {username}'s update thread after validation completed. {e}")
                    self.removeUser(username, clientSocket)

        print(f"[Thread] Closed {username}'s update thread")

    def addUser(self, username):
        # Adds user to the list of users and updates everyone's user lists
        self.users.append(username)
        self.userOnline += 1

        message = "/accept "

        for user in self.users:
            message += f"{user} "

        sendInstance.broadcast(message)

    def removeUser(self, username, clientSocket):
        # Called when a user has a duplicate username or leaves
        clientSocket.close()

        if clientSocket in connectionInstance.clients:
            connectionInstance.clients.remove(clientSocket)

        if username in connectionInstance.users:
            connectionInstance.users.remove(username)
            self.userOnline -= 1

        if clientSocket in actionsInstance.mods:
            actionsInstance.mods.remove(clientSocket)

        if username in actionsInstance.modUsers:
            actionsInstance.modUsers.remove(username)
            actionsInstance.modOnline -= 1

            if actionsInstance.voteActive is True:
                actionsInstance.resetVote()

                sendInstance.broadcastDisplay("The vote has been called off as a mod has left")

        sendInstance.broadcast(f"/remove {username}")

    def validateUsername(self, username):
        # Criteria for a valid username: doesn't already exist, has no spaces, and is under 11 characters
        if username in self.users or " " in username or len(username) > 7 or len(username) < 1 or username == "None":
            return False

        else:
            return True

    @staticmethod
    def validateMessageLength(message):
        if len(message) > 50:
            return False

        else:
            return True


actionsInstance = Actions()
connectionInstance = Connection()
securityInstance = Security()
sendInstance = Send()

if __name__ == '__main__':
    connectionInstance.connect()
