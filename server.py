# 2/4/2023
# V13.3.2

from math import sqrt, gcd
from socket import socket, gethostname, gethostbyname
from time import time
from random import randint
from threading import Thread


class Security:
    # Handles all the algorithms around ecnrypting, decrypting, and the generation of keys
    def __init__(self):
        self.d = None
        self.e = None
        self.P = None
        self.Q = None
        self.N = None
        self.cipherKey = None
        self.encryptedCipherKey = None

    def getKeys(self):
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

            for factor in range(2, int(sqrt(prime) + 1)):
                if prime % factor == 0:
                    isPrime = False
                    break

            if isPrime is True:
                primes.append(prime)

        while True:
            # Generate 2 primes P and Q where the product N is 6 digits
            P = primes[randint(0, len(primes) - 1)]
            Q = primes[randint(0, len(primes) - 1)]

            self.P = P
            self.Q = Q

            # N is the 7-12th digits of either the public or private key
            self.N = P * Q

            phiN = (P - 1) * (Q - 1)

            if len(str(self.N)) == 6:
                break

        # Generate e such that e < phiN, 6 digits long, as well as coprime with phiN
        for coprime in range(100000, phiN):
            if gcd(coprime, phiN) == 1:
                coprimes.append(coprime)

        self.e = coprimes[randint(0, len(coprimes))]

        for k in range(1, upper ** 2):
            # Generate d such that d = e^-1 mod phiN and is 6 digits long
            if (k * phiN + 1) % self.e == 0:
                if (k * phiN + 1) // self.e != self.e and len(str((k * phiN + 1) // self.e)) == 6:
                    self.d = (k * phiN + 1) // self.e
                    break

        # Generates a cipher key between 1-26, then encrypt it
        self.cipherKey = randint(1, 26)
        self.encryptedCipherKey = self.getrsaEncryptedMessage(self.cipherKey, self.e, self.N)

        print(f"[Server] Public key = {self.e}{self.N}")
        print(f"[Server] Private key = {self.d}{self.N}")
        print(f"[Server] Cipher key = {self.encryptedCipherKey}")

    @staticmethod
    def getrsaEncryptedMessage(key, e, N):
        # Used to encrypt the keys
        return pow(key, e, N)

    @staticmethod
    def getrsaDecryptedMessage(key, d, N):
        # Used to decrypt the keys
        return pow(key, d, N)

    @staticmethod
    def getCaesarEncryptedMessage(message, cipherKey):
        # Used to encrypt messages
        newMessage = ""
        for letter in message:

            if letter.isalpha() is True:

                if letter.islower() is True:
                    step = 97

                elif letter.isupper() is True:
                    step = 65

                else:
                    raise ValueError("Invalid character")

                index = (ord(letter) + cipherKey - step) % 26

                newMessage += chr(index + step)

            else:
                newMessage += letter

        return newMessage

    @staticmethod
    def getCaesarDecryptedMessage(message, cipherKey):
        # Used to decrypt messages
        newMessage = ""
        for letter in message:

            if letter.isalpha() is True:

                if letter.islower() is True:
                    step = 97

                elif letter.isupper() is True:
                    step = 65

                else:
                    raise ValueError("Invalid character")

                index = (ord(letter) - cipherKey - step) % 26

                newMessage += chr(index + step)

            else:
                newMessage += letter

        return newMessage


class Send:
    # Handles all the different ways a message can be send, such as if the message is sent
    # publicly, privately, and if the message should be displayed as an animated banner
    # Also handles commands sent by the user, using the prefix /
    @staticmethod
    def broadcast(message):
        # Send a public message to every client
        print(f"[Public] {message}")

        for client in connection.clients:
            client.send(security.getCaesarEncryptedMessage(message, security.cipherKey).encode())

    @staticmethod
    def broadcastDisplay(message):
        # Sends a public animated banner with {message} parameter
        print(f"[PublicDisplay] {message}")

        for client in connection.clients:
            client.send(
                security.getCaesarEncryptedMessage(f"/display {message}", security.cipherKey).encode())

    @staticmethod
    def privateBroadcast(message, clientSocket):
        # Send a private message to 1 specific client
        if clientSocket in connection.clients:
            print(f"[Private] {message}")

            clientSocket.send(security.getCaesarEncryptedMessage(message, security.cipherKey).encode())

    @staticmethod
    def privateBroadcastDisplay(message, clientSocket):
        # Sends a private animted banner with {message} parameter
        if clientSocket in connection.clients:
            print(f"[PrivateDisplay] {message}")

            clientSocket.send(
                security.getCaesarEncryptedMessage(f"/display {message}", security.cipherKey).
                encode())

    @staticmethod
    def getCommand(message, username, clientSocket):
        # Commands called by the prefix /
        if message == "/leave":
            connection.setRemovedUser(username, clientSocket)
        elif message[0:6] == "/color" or message[0:7] == "/border" or message[0:9] == "/savechat":
            send.privateBroadcast(message, clientSocket)
        elif message in ["/theme", "/ldm", "/previous", "/next"]:
            send.privateBroadcast(message, clientSocket)
        else:
            send.privateBroadcastDisplay("Your command is unknown", clientSocket)


class Connection:
    # Handles all the connection requests by users, and runs a thread for each user
    # The main connect() method also runs indefiitely and accepts any requests to connect
    # The connect accepts the socket connection, and a username is sent by the client.
    # A listening thread is then started for this user until they disconnect.
    # If the username sent by the client is approved (no spaces, correct length etc) then the
    # client is allowed to receive and send messages, otherwise they can only do so after
    # Inputting a valid username. If a user leaves then the server also notifies all connected users.
    def __init__(self):
        self.socket = socket()
        self.host = gethostbyname(gethostname())
        self.port = randint(49125, 65535)
        self.userOnline = 0
        self.users = []
        self.clients = []

    def bindToSocket(self):
        # Binds to an open port within the range 49125-65536
        while True:
            try:
                if self.host == '127.0.0.1' and __name__ == '__main__':
                    self.host = input("[Server] Failed to bind - Enter an IP to host the server on\n")

                self.socket.bind((self.host, self.port))

            except ConnectionError:
                self.port = randint(49125, 65536)

            except OSError:
                self.host = input("[Server] Failed to bind - Enter an IP to host the server on\n")

            else:
                print(f"[Server] Server hosted on {str(self.host)} on port {str(self.port)}")
                break

    def connect(self):
        # After binding, receive incoming requests
        self.bindToSocket()
        self.socket.listen()

        security.getKeys()

        while True:
            # The main thread listens for incoming connections and accepts it
            # This also broadcasts to other online users that a new user has connected.

            clientSocket, Address = self.socket.accept()

            self.clients.append(clientSocket)

            username = security.getCaesarDecryptedMessage(clientSocket.recv(1024).decode(),
                                                                  security.cipherKey)

            # Criteria for a valid username: doesn't already exist, has no spaces, and is under 11 characters
            if self.getUsernameValidity(username) is True:
                # Allows the user to join the chatroom, send and receive messages
                self.addUser(username)

                # Initialise an update thread given the username is valid
                Thread(target=self.listen, args=[username, clientSocket, True]).start()
                print(f"[Thread] Started {username}'s update thread. Username is valid")

            else:
                send.privateBroadcast("/reject", clientSocket)

                # Initialise an update thread given the username is invalid
                Thread(target=self.listen, args=[username, clientSocket, False]).start()
                print(f"[Thread] Started {username}'s update thread. Username is invalid")

    def listen(self, username, clientSocket, hasValidUsername):
        # A listening thread linked to every unique client, and detects input from them
        if hasValidUsername is False:
            # If the username is not valid, wait in this thread until it is
            while hasValidUsername is False and clientSocket in self.clients:
                try:
                    signal = security.getCaesarDecryptedMessage(clientSocket.recv(1024).decode(),
                                                                        security.cipherKey)

                    if signal:
                        if signal == "/leave":
                            # If the user quits after failing to input a valid username, remove them
                            self.setRemovedUser(None, clientSocket)

                        if self.getUsernameValidity(signal) is True:
                            # Allow the client to receive and accept messages
                            self.addUser(signal)

                            username = signal
                            hasValidUsername = True

                        else:
                            send.privateBroadcast("/reject", clientSocket)

                except (ConnectionResetError, OSError) as e:
                    print(f"[Thread] An error occured in {username}'s update thread before validtion completed. {e}")
                    self.setRemovedUser(None, clientSocket)

        messagesSentRecently = 0
        lastMessageSentTime = 0
        warnUser = False
        detectSpam = True

        while hasValidUsername is True and clientSocket in self.clients:
            # After having a valid username, the client can now receive and send messages
            try:
                signal = security.getCaesarDecryptedMessage(clientSocket.recv(1024).decode(),
                                                                    security.cipherKey)
                unifiedmessage = f"{username}: {signal}"

                if signal:
                    if signal[0] == "/":
                        send.getCommand(signal, username, clientSocket)

                    else:
                        if detectSpam is True:
                            if messagesSentRecently >= 3:
                                if warnUser is False:
                                    send.privateBroadcast("/timeout You are sending messages too quickly",
                                                                  clientSocket)
                                    warnUser = True

                                if time() > lastMessageSentTime + 5:
                                    messagesSentRecently = 0
                                    warnUser = False

                            else:
                                if self.getMessageLengthValidity(unifiedmessage) is False:
                                    send.privateBroadcast("/timeout Your message is too long", clientSocket)

                                else:
                                    send.broadcast(unifiedmessage)

                                if lastMessageSentTime + 1 > time():
                                    messagesSentRecently += 1

                                elif messagesSentRecently > 0:
                                    messagesSentRecently -= 1

                                lastMessageSentTime = time()

                        else:
                            if self.getMessageLengthValidity(unifiedmessage) is False:
                                send.privateBroadcast("/timeout Your meessage is too long", clientSocket)

                            else:
                                send.broadcast(unifiedmessage)

            except (ConnectionResetError, OSError) as e:
                print(f"[Thread] An error occured in {username}'s update thread after validation completed. {e}")
                self.setRemovedUser(username, clientSocket)

        print(f"[Thread] Closed {username}'s update thread")

    def addUser(self, username):
        # Adds user to the list of users and updates everyone's user lists
        self.users.append(username)
        self.userOnline += 1

        message = "/accept "

        for user in self.users:
            message += f"{user} "

        send.broadcast(message)

    def setRemovedUser(self, username, clientSocket):
        # Called when a user has a duplicate username or leaves
        clientSocket.close()

        if clientSocket in self.clients:
            self.clients.remove(clientSocket)

        if username in self.users:
            self.users.remove(username)
            self.userOnline -= 1

        send.broadcast(f"/remove {username}")

    def getUsernameValidity(self, username):
        # Criteria for a valid username: doesn't already exist, has no spaces, and is under 11 characters
        if username in self.users or " " in username or len(username) > 7 or len(username) < 1 or username == "None":
            return False

        else:
            return True

    @staticmethod
    def getMessageLengthValidity(message):
        # Prevent messages of length 50 or greater being sent
        return False if len(message) > 50 else True


if __name__ == '__main__':
    connection = Connection()
    security = Security()
    send = Send()

    connection.connect()
