# 16/12/2022
# V13.2.5

import platform
import socket
import colorutils
import sys
from time import sleep, localtime, strftime, time
from threading import Thread
from guizero import *


class Animation:
    # Creates a class with animation methods and a thread method
    def __init__(self):
        self.queue = []
        self.readRate = 1
        self.waitMultiplier = 1

    def animateHeader(self, message):
        # Code 1

        if not uiInstance.darkMode:
            (R, G, B) = (255, 255, 255)

            while not R == uiInstance.animationColor[0] or not G == uiInstance.animationColor[1] \
                    or not B == uiInstance.animationColor[2]:
                # Text fades from white to color
                if R < uiInstance.animationColor[0]:
                    R += 1
                if G < uiInstance.animationColor[1]:
                    G += 1
                if B < uiInstance.animationColor[2]:
                    B += 1
                if R > uiInstance.animationColor[0]:
                    R -= 1
                if G > uiInstance.animationColor[1]:
                    G -= 1
                if B > uiInstance.animationColor[2]:
                    B -= 1

                uiInstance.header.text_color = (R, G, B)
                sleep(uiInstance.rate)

            uiInstance.header.value = message

            while not R == 255 or not G == 255 or not B == 255:
                # Fades background from color to white
                if R < 255:
                    R += 1
                if G < 255:
                    G += 1
                if B < 255:
                    B += 1
                if R > 255:
                    R -= 1
                if G > 255:
                    G -= 1
                if B > 255:
                    B -= 1

                uiInstance.header.bg = (R, G, B)
                sleep(uiInstance.rate)

            sleep(self.readRate * self.waitMultiplier)

            while not R == uiInstance.animationColor[0] or not G == uiInstance.animationColor[1] \
                    or not B == uiInstance.animationColor[2]:
                # Fades background from white to color
                if R < uiInstance.animationColor[0]:
                    R += 1
                if G < uiInstance.animationColor[1]:
                    G += 1
                if B < uiInstance.animationColor[2]:
                    B += 1
                if R > uiInstance.animationColor[0]:
                    R -= 1
                if G > uiInstance.animationColor[1]:
                    G -= 1
                if B > uiInstance.animationColor[2]:
                    B -= 1

                uiInstance.header.bg = (R, G, B)
                sleep(uiInstance.rate)

            uiInstance.header.value = "Welcome " + connectionInstance.username

            while not R == 255 or not G == 255 or not B == 255:
                # Text fades from white to black
                if R < 255:
                    R += 1
                if G < 255:
                    G += 1
                if B < 255:
                    B += 1
                if R > 255:
                    R -= 1
                if G > 255:
                    G -= 1
                if B > 255:
                    B -= 1

                uiInstance.header.text_color = (R, G, B)
                sleep(uiInstance.rate)

        else:
            (R, G, B) = uiInstance.darkbg

            while not R == uiInstance.animationColor[0] or not G == uiInstance.animationColor[1] \
                    or not B == uiInstance.animationColor[2]:
                # Text fades from black to color
                if R < uiInstance.animationColor[0]:
                    R += 1
                if G < uiInstance.animationColor[1]:
                    G += 1
                if B < uiInstance.animationColor[2]:
                    B += 1
                if R > uiInstance.animationColor[0]:
                    R -= 1
                if G > uiInstance.animationColor[1]:
                    G -= 1
                if B > uiInstance.animationColor[2]:
                    B -= 1

                uiInstance.header.text_color = (R, G, B)
                sleep(uiInstance.rate)

            uiInstance.header.value = message

            while not R == uiInstance.darkbg[0] or not G == uiInstance.darkbg[1] or not B == uiInstance.darkbg[2]:
                # Fades background from color to black
                if R < uiInstance.darkbg[0]:
                    R += 1
                if G < uiInstance.darkbg[1]:
                    G += 1
                if B < uiInstance.darkbg[2]:
                    B += 1
                if R > uiInstance.darkbg[0]:
                    R -= 1
                if G > uiInstance.darkbg[1]:
                    G -= 1
                if B > uiInstance.darkbg[2]:
                    B -= 1

                uiInstance.header.bg = (R, G, B)
                sleep(uiInstance.rate)

            sleep(self.readRate * self.waitMultiplier)

            while not R == uiInstance.animationColor[0] or not G == uiInstance.animationColor[1] \
                    or not B == uiInstance.animationColor[2]:
                # Fades background from black to color
                if R > uiInstance.animationColor[0]:
                    R -= 1
                if G > uiInstance.animationColor[1]:
                    G -= 1
                if B > uiInstance.animationColor[2]:
                    B -= 1
                if R < uiInstance.animationColor[0]:
                    R += 1
                if G < uiInstance.animationColor[1]:
                    G += 1
                if B < uiInstance.animationColor[2]:
                    B += 1

                uiInstance.header.bg = (R, G, B)
                sleep(uiInstance.rate)

            uiInstance.header.value = f"Welcome {connectionInstance.username}"

            while not R == uiInstance.darkbg[0] or not G == uiInstance.darkbg[1] or not B == uiInstance.darkbg[2]:
                # Text fades from any color to black
                if R < uiInstance.darkbg[0]:
                    R += 1
                if G < uiInstance.darkbg[1]:
                    G += 1
                if B < uiInstance.darkbg[2]:
                    B += 1
                if R > uiInstance.darkbg[0]:
                    R -= 1
                if G > uiInstance.darkbg[1]:
                    G -= 1
                if B > uiInstance.darkbg[2]:
                    B -= 1

                uiInstance.header.text_color = (R, G, B)
                sleep(uiInstance.rate)

    @staticmethod
    def switchTheme():
        # Code 2
        if uiInstance.darkMode:
            while uiInstance.darkMode:
                # To turn Dark Mode off
                (R, G, B) = (70, 70, 70)

                while not (R, G, B) == (255, 255, 255):
                    R += 1
                    G += 1
                    B += 1

                    uiInstance.header.text_color = (R, G, B)
                    uiInstance.chatHistory.bg = (R, G, B)
                    uiInstance.messageInput.bg = (R, G, B)
                    uiInstance.userList.bg = (R, G, B)
                    sleep(uiInstance.rate)

                uiInstance.darkMode = False

        else:
            while not uiInstance.darkMode:
                # To turn Dark Mode on
                (R, G, B) = (255, 255, 255)

                while not (R, G, B) == uiInstance.darkbg:
                    R -= 1
                    G -= 1
                    B -= 1

                    uiInstance.header.text_color = (R, G, B)
                    uiInstance.chatHistory.bg = (R, G, B)
                    uiInstance.messageInput.bg = (R, G, B)
                    uiInstance.userList.bg = (R, G, B)
                    sleep(uiInstance.rate)

                uiInstance.darkMode = True

        return

    @staticmethod
    def fadeColor(newColor):
        # Code 3

        (R, G, B) = uiInstance.color

        while not R == newColor[0] or not G == newColor[1] or not B == newColor[2]:
            if R > newColor[0]:
                R -= 1
            if G > newColor[1]:
                G -= 1
            if B > newColor[2]:
                B -= 1
            if R < newColor[0]:
                R += 1
            if G < newColor[1]:
                G += 1
            if B < newColor[2]:
                B += 1

            if connectionInstance.connected:
                uiInstance.userList.text_color = (R, G, B)
                uiInstance.chatHistory.text_color = (R, G, B)
                uiInstance.messageInput.text_color = (R, G, B)

            else:
                uiInstance.connectText.text_color = (R, G, B)

            sleep(uiInstance.rate)

        uiInstance.color = newColor

    @staticmethod
    def fadeBorder(newColor):
        # Code 4

        (R, G, B) = uiInstance.animationColor

        while not (R, G, B) == newColor:
            if R < newColor[0]:
                R += 1
            if G < newColor[1]:
                G += 1
            if B < newColor[2]:
                B += 1
            if R > newColor[0]:
                R -= 1
            if G > newColor[1]:
                G -= 1
            if B > newColor[2]:
                B -= 1

            if connectionInstance.connected:
                uiInstance.header.bg = (R, G, B)
                uiInstance.chatHistoryTopBorder.bg = (R, G, B)
                uiInstance.chatHistoryRightBorder.bg = (R, G, B)
                uiInstance.chatHistoryBottomBorder.bg = (R, G, B)
                uiInstance.chatHistoryLeftBorder.bg = (R, G, B)
                uiInstance.userListTopBorder.bg = (R, G, B)
                uiInstance.userListRightBorder.bg = (R, G, B)
                uiInstance.userListBottomBorder.bg = (R, G, B)
                uiInstance.userListLeftBorder.bg = (R, G, B)
                uiInstance.messageInputTopBorder.bg = (R, G, B)
                uiInstance.messageInputRightBorder.bg = (R, G, B)
                uiInstance.messageInputBottomBorder.bg = (R, G, B)
                uiInstance.messageInputLeftBorder.bg = (R, G, B)

            else:
                uiInstance.status.bg = (R, G, B)

            sleep(uiInstance.rate)

        uiInstance.animationColor = newColor

    @staticmethod
    def animateStatus(message):
        # Code 5
        (R, G, B) = (255, 255, 255)

        while not R == uiInstance.animationColor[0] or not G == uiInstance.animationColor[1] \
                or not B == uiInstance.animationColor[2]:
            # Text fades from white to color
            if R < uiInstance.animationColor[0]:
                R += 1
            if G < uiInstance.animationColor[1]:
                G += 1
            if B < uiInstance.animationColor[2]:
                B += 1
            if R > uiInstance.animationColor[0]:
                R -= 1
            if G > uiInstance.animationColor[1]:
                G -= 1
            if B > uiInstance.animationColor[2]:
                B -= 1

            uiInstance.status.text_color = (R, G, B)
            sleep(uiInstance.rate)

        uiInstance.status.value = message

        while not R == 255 or not G == 255 or not B == 255:
            # Text fades from white to black
            if R < 255:
                R += 1
            if G < 255:
                G += 1
            if B < 255:
                B += 1
            if R > 255:
                R -= 1
            if G > 255:
                G -= 1
            if B > 255:
                B -= 1

            uiInstance.status.text_color = (R, G, B)
            sleep(uiInstance.rate)

    @staticmethod
    def fadeIndicator(key, newColor):
        # Code 6

        if key == 0:
            (R, G, B) = colorutils.web_to_rgb(uiInstance.usernameIndicator.bg)

        elif key == 1:
            (R, G, B) = colorutils.web_to_rgb(uiInstance.colorIndicator.bg)

        elif key == 2:
            (R, G, B) = colorutils.web_to_rgb(uiInstance.hostIndicator.bg)

        elif key == 3:
            (R, G, B) = colorutils.web_to_rgb(uiInstance.portIndicator.bg)

        elif key == 4:
            (R, G, B) = colorutils.web_to_rgb(uiInstance.publicKeyIndicator.bg)

        elif key == 5:
            (R, G, B) = colorutils.web_to_rgb(uiInstance.privateKeyIndicator.bg)

        elif key == 6:
            (R, G, B) = colorutils.web_to_rgb(uiInstance.cipherKeyIndicator.bg)

        while not (R, G, B) == newColor:
            if R < newColor[0]:
                R += 1
            if G < newColor[1]:
                G += 1
            if B < newColor[2]:
                B += 1
            if R > newColor[0]:
                R -= 1
            if G > newColor[1]:
                G -= 1
            if B > newColor[2]:
                B -= 1

            if key == 0:
                uiInstance.usernameIndicator.bg = (R, G, B)

            elif key == 1:
                uiInstance.colorIndicator.bg = (R, G, B)

            elif key == 2:
                uiInstance.hostIndicator.bg = (R, G, B)

            elif key == 3:
                uiInstance.portIndicator.bg = (R, G, B)

            elif key == 4:
                uiInstance.publicKeyIndicator.bg = (R, G, B)

            elif key == 5:
                uiInstance.privateKeyIndicator.bg = (R, G, B)

            elif key == 6:
                uiInstance.cipherKeyIndicator.bg = (R, G, B)

            sleep(uiInstance.rate)

    def animationThread(self):
        # This is the new thread in place of the hundreds of unterminated threads called before
        # The format for this thread is [[Class animation method code, *args]]
        print(f"Started animation thread at {str(time())}")
        while True:
            if self.queue:
                print(self.queue)
                # Check if queue has duplicate items
                while len(self.queue) > 1 and self.queue[0] == self.queue[1]:
                    self.queue.pop(1)

                if self.queue[0][0] == 1:
                    if not uiInstance.LDM:
                        if len(str(self.queue[0][0])) < 10:
                            self.waitMultiplier = 2.0
                        elif len(str(self.queue[0][0])) < 15:
                            self.waitMultiplier = 2.5
                        else:
                            self.waitMultiplier = 3.0

                        self.animateHeader(self.queue[0][1])

                    else:
                        communicationInstance.addMessage(self.queue[0][1])

                elif self.queue[0][0] == 2:
                    if (uiInstance.darkMode and uiInstance.color == (255, 255, 255)) \
                            or (uiInstance.darkMode and uiInstance.animationColor == (255, 255, 255)) \
                            or (not uiInstance.darkMode and uiInstance.color == (0, 0, 0)) \
                            or (not uiInstance.darkMode and uiInstance.animationColor == (0, 0, 0)):

                        self.queue.append([1, "You cannot change the theme due to contrast"])

                    else:
                        self.switchTheme()

                elif self.queue[0][0] == 3:
                    self.fadeColor(self.queue[0][1])

                elif self.queue[0][0] == 4:
                    self.fadeBorder(self.queue[0][1])

                elif self.queue[0][0] == 5:
                    if len(str(self.queue[0][0])) < 10:
                        self.waitMultiplier = 2.0
                    elif len(str(self.queue[0][0])) < 15:
                        self.waitMultiplier = 2.5
                    else:
                        self.waitMultiplier = 3.0

                    self.animateStatus(self.queue[0][1])

                elif self.queue[0][0] == 6:
                    if not connectionInstance.connected:
                        self.fadeIndicator(self.queue[0][1], self.queue[0][2])

                self.queue.pop(0)


class Communication:
    def __init__(self):
        self.warningTimer = None
        self.messageTooLongWarning = False
        self.users = []
        self.chatHistory = []
        self.transcript = [[]]
        self.page = 0

    @staticmethod
    def rsaEncrypt(key):
        rsaKey = pow(key, connectionInstance.e, connectionInstance.N)

        return rsaKey

    @staticmethod
    def rsaDecrypt(key):
        newKey = pow(key, connectionInstance.d, connectionInstance.N)

        return newKey

    @staticmethod
    def caesarEncrypt(message):
        newMessage = ""
        for letter in message:

            if letter.isalpha():

                if letter.islower():
                    step = 97

                elif letter.isupper():
                    step = 65

                index = (ord(letter) + connectionInstance.cipherKey - step) % 26

                newMessage += chr(index + step)

            else:
                newMessage += letter

        return newMessage

    @staticmethod
    def caesarDecrypt(message):
        newMessage = ""
        for letter in message:

            if letter.isalpha():

                if letter.islower():
                    step = 97

                elif letter.isupper():
                    step = 65

                index = (ord(letter) - connectionInstance.cipherKey - step) % 26

                newMessage += chr(index + step)

            else:
                newMessage += letter

        return newMessage

    @staticmethod
    def saveChatHistory(location):
        # Called by /savechat [Location]
        if location and " " not in location:
            with open(location, "w") as file:
                for chatLine in communicationInstance.chatHistory:
                    file.write(chatLine + "\n")
                file.close()

                animationInstance.queue.append([1, f"Your file has been saved in {str(location)}"])

        else:
            animationInstance.queue.append([1, "You can't save to this location"])

    @staticmethod
    def disconnectLoop():
        # Called by using an existing username when connecting
        uiInstance.animationColor = (255, 0, 0)

        while True:
            animationInstance.queue.append([1, "You cannot use this username, "
                                               "please rejoin under a different username"])
            sleep(1)

    def sendToServer(self):
        # Gets the value of the input, encrypts, then broadcasts
        try:
            message = uiInstance.messageInput.value
            if message:
                if message == "/leave":
                    connectionInstance.leave()
                else:
                    if len(message) + len(connectionInstance.username) + 2 >= 45:
                        if not self.messageTooLongWarning:
                            animationInstance.queue.append([1, "Your message is too long"])
                            self.messageTooLongWarning = True
                            self.warningTimer = time()

                        else:
                            if time() > self.warningTimer + 5:
                                self.messageTooLongWarning = False

                    else:
                        connectionInstance.socket.send(self.caesarEncrypt(message).encode())
                        uiInstance.messageInput.clear()

        except BrokenPipeError:
            connectionInstance.connected = False
            connectionInstance.leave()

    def setUsers(self, message):
        # Called by /add [Users spilt by space]
        message = message.split()
        message.sort()

        uiInstance.userList.clear()
        uiInstance.userList.append("Users online:")

        for user in message:
            if user not in self.users:
                uiInstance.userList.append(user)
                self.users.append(user)

                message = f"{str(user)} has connected"
                animationInstance.queue.append([1, message])
                print(f"Appended /add user at {str(time())}")

            else:
                uiInstance.userList.append(user)

    def removeUsers(self, message):
        # Called by /remove [Users split by space]
        if message == connectionInstance.username:
            while True:
                uiInstance.animationColor = (255, 0, 0)
                animationInstance.queue.append([1, "You have been kicked / disconnected"])
                sleep(1)

        uiInstance.userList.remove(message[8:])
        self.users.remove(message[8:])
        animationInstance.queue.append([1, f"{message[8:]} has disconnected"])

    def previousPage(self):
        # Called by /previous
        if self.page > 0:
            self.page -= 1

            uiInstance.chatHistory.clear()
            uiInstance.chatHistory.value = self.transcript[self.page][0]

            for line in self.transcript[self.page][1:]:
                uiInstance.chatHistory.append(line)

            if not uiInstance.LDM:
                animationInstance.queue.append([1, f"You are on page {str(self.page + 1)} of {str(uiInstance.page + 1)}"
                                                ])
        else:
            animationInstance.queue.append([1, "You cannot go below this page"])

    def nextPage(self):
        # Called by /next
        if self.page < uiInstance.page:
            self.page += 1

            uiInstance.chatHistory.clear()
            uiInstance.chatHistory.value = self.transcript[self.page][0]

            for line in self.transcript[self.page][1:]:
                uiInstance.chatHistory.append(line)

            if not uiInstance.LDM:
                animationInstance.queue.append([1, f"You are on page {str(self.page + 1)} of {str(uiInstance.page + 1)}"
                                                ])
        else:
            animationInstance.queue.append([1, "You are at the highest page"])

    def createNewPage(self, message):
        # Sends the client to the new current page and shows input
        self.transcript.append([message])
        self.page = uiInstance.page + 1
        uiInstance.chatHistory.clear()
        uiInstance.chatHistory.value = message
        uiInstance.page += 1
        uiInstance.linesSent = 1

    def addMessage(self, message):
        # Called when the message is not a command
        if uiInstance.linesSent >= uiInstance.linesLimit:
            self.createNewPage(message)

        else:
            # Received input
            self.chatHistory.append(strftime("%H:%M:%S", localtime()) + f" {message}")
            if uiInstance.linesSent == 0:
                # Only true for the very first message
                self.transcript[uiInstance.page].append(message)
                uiInstance.chatHistory.value = message
                uiInstance.linesSent += 1

            else:
                if self.page == uiInstance.page:
                    # If you are viewing the current page then
                    self.transcript[uiInstance.page].append(message)
                    uiInstance.chatHistory.append(message)
                    uiInstance.linesSent += 1

                else:
                    # If you are viewing an older page then load current page then show input
                    self.page = uiInstance.page
                    uiInstance.chatHistory.clear()
                    uiInstance.chatHistory.value = self.transcript[self.page][0]
                    uiInstance.linesSent = 1

                    for line in self.transcript[self.page][1:]:
                        uiInstance.chatHistory.append(line)
                        uiInstance.linesSent += 1

                    if uiInstance.linesSent >= uiInstance.linesLimit:
                        # If the current page has no space left
                        self.createNewPage(message)

                    else:
                        self.transcript[uiInstance.page].append(message)
                        uiInstance.chatHistory.append(message)
                        uiInstance.linesSent += 1

    def updateThread(self):
        # Starts when the user is connected
        # Looks out for server broadcasts
        try:
            print(f"Started update thread at {str(time())}")
            while connectionInstance.connected:
                message = self.caesarDecrypt(connectionInstance.socket.recv(1024).decode())

                if message:
                    print(f"Received message: {message}")

                    if message[0:8] == "/display":
                        animationInstance.queue.append([1, message[9:]])

                    elif message == "/theme":
                        animationInstance.queue.append([2])

                    elif message[0:9] == "/savechat":
                        communicationInstance.saveChatHistory(message[10:])

                    elif message == "/ldm":
                        uiInstance.setLDM()

                    elif message[0:4] == "/mod":
                        uiInstance.setMod(message[5:])

                    elif message[0:5] == "/rate":
                        uiInstance.setRate(message[6:])

                    elif message[0:6] == "/color":
                        uiInstance.chooseColor(3, message[7:])

                    elif message[0:7] == "/border":
                        uiInstance.chooseColor(4, message[8:])

                    elif message[0:4] == "/add":
                        self.setUsers(message[5:])

                    elif message[0:7] == "/remove":
                        self.removeUsers(message[8:])

                    elif message == "/next":
                        self.nextPage()

                    elif message == "/previous":
                        self.previousPage()

                    elif message == "/disconnect":
                        self.disconnectLoop()

                    else:
                        self.addMessage(message)

        except ConnectionResetError:
            connectionInstance.connected = False
            connectionInstance.leave()
            print("Closed thread successfully")

        finally:
            return


class Connection:
    def __init__(self):
        # Inputs
        self.username = None
        self.color = None
        self.host = None
        self.port = None
        self.privateKey = None
        self.publicKey = None
        self.cipherKey = None

        # Attributes
        self.encryptedCipherKey = None
        self.e = None
        self.d = None
        self.N = None
        self.socket = socket.socket()
        self.connected = False
        self.mod = False
        self.inputRequest = 0

        # Input booleans
        self.hasUsername = False
        self.hasColor = False
        self.hasHost = False
        self.hasPort = False
        self.hasPublicKey = False
        self.hasPrivateKey = False
        self.hasCipherKey = False

        # Input booleans in list
        self.hasInputs = [self.hasUsername, self.hasColor, self.hasHost, self.hasPort, self.hasPublicKey,
                          self.hasPrivateKey, self.hasCipherKey]

    def connect(self):
        # Called when the user has filled out all 7 inputs
        # Connects to the socket, calculates the RSA encryption key, decryption key, and
        # The cipher key.
        self.e = int(str(self.publicKey[0:6]), base=10)
        self.d = int(str(self.privateKey[0:6]), base=10)
        self.N = int(str(self.privateKey[6:12]), base=10)
        self.cipherKey = communicationInstance.rsaDecrypt(int(self.encryptedCipherKey, base=10))

        try:
            self.socket.connect((self.host, int(self.port, base=10)))
            self.socket.send(self.username.encode())
            self.connected = True

            uiInstance.color = connectionInstance.color
            uiInstance.openChat()

        except ConnectionRefusedError:
            animationInstance.queue.append([1, "Connection refused"])

        except OSError:
            connectionInstance.leave()

    def leave(self):
        if connectionInstance.connected:
            self.socket.send("/leave".encode())
            self.connected = False

            uiInstance.chatWindow.hide()

        uiInstance.setupWindow.hide()

        self.socket.close()
        sys.exit("You have disconnected")


class UI:
    def __init__(self):
        # UI elements (setup)
        self.setupWindow = None
        self.inputTextBox = None
        self.status = None
        self.connectText = None
        self.usernameIndicator = None
        self.colorIndicator = None
        self.hostIndicator = None
        self.portIndicator = None
        self.publicKeyIndicator = None
        self.privateKeyIndicator = None
        self.cipherKeyIndicator = None

        # UI elements (chatWindow)
        self.chatWindow = None
        self.header = None
        self.border = None
        self.userList = None
        self.chatHistory = None
        self.messageInput = None

        # UI Borders (chatWindow)
        self.userListTopBorder = None
        self.userListRightBorder = None
        self.userListBottomBorder = None
        self.userListLeftBorder = None
        self.chatHistoryTopBorder = None
        self.chatHistoryRightBorder = None
        self.chatHistoryBottomBorder = None
        self.chatHistoryLeftBorder = None
        self.messageInputTopBorder = None
        self.messageInputRightBorder = None
        self.messageInputBottomBorder = None
        self.messageInputLeftBorder = None

        # Attributes
        self.font = "San Francisco"
        self.color = (173, 216, 230)
        self.animationColor = (173, 216, 230)
        self.bg = (70, 70, 70)
        self.darkbg = (40, 40, 40)
        self.waitTime = 1
        self.linesSent = 0
        self.darkMode = False
        self.LDM = False
        self.hasRequestedInput = False
        self.page = 0

        # Method list
        self.getInputs = [self.getUsername, self.getColor, self.getHost, self.getPort, self.getPublicKey,
                          self.getPrivateKey, self.getCipherKey]

        if platform.system() == "Darwin":
            self.fontSize = 22
            self.rate = 0.00035
            self.linesLimit = 13
        elif platform.system() == "Windows":
            self.fontSize = 18
            self.rate = 0.00000
            self.linesLimit = 9
        else:
            self.fontSize = 12
            self.rate = 0.00000
            self.linesLimit = 13

    # Methods below alter UI attributes

    @staticmethod
    def chooseColor(code, message):
        # Called by /color [Color]
        try:
            color = colorutils.web_to_rgb(message)

            if (uiInstance.darkMode and color == (0, 0, 0)) or (
                    not uiInstance.darkMode and color == (255, 255, 255)):
                animationInstance.queue.append([1, "You cannot do this due to contrast"])

            else:
                animationInstance.queue.append([code, color])

        except ValueError:
            animationInstance.queue.append([1, "You cannot use this color as it is undefined"])

    @staticmethod
    def setMod(message):
        # Called by /mod [User]
        if message == connectionInstance.username and not connectionInstance.mod:
            if not uiInstance.darkMode:
                animationInstance.queue.append([2, False])

            connectionInstance.mod = True

            uiInstance.chooseColor(3, "khaki")
            uiInstance.chooseColor(4, "khaki")

    @staticmethod
    def setRate(rate):
        # Called by /rate [Rate]
        try:
            rate = float(rate)
            if 0 < rate < 3:
                animationInstance.readRate = rate
                animationInstance.queue.append(
                    [1, f"You changed the animation hold to {str(animationInstance.readRate)}"])

            else:
                animationInstance.queue.append([1, "You can only use a rate value between 0-3"])

        except ValueError:
            animationInstance.queue.append([1, "You cannot use this value"])

    @staticmethod
    def setLDM():
        # Called by /ldm
        if uiInstance.LDM:
            uiInstance.LDM = False
            animationInstance.queue.append([1, "You turned LDM off"])

        else:
            uiInstance.LDM = True
            animationInstance.queue.append([1, "You turned LDM on"])

    # The next 7 methods request for user inputs prior to connecting

    def getUsername(self, key):
        if not self.hasRequestedInput or not key:
            animationInstance.queue.append([5, "Choose a username"])

            self.hasRequestedInput = True

        else:
            if "Username" == uiInstance.inputTextBox.value or " " in uiInstance.inputTextBox.value or \
                    "[" in uiInstance.inputTextBox.value or "]" in uiInstance.inputTextBox.value or \
                    not uiInstance.inputTextBox.value:
                # Checks: if username is not empty, not Username and does not contain spaces or [ and ]
                animationInstance.queue.append([5, "Try a different username"])

            else:
                connectionInstance.username = uiInstance.inputTextBox.value
                connectionInstance.inputRequest += 1

                connectionInstance.hasUsername = True
                connectionInstance.hasInputs[0] = True
                self.hasRequestedInput = False

        uiInstance.inputTextBox.clear()

    def getColor(self, key):
        if not self.hasRequestedInput or not key:
            animationInstance.queue.append([5, f"{connectionInstance.username}, choose a color"])

            self.hasRequestedInput = True

        else:
            if not uiInstance.inputTextBox.value:
                animationInstance.queue.append([5, "Try a different color"])

            else:
                try:
                    color = colorutils.web_to_rgb(uiInstance.inputTextBox.value)

                    if color == (255, 255, 255):
                        animationInstance.queue.append([5, "Try a different color"])

                    else:
                        connectionInstance.color = color
                        connectionInstance.inputRequest += 1

                        connectionInstance.hasColor = True
                        connectionInstance.hasInputs[1] = True
                        self.hasRequestedInput = False

                        animationInstance.queue.append([3, color])
                        animationInstance.queue.append([4, color])

                        uiInstance.inputTextBox.clear()

                        return color

                except ValueError:
                    animationInstance.queue.append([5, "Try a different color"])

        uiInstance.inputTextBox.clear()

        return uiInstance.animationColor

    def getHost(self, key):
        if not self.hasRequestedInput or not key:
            animationInstance.queue.append([5, f"{connectionInstance.username}, enter your IP"])

            self.hasRequestedInput = True

        else:
            if not uiInstance.inputTextBox.value or "." not in uiInstance.inputTextBox.value:
                animationInstance.queue.append([5, "Try a different IP"])

            else:
                connectionInstance.host = uiInstance.inputTextBox.value
                connectionInstance.inputRequest += 1

                connectionInstance.hasHost = True
                connectionInstance.hasInputs[2] = True
                self.hasRequestedInput = False

        uiInstance.inputTextBox.clear()

        return

    def getPort(self, key):
        if not self.hasRequestedInput or not key:
            animationInstance.queue.append([5, f"{connectionInstance.username}, enter your port"])

            self.hasRequestedInput = True

        else:
            if not len(str(uiInstance.inputTextBox.value)) == 5:
                animationInstance.queue.append([5, "Try a different port"])

            else:
                connectionInstance.port = uiInstance.inputTextBox.value
                connectionInstance.inputRequest += 1

                connectionInstance.hasPort = True
                connectionInstance.hasInputs[3] = True
                self.hasRequestedInput = False

        uiInstance.inputTextBox.clear()

        return

    def getPublicKey(self, key):
        if not self.hasRequestedInput or not key:
            animationInstance.queue.append([5, f"{connectionInstance.username}, enter the public RSA key"])

            self.hasRequestedInput = True

        else:
            if not len(uiInstance.inputTextBox.value) == 12:
                animationInstance.queue.append([5, "Try reentering the public RSA key"])

            else:
                connectionInstance.publicKey = uiInstance.inputTextBox.value
                connectionInstance.inputRequest += 1

                connectionInstance.hasPublicKey = True
                connectionInstance.hasInputs[4] = True
                self.hasRequestedInput = False

        uiInstance.inputTextBox.clear()

        return

    def getPrivateKey(self, key):
        if not self.hasRequestedInput or not key:
            animationInstance.queue.append([5, f"{connectionInstance.username}, enter your private RSA key"])

            self.hasRequestedInput = True

        else:
            if not len(uiInstance.inputTextBox.value) == 12:
                animationInstance.queue.append([5, "Try reentering the private RSA key"])

            else:
                connectionInstance.privateKey = uiInstance.inputTextBox.value
                connectionInstance.inputRequest += 1

                connectionInstance.hasPrivateKey = True
                connectionInstance.hasInputs[5] = True
                self.hasRequestedInput = False

        uiInstance.inputTextBox.clear()

        return

    def getCipherKey(self, key):
        if not self.hasRequestedInput or not key:
            animationInstance.queue.append([5, f"{connectionInstance.username}, enter the public Cipher key"])

            self.hasRequestedInput = True

        else:
            if not uiInstance.inputTextBox.value:
                animationInstance.queue.append([5, "Try a different public Cipher key"])

            else:
                connectionInstance.encryptedCipherKey = uiInstance.inputTextBox.value
                connectionInstance.inputRequest += 1

                connectionInstance.hasCipherKey = True
                connectionInstance.hasInputs[6] = True
                self.hasRequestedInput = False

        uiInstance.inputTextBox.clear()

        return

    def requestInput(self, key):
        if not connectionInstance.connected:
            # Creates a series of input requests
            color = uiInstance.animationColor

            # Creates white block cursor
            for check in range(7):
                if connectionInstance.inputRequest == check:
                    if connectionInstance.inputRequest == 1:
                        color = self.getInputs[1](key)

                    else:
                        self.getInputs[check](key)

                    animationInstance.queue.append([6, check, (255, 255, 255)])

            # Marks every completed input with color
            for check in range(7):
                if connectionInstance.hasInputs[check] and not connectionInstance.inputRequest == check:
                    animationInstance.queue.append([6, check, color])

            if connectionInstance.inputRequest < 0:
                connectionInstance.inputRequest = 6
                self.requestInput(key)

            if connectionInstance.inputRequest > 6:
                connectionInstance.inputRequest = 0
                self.requestInput(key)

            if connectionInstance.hasUsername and connectionInstance.hasColor and connectionInstance.hasHost \
                    and connectionInstance.hasPort and connectionInstance.hasPublicKey and \
                    connectionInstance.hasPrivateKey and connectionInstance.hasCipherKey and \
                    not connectionInstance.connected:
                connectionInstance.connect()

    def keyPressed(self, event):
        # Detects key presses with emphasis on enter, left and right
        if event:
            # Left and right keys bypass all if statements in getInputs, therefore will request for inputs every time
            # Whereas enter key does not bypass (as it is True), so it may request with the "try again" message
            if event.tk_event.keysym == "Left":
                if 7 > connectionInstance.inputRequest > -1:
                    animationInstance.queue.append([6, connectionInstance.inputRequest, uiInstance.bg])

                    connectionInstance.inputRequest -= 1

                    self.requestInput(False)

            if event.tk_event.keysym == "Right":
                if 7 > connectionInstance.inputRequest > -1:
                    animationInstance.queue.append([6, connectionInstance.inputRequest, uiInstance.bg])

                    connectionInstance.inputRequest += 1

                    self.requestInput(False)

            if event.tk_event.keysym == "Return":
                if connectionInstance.connected:
                    communicationInstance.sendToServer()

                else:
                    self.requestInput(True)

            else:
                if connectionInstance.connected and event.tk_event.keysym:
                    uiInstance.messageInput.focus()

                elif not connectionInstance.connected and event.tk_event.keysym:
                    uiInstance.inputTextBox.focus()

    # Methods below create the UI

    def openChat(self):
        # Creates chat window
        self.chatWindow = Window(self.setupWindow, width=1280, height=720, title="Chatroom", bg=self.bg)
        self.chatWindow.when_closed = connectionInstance.leave
        self.chatWindow.when_key_pressed = self.keyPressed

        topPadding = Box(self.chatWindow, width="fill", height=50, align="top")
        leftPadding = Box(self.chatWindow, width=50, height="fill", align="left")
        rightPadding = Box(self.chatWindow, width=50, height="fill", align="right")
        bottomPadding = Box(self.chatWindow, width="fill", height=50, align="bottom")

        self.border = Box(self.chatWindow, width="fill", height="fill")

        header = Box(self.border, width="fill", height=50, align="top")
        headerBlocker = Box(self.border, width="fill", height=50, align="top")

        userListBox = Box(self.border, width=220, height="fill", align="right")
        userBox = Box(self.border, width="fill", height="fill", align="left")
        inputBox = Box(userBox, width="fill", height=120, align="bottom")
        inputBlocker = Box(inputBox, width=50, height="fill", align="right")

        userListBorder = Box(userListBox, width=50, height="fill", align="left")
        self.userListTopBorder = Box(userListBox, width="fill", height=10, align="top")
        self.userListTopBorder.bg = uiInstance.animationColor
        self.userListRightBorder = Box(userListBox, width=10, height="fill", align="right")
        self.userListRightBorder.bg = uiInstance.animationColor
        self.userListBottomBorder = Box(userListBox, width="fill", height=10, align="bottom")
        self.userListBottomBorder.bg = uiInstance.animationColor
        self.userListLeftBorder = Box(userListBox, width=10, height="fill", align="left")
        self.userListLeftBorder.bg = uiInstance.animationColor

        self.userList = ListBox(userListBox, items=["Users online:"], width=150, height="fill", align="right")
        self.userList.text_color = connectionInstance.color
        self.userList.text_size = self.fontSize
        self.userList.bg = (255, 255, 255)

        self.header = Text(header, text=f"Welcome {connectionInstance.username}", width="fill", height=50)
        self.header.text_color = (255, 255, 255)
        self.header.text_size = self.fontSize + 14
        self.header.bg = uiInstance.animationColor

        self.chatHistoryTopBorder = Box(userBox, width="fill", height=10, align="top")
        self.chatHistoryTopBorder.bg = uiInstance.animationColor
        self.chatHistoryRightBorder = Box(userBox, width=10, height="fill", align="right")
        self.chatHistoryRightBorder.bg = uiInstance.animationColor
        self.chatHistoryBottomBorder = Box(userBox, width="fill", height=10, align="bottom")
        self.chatHistoryBottomBorder.bg = uiInstance.animationColor
        self.chatHistoryLeftBorder = Box(userBox, width=10, height="fill", align="left")
        self.chatHistoryLeftBorder.bg = uiInstance.animationColor

        self.chatHistory = TextBox(userBox, width="fill", height="fill", align="top", multiline=True)
        self.chatHistory.text_color = connectionInstance.color
        self.chatHistory.text_size = self.fontSize + 2
        self.chatHistory.bg = (255, 255, 255)
        self.chatHistory.disable()

        messageInputBorder = Box(inputBox, width="fill", height=50, align="top")
        self.messageInputTopBorder = Box(inputBox, width="fill", height=10, align="top")
        self.messageInputTopBorder.bg = uiInstance.animationColor
        self.messageInputRightBorder = Box(inputBox, width=10, height="fill", align="right")
        self.messageInputRightBorder.bg = uiInstance.animationColor
        self.messageInputBottomBorder = Box(inputBox, width="fill", height=10, align="bottom")
        self.messageInputBottomBorder.bg = uiInstance.animationColor
        self.messageInputLeftBorder = Box(inputBox, width=10, height="fill", align="left")
        self.messageInputLeftBorder.bg = uiInstance.animationColor

        self.messageInput = TextBox(inputBox, width="fill", align="bottom")
        self.messageInput.text_color = connectionInstance.color
        self.messageInput.text_size = self.fontSize + 10
        self.messageInput.bg = (255, 255, 255)
        self.messageInput.when_key_pressed = self.keyPressed

        # Threads here will start when the chat is open
        Thread(target=communicationInstance.updateThread).start()

        self.setupWindow.hide()
        self.chatWindow.show()

    def openSetup(self):
        # Creates setup window
        self.setupWindow = App(title="Connect", width=800, height=275)
        self.setupWindow.bg = self.bg
        self.setupWindow.font = self.font
        self.setupWindow.when_key_pressed = self.keyPressed

        topPadding = Box(self.setupWindow, width="fill", height=50, align="top")
        bottomPadding = Box(self.setupWindow, width="fill", height=50, align="bottom")
        contents = Box(self.setupWindow, width="fill", height="fill", align="top")

        header = Box(contents, width="fill", height=40, align="top")
        indicator = Box(contents, width="fill", height=40, align="bottom")

        rightPadding = Box(contents, width=20, height="fill", align="right")
        leftPadding = Box(contents, width=10, height="fill", align="left")

        self.status = Text(header, text="Welcome", width="fill", height=40)
        self.status.text_color = (255, 255, 255)
        self.status.text_size = self.fontSize + 10
        self.status.bg = uiInstance.animationColor

        self.inputTextBox = TextBox(contents, width=30, align="left")
        self.inputTextBox.text_color = (255, 255, 255)
        self.inputTextBox.text_size = self.fontSize
        self.inputTextBox.bg = self.darkbg

        self.connectText = Text(contents, text="Press Enter to continue", align="right")
        self.connectText.text_color = self.animationColor
        self.connectText.text_size = self.fontSize + 2

        self.usernameIndicator = Box(indicator, width=114, height="fill", align="left")
        self.colorIndicator = Box(indicator, width=114, height="fill", align="left")
        self.hostIndicator = Box(indicator, width=114, height="fill", align="left")
        self.portIndicator = Box(indicator, width=114, height="fill", align="left")
        self.publicKeyIndicator = Box(indicator, width=114, height="fill", align="left")
        self.privateKeyIndicator = Box(indicator, width=114, height="fill", align="left")
        self.cipherKeyIndicator = Box(indicator, width=114, height="fill", align="left")

        # Threads here will start when the code starts
        Thread(target=animationInstance.animationThread).start()

        self.setupWindow.display()


print(f"Started code at {str(time())}")

animationInstance = Animation()
communicationInstance = Communication()
connectionInstance = Connection()
uiInstance = UI()

uiInstance.openSetup()
