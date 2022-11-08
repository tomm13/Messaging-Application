# 8/11/2022
# V13 

# import logging
import platform
import socket
import colorutils
import sys
from time import sleep, localtime, strftime, time
from threading import Thread
from guizero import *


class Animation:
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

        return

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

            uiInstance.userList.text_color = (R, G, B)
            uiInstance.chatHistory.text_color = (R, G, B)
            uiInstance.messageInput.text_color = (R, G, B)

            sleep(uiInstance.rate)

        uiInstance.color = newColor

        return

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
            sleep(uiInstance.rate)

        uiInstance.animationColor = newColor

        return

    def animateStatus(self):
        # Code 5

        while not connectionInstance.connected:
            (R, G, B) = (255, 255, 255)

            while not R == uiInstance.animationColor[0] or not G == uiInstance.animationColor[1] or not \
                    B == uiInstance.animationColor[2]:
                if R > uiInstance.animationColor[0]:
                    R -= 1
                if G > uiInstance.animationColor[1]:
                    G -= 1
                if B > uiInstance.animationColor[2]:
                    B -= 1

                uiInstance.status.text_color = (R, G, B)
                uiInstance.connectText.text_color = (R, G, B)
                sleep(uiInstance.rate * 20)

            sleep(self.readRate)

            while not R == 255 or not G == 255 or not B == 255:
                if R < 255:
                    R += 1
                if G < 255:
                    G += 1
                if B < 255:
                    B += 1

                uiInstance.status.text_color = (R, G, B)
                uiInstance.connectText.text_color = (R, G, B)
                sleep(uiInstance.rate * 20)

            sleep(self.readRate)

        return

    def animationThread(self):
        # This is the new thread in place of the hundreds of unterminated threads called before
        # The format for this thread is [[Class animation method code, *args]]
        print(f"Started animation thread at : {str(time())}")
        while True:
            if self.queue:
                print(f"Animation queue at {str(time())}: {str(self.queue)}")
                # Check if queue has duplicate items
                while len(self.queue) > 1 and self.queue[0] == self.queue[1]:
                    self.queue.pop(0)

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
                    self.animateStatus()

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
    def decrypt(message):
        message = message.split()
        decryptedMessage = []

        for letter in message:
            letter = int(letter, base=10)
            index = pow(letter, connectionInstance.d, connectionInstance.N)
            decryptedLetter = chr(index)
            decryptedMessage.append(decryptedLetter)

        message = str("".join(decryptedMessage))
        return message

    @staticmethod
    def saveChatHistory(location):
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
        uiInstance.animationColor = (255, 0, 0)

        while True:
            animationInstance.queue.append([1, "You cannot use this username, "
                                               "please rejoin under a different username"])
            sleep(1)

    def sendToServer(self):
        try:
            message = uiInstance.messageInput.value
            if message:
                if message == "/leave":
                    connectionInstance.leave()
                else:
                    if len(message) + len(connectionInstance.username) + 2 >= 45:
                        if not self.messageTooLongWarning:
                            animationInstance.queue.append([1, "Your message is too long."])
                            self.messageTooLongWarning = True
                            self.warningTimer = time()

                        else:
                            if time() > self.warningTimer + 5:
                                self.messageTooLongWarning = False

                    else:
                        connectionInstance.socket.send(message.encode())
                        uiInstance.messageInput.clear()

        except BrokenPipeError:
            connectionInstance.connected = False
            connectionInstance.leave()

    def setUsers(self, message):
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
        if message == connectionInstance.username:
            while True:
                uiInstance.animationColor = (255, 0, 0)
                animationInstance.queue.append([1, "You have been kicked / disconnected"])
                sleep(1)

        uiInstance.userList.remove(message[8:])
        self.users.remove(message[8:])
        message = f"{message[8:]} has disconnected"
        animationInstance.queue.append([1, message])

    def previousPage(self):
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
        try:
            print(f"Started update thread at {str(time())}")
            while connectionInstance.connected:
                message = self.decrypt(connectionInstance.socket.recv(1024).decode())

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

                    elif message[0:14] == "/recentmessage":
                        self.addMessage(message[15:])

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
    def __init__(self, username, color, host, port, privateKey):
        self.username = username
        self.color = color
        self.host = host
        self.port = port
        self.privateKey = privateKey
        self.d = None
        self.N = None
        self.socket = socket.socket()
        self.connected = False
        self.mod = False

    def connect(self, usernameInput, colorInput, hostInput, portInput, privateKeyInput):
        try:
            self.username = usernameInput.value
            self.color = colorInput.value
            self.host = hostInput.value
            self.port = int(portInput.value, base=10)
            self.privateKey = privateKeyInput.value
            self.d = int(str(self.privateKey[0:6]), base=10)
            self.N = int(str(self.privateKey[6:12]), base=10)

            if not self.username == "" and not self.username == "Username" and " " not in self.username and "[" not in \
                    self.username and "]" not in self.username:
                # Checks: if username is not empty, not Username and does not contain spaces or [ and ]

                try:
                    uiInstance.color = colorutils.web_to_rgb(connectionInstance.color)
                    uiInstance.status.value = "Connection Success"

                    self.socket.connect((self.host, self.port))
                    self.socket.send(self.username.encode())
                    self.connected = True

                    UI.openChat(uiInstance)

                except ConnectionRefusedError:
                    uiInstance.status.value = "Connection Refused"

                except OSError:
                    connectionInstance.leave()

                except BrokenPipeError:
                    uiInstance.status.value = "Broken Pipe"

            else:
                uiInstance.status.value = "Invalid Username"

        except ValueError:
            uiInstance.status.value = "Invalid Values"

        except IndexError:
            uiInstance.status.value = "Invalid Key Format"

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
        self.usernameInput = None
        self.colorInput = None
        self.hostInput = None
        self.portInput = None
        self.keyInput = None
        self.status = None
        self.connectText = None

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
        self.page = 0

        if platform.system() == "Darwin":
            self.fontSize = 22
            self.rate = 0.00035
            self.linesLimit = 13
        elif platform.system() == "Windows":
            self.fontSize = 18
            self.rate = 0.00000
            self.linesLimit = 9

    # Methods below alter UI attributes

    @staticmethod
    def chooseColor(code, message):
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
        if message == connectionInstance.username and not connectionInstance.mod:
            if not uiInstance.darkMode:
                animationInstance.queue.append([2, False])

            connectionInstance.mod = True

            uiInstance.chooseColor(3, "khaki")
            uiInstance.chooseColor(4, "khaki")

    @staticmethod
    def setRate(rate):
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
        if uiInstance.LDM:
            uiInstance.LDM = False
            animationInstance.queue.append([1, "You turned LDM off"])

        else:
            uiInstance.LDM = True
            animationInstance.queue.append([1, "You turned LDM on"])

    # Methods below create the UI
    def openChat(self):
        try:
            self.chatWindow = Window(self.setupWindow, width=1280, height=720, title="Chatroom", bg=self.bg)
            self.chatWindow.when_closed = connectionInstance.leave
            self.chatWindow.when_key_pressed = keyPressed

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
            self.userList.bg = (255, 255, 255)
            self.userList.text_size = self.fontSize

            self.header = Text(header, text="Connecting...", width="fill", height=50)
            self.header.text_size = self.fontSize + 14
            self.header.text_color = (255, 255, 255)
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
            self.chatHistory.bg = (255, 255, 255)
            self.chatHistory.text_size = self.fontSize + 2
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
            self.messageInput.bg = (255, 255, 255)
            self.messageInput.text_size = self.fontSize + 10
            self.messageInput.when_key_pressed = keyPressed

            # Threads start here

            startUpdateThread = Thread(target=communicationInstance.updateThread)
            startUpdateThread.start()

            self.setupWindow.hide()
            self.chatWindow.show()

        except Exception as e:
            print(f"Your client crashed unexpectedly due to {str(e)}")
            connectionInstance.leave()

    def openSetup(self):
        self.setupWindow = App(title="Connect", width=800, height=275)
        self.setupWindow.bg = self.bg
        self.setupWindow.font = self.font
        self.setupWindow.when_key_pressed = keyPressed

        topPadding = Box(self.setupWindow, width="fill", height=50, align="top")
        bottomPadding = Box(self.setupWindow, width="fill", height=50, align="bottom")
        contents = Box(self.setupWindow, width="fill", height="fill", align="top")

        inputBox = Box(contents, width=400, height=150, align="left")
        rightPadding = Box(contents, width=16, height="fill", align="right")
        verifyBox = Box(contents, width=384, height=150, align="right")

        usernameBlocker = Box(inputBox, width=15, height=150, align="right")
        usernameInputBox = Box(inputBox, width=275, height=30)
        colorBlocker = Box(inputBox, width=15, height=120, align="right")
        colorInputBox = Box(inputBox, width=260, height=30)
        hostBlocker = Box(inputBox, width=15, height=90, align="right")
        hostInputBox = Box(inputBox, width=245, height=30)
        portBlocker = Box(inputBox, width=15, height=60, align="right")
        portInputBox = Box(inputBox, width=230, height=30)
        keyBlocker = Box(inputBox, width=15, height=30, align="right")
        keyInputBox = Box(inputBox, width=215, height=30)

        self.usernameInput = TextBox(usernameInputBox, text=connectionInstance.username, width="fill")
        self.colorInput = TextBox(colorInputBox, text=connectionInstance.color, width="fill")
        self.hostInput = TextBox(hostInputBox, text=connectionInstance.host, width="fill")
        self.portInput = TextBox(portInputBox, text=connectionInstance.port, width="fill")
        self.keyInput = TextBox(keyInputBox, text=connectionInstance.privateKey, width="fill")

        self.usernameInput.text_color = self.animationColor
        self.colorInput.text_color = self.animationColor
        self.hostInput.text_color = self.animationColor
        self.portInput.text_color = self.animationColor
        self.keyInput.text_color = self.animationColor

        self.usernameInput.text_size = self.fontSize - 6
        self.colorInput.text_size = self.fontSize - 6
        self.hostInput.text_size = self.fontSize - 6
        self.portInput.text_size = self.fontSize - 6
        self.keyInput.text_size = self.fontSize - 6

        self.usernameInput.bg = self.darkbg
        self.colorInput.bg = self.darkbg
        self.hostInput.bg = self.darkbg
        self.portInput.bg = self.darkbg
        self.keyInput.bg = self.darkbg

        self.status = Text(verifyBox, text="Not Connected")
        self.status.text_size = self.fontSize + 12

        verifyBoxBlocker = Box(verifyBox, width="fill", height=64, align="top")

        self.connectText = Text(verifyBox, text="Enter to continue")
        self.connectText.text_size = self.fontSize + 2

        build = Text(bottomPadding, text="Optimisation part 2", align="bottom")

        animationInstance.queue.append([5])

        startAnimationThread = Thread(target=animationInstance.animationThread)
        startAnimationThread.start()

        self.setupWindow.display()


def keyPressed(event):
    if event:
        if event.tk_event.keysym == "Return":
            if connectionInstance.connected:
                communicationInstance.sendToServer()
            else:
                connectionInstance.connect(uiInstance.usernameInput, uiInstance.colorInput,
                                           uiInstance.hostInput, uiInstance.portInput, uiInstance.keyInput)

        else:
            if connectionInstance.connected and event.tk_event.keysym.isalnum():
                uiInstance.messageInput.focus()


print(f"Started code at {str(time())}")

# connectionInstance = Connection("Username", "Chat Color", "Host IP", "Port", "Private Key")
connectionInstance = Connection("tomm", "lightblue", "10.28.206.143", "61172", "502315755221")
uiInstance = UI()
communicationInstance = Communication()
animationInstance = Animation()

UI.openSetup(uiInstance)
