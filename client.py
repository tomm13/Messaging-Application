# 5/1/2023
# V13.3

import platform
import socket
import colorutils
from time import sleep, localtime, strftime, time
from threading import Thread
from guizero import *


class Animation:
    # Creates a class with animation methods and a thread method
    def __init__(self):
        self.queue = []
        self.readRate = 1
        self.waitMultiplier = 1

    # Creates animations used in chat

    def animateHeaderInChat(self, message):
        # Code 1

        if uiInstance.LDM is False:
            if uiInstance.darkMode is False:
                (R, G, B) = (255, 255, 255)

                while (R, G, B) != uiInstance.animationColor:
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

                while (R, G, B) != (255, 255, 255):
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

                while (R, G, B) != uiInstance.animationColor:
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

                uiInstance.header.value = "Welcome " + connectionInstance.inputs[0]

                while (R, G, B) != (255, 255, 255):
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

                while (R, G, B) != uiInstance.animationColor:
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

                while (R, G, B) != uiInstance.darkbg:
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

                while (R, G, B) != uiInstance.animationColor:
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

                uiInstance.header.value = f"Welcome {connectionInstance.inputs[0]}"

                while (R, G, B) != uiInstance.darkbg:
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

        else:
            communicationInstance.addMessage(message)

    @staticmethod
    def switchTheme():
        # Code 2
        if uiInstance.LDM is False:
            if uiInstance.darkMode is True:
                while uiInstance.darkMode is True:
                    # To turn Dark Mode off
                    (R, G, B) = (70, 70, 70)

                    while (R, G, B) != (255, 255, 255):
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
                while uiInstance.darkMode is False:
                    # To turn Dark Mode on
                    (R, G, B) = (255, 255, 255)

                    while (R, G, B) != uiInstance.darkbg:
                        R -= 1
                        G -= 1
                        B -= 1

                        uiInstance.header.text_color = (R, G, B)
                        uiInstance.chatHistory.bg = (R, G, B)
                        uiInstance.messageInput.bg = (R, G, B)
                        uiInstance.userList.bg = (R, G, B)
                        sleep(uiInstance.rate)

                    uiInstance.darkMode = True

        else:
            if uiInstance.darkMode is True:
                # To turn Dark Mode off
                (R, G, B) = (255, 255, 255)

                uiInstance.header.text_color = (R, G, B)
                uiInstance.chatHistory.bg = (R, G, B)
                uiInstance.messageInput.bg = (R, G, B)
                uiInstance.userList.bg = (R, G, B)

                uiInstance.darkMode = False

            else:
                # To turn Dark Mode on
                (R, G, B) = uiInstance.darkbg

                uiInstance.header.text_color = (R, G, B)
                uiInstance.chatHistory.bg = (R, G, B)
                uiInstance.messageInput.bg = (R, G, B)
                uiInstance.userList.bg = (R, G, B)

                uiInstance.darkMode = True

    @staticmethod
    def fadeColorsInChat(newColor):
        # Code 3

        if uiInstance.LDM is False:
            (R, G, B) = uiInstance.color

            while (R, G, B) != newColor:
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

        else:
            (R, G, B) = newColor

            uiInstance.userList.text_color = (R, G, B)
            uiInstance.chatHistory.text_color = (R, G, B)
            uiInstance.messageInput.text_color = (R, G, B)

        uiInstance.color = newColor

    @staticmethod
    def fadeBordersInChat(newColor):
        # Code 4

        if uiInstance.LDM is False:
            (R, G, B) = uiInstance.animationColor

            while (R, G, B) != newColor:
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

        else:
            (R, G, B) = newColor

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

        uiInstance.animationColor = newColor

    # Creates animations used in setup

    @staticmethod
    def animateHeaderInSetup(message):
        # Code 5

        if uiInstance.LDM is False:
            (R, G, B) = (255, 255, 255)

            while (R, G, B) != uiInstance.animationColor:
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

            while (R, G, B) != (255, 255, 255):
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

        else:
            uiInstance.status.value = message

    @staticmethod
    def fadeColorsInSetup(newColor):
        # Code 6

        if uiInstance.LDM is False:
            (R, G, B) = uiInstance.color

            while (R, G, B) != newColor:
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

                uiInstance.connectText.text_color = (R, G, B)
                uiInstance.inputTextBox.text_color = (R, G, B)
                uiInstance.status.bg = (R, G, B)

                sleep(uiInstance.rate)

        else:
            (R, G, B) = newColor

            uiInstance.connectText.text_color = (R, G, B)
            uiInstance.inputTextBox.text_color = (R, G, B)
            uiInstance.status.bg = (R, G, B)

        uiInstance.color = newColor

    @staticmethod
    def fadeIndicator(key, newColor):
        # Code 7

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

        if uiInstance.LDM is False:

            while (R, G, B) != newColor:
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

        else:
            (R, G, B) = newColor

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

    def animationThread(self):
        # This is the new thread in place of the hundreds of unterminated threads called before
        # The format for this thread is [[Class animation method code, *args]]
        while True:
            if self.queue:
                # Check if queue has duplicate items
                while len(self.queue) > 1 and self.queue[0] == self.queue[1]:
                    self.queue.pop(1)

                if self.queue[0][0] == 1:
                    if len(str(self.queue[0][0])) < 10:
                        self.waitMultiplier = 2.0
                    elif len(str(self.queue[0][0])) < 15:
                        self.waitMultiplier = 2.5
                    else:
                        self.waitMultiplier = 3.0

                    self.animateHeaderInChat(self.queue[0][1])

                elif self.queue[0][0] == 2:
                    if (uiInstance.darkMode and uiInstance.color == (255, 255, 255)) \
                            or (uiInstance.darkMode and uiInstance.animationColor == (255, 255, 255)) \
                            or (not uiInstance.darkMode and uiInstance.color == (0, 0, 0)) \
                            or (not uiInstance.darkMode and uiInstance.animationColor == (0, 0, 0)):

                            self.queue.append([1, "You cannot change the theme due to contrast"])

                    else:
                        self.switchTheme()

                elif self.queue[0][0] == 3:
                    self.fadeColorsInChat(self.queue[0][1])

                elif self.queue[0][0] == 4:
                    self.fadeBordersInChat(self.queue[0][1])

                elif self.queue[0][0] == 5:
                    if len(str(self.queue[0][0])) < 10:
                        self.waitMultiplier = 2.0
                    elif len(str(self.queue[0][0])) < 15:
                        self.waitMultiplier = 2.5
                    else:
                        self.waitMultiplier = 3.0

                    self.animateHeaderInSetup(self.queue[0][1])

                elif self.queue[0][0] == 6:
                    self.fadeColorsInSetup(self.queue[0][1])

                elif self.queue[0][0] == 7:
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

    def sendToServer(self, message):
        # Gets the value of the input, encrypts, then broadcasts
        try:
            if message:
                if message == "/leave":
                    connectionInstance.leave()
                else:
                    if len(message) + len(connectionInstance.inputs[0]) + 2 >= 45:
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
            connectionInstance.leave()

    def addUsers(self, users):
        # Called by /add [Users spilt by space]
        users = users.split()
        users.sort()

        uiInstance.userList.clear()
        uiInstance.userList.append("Users online:")

        for user in users:
            if user not in self.users:
                uiInstance.userList.append(user)
                self.users.append(user)

                animationInstance.queue.append([1, f"{str(user)} has connected"])

            else:
                uiInstance.userList.append(user)

    def removeUser(self, user):
        # Called by /remove [Users split by space]
        try:
            if user == connectionInstance.inputs[0]:
                while True:
                    uiInstance.animationColor = (255, 0, 0)
                    animationInstance.queue.append([1, "You have been kicked / disconnected"])
                    sleep(1)

            uiInstance.userList.remove(user)
            self.users.remove(user)
            animationInstance.queue.append([1, f"{user} has disconnected"])

        except ValueError as e:
            print(f"Tried to remove -{user}-. Failed due to {e}")

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

                    elif message[0:6] == "/color":
                        uiInstance.chooseColor(3, message[7:])

                    elif message[0:7] == "/border":
                        uiInstance.chooseColor(4, message[8:])

                    elif message[0:4] == "/add":
                        self.addUsers(message[5:])

                    elif message[0:7] == "/remove":
                        self.removeUser(message[8:])

                    elif message == "/next":
                        self.nextPage()

                    elif message == "/previous":
                        self.previousPage()

                    elif message == "/disconnect":
                        self.disconnectLoop()

                    else:
                        self.addMessage(message)

        except (ConnectionResetError, OSError):
            connectionInstance.leave()


class Connection:
    def __init__(self):
        # Inputs list
        self.inputs = [None for i in range(7)]

        # Attributes
        self.socket = socket.socket()
        self.e = None
        self.d = None
        self.N = None
        self.cipherKey = None
        self.connected = False
        self.mod = False
        self.inputRequest = 0
        self.timeoutduration = 5

    def connect(self):
        # Called when the user has filled out all 7 inputs
        # Connects to the socket, calculates the RSA encryption key, decryption key, and
        # The cipher key.
        self.e = int(str(self.inputs[4][0:6]), base=10)
        self.d = int(str(self.inputs[5][0:6]), base=10)
        self.N = int(str(self.inputs[5][6:12]), base=10)
        self.cipherKey = communicationInstance.rsaDecrypt(int(self.inputs[6], base=10))

        try:
            self.socket.settimeout(self.timeoutduration)
            self.socket.connect((self.inputs[2], int(self.inputs[3], base=10)))
            self.socket.settimeout(None)

            self.socket.send(self.inputs[0].encode())
            self.connected = True

            uiInstance.color = self.inputs[1]
            uiInstance.animationColor = self.inputs[1]
            uiInstance.openChat()

        except (ConnectionRefusedError, OSError, TimeoutError):
            animationInstance.queue.append([5, "Connection refused, try checking the host IP and port"])

    def leave(self):
        if connectionInstance.connected:
            self.socket.send("/leave".encode())
            self.connected = False

            uiInstance.chatWindow.exit_full_screen()
            uiInstance.chatWindow.destroy()

        uiInstance.setupWindow.destroy()

        self.socket.close()


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
        self.page = 0
        self.linesSent = 0
        self.linesLimit = 19
        self.darkMode = False
        self.hasRequestedInput = False

        # Font sizes list for different OS's
        self.fontSizes = [[22, 17], [36, 26], [24, 19], [32, 28], [32, 23], [22, 19], [24, 17]]

        # Messages List
        self.getInputsMessages = [["Choose a username", "Try a different username"],
                                  ["Choose a color", "Try a different color"],
                                  ["Enter the host IP", "Try a different IP"],
                                  ["Enter the host port", "Try a different port"],
                                  ["Enter the public key", "Try a different public key"],
                                  ["Enter the private key", "Try a different private key"],
                                  ["Enter the cipher key", "Try a different cipher key"]]

        if platform.system() == "Darwin":
            # For macOS
            self.fontIndex = 0
            self.rate = 0.00035
            self.LDM = False

        else:
            # For other platforms
            self.fontIndex = 1
            self.rate = None
            self.LDM = True

            print("Unfortunately your system does not support animations, therefore they have been disabled.")

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
        if message == connectionInstance.inputs[0] and not connectionInstance.mod:
            if not uiInstance.darkMode:
                animationInstance.queue.append([2, False])

            connectionInstance.mod = True

            uiInstance.chooseColor(3, "khaki")
            uiInstance.chooseColor(4, "khaki")

    @staticmethod
    def setLDM():
        # Called by /ldm
        if platform.system() == "Darwin":
            # For macOS
            if uiInstance.LDM:
                uiInstance.LDM = False
                animationInstance.queue.append([1, "You turned LDM off"])

            else:
                uiInstance.LDM = True
                animationInstance.queue.append([1, "You turned LDM on"])

        else:
            animationInstance.queue.append(
                [1, "Animations are forcefully disabled on your OS."])

    # Gets the 7 inputs
    def getInputs(self, check, key, value):
        if not self.hasRequestedInput or not key:
            animationInstance.queue.append([5, self.getInputsMessages[check][0]])

            self.hasRequestedInput = True

        else:
            if not value:
                animationInstance.queue.append([5, self.getInputsMessages[check][1]])

            else:
                # If the requested input is color
                if check == 1:
                    try:
                        color = colorutils.web_to_rgb(value)

                        # Prevent matching background and text colors
                        if color == (255, 255, 255):
                            animationInstance.queue.append([5, self.getInputsMessages[check][1]])

                        else:
                            # The inputted color is accepted, and the UI elements will fade to this new color
                            animationInstance.queue.append([6, color])

                            return color

                    except ValueError:
                        animationInstance.queue.append([5, self.getInputsMessages[check][1]])

                else:
                    return value

        return None

    def requestInput(self, key, value):
        if not connectionInstance.connected:
            # Creates a series of input requests
            for check in range(7):
                if connectionInstance.inputRequest == check:
                    val = self.getInputs(check, key, value)

                    # Get best value
                    if val is not None:
                        connectionInstance.inputs[check] = val
                        connectionInstance.inputRequest += 1

                        self.hasRequestedInput = False

                    # For testing, UI elements are inaccessible
                    if __name__ == '__main__':
                        self.inputTextBox.clear()

                    # Creates white block cursor
                    animationInstance.queue.append([7, check, (255, 255, 255)])

            # Marks every completed input with color
            for check in range(7):
                if connectionInstance.inputs[check] and not connectionInstance.inputRequest == check:

                    # Use the inputted color if given, otherwise use the default lightblue
                    if connectionInstance.inputs[1] is not None:
                        animationInstance.queue.append([7, check, connectionInstance.inputs[1]])

                    else:
                        # Copies the default color into the inputs list
                        animationInstance.queue.append([7, check, uiInstance.animationColor])

            if connectionInstance.inputRequest < 0:
                connectionInstance.inputRequest = 6
                self.requestInput(key, value)

            if connectionInstance.inputRequest > 6:
                connectionInstance.inputRequest = 0
                self.requestInput(key, value)

            if all(check is not None for check in connectionInstance.inputs) \
                    and key and not connectionInstance.connected:
                connectionInstance.connect()

    def keyPressed(self, event):
        # Detects key presses with emphasis on enter, left and right
        if event:
            # Left and right keys bypass all if statements in getInputs, therefore will request for inputs every time
            # Whereas enter key does not bypass (as it is True), so it may request with the "try again" message
            if event.tk_event.keysym == "Left":
                if 7 > connectionInstance.inputRequest > -1:
                    animationInstance.queue.append([7, connectionInstance.inputRequest, uiInstance.bg])

                    connectionInstance.inputRequest -= 1

                    self.requestInput(False, uiInstance.inputTextBox.value)

            if event.tk_event.keysym == "Right":
                if 7 > connectionInstance.inputRequest > -1:
                    animationInstance.queue.append([7, connectionInstance.inputRequest, uiInstance.bg])

                    connectionInstance.inputRequest += 1

                    self.requestInput(False, uiInstance.inputTextBox.value)

            if event.tk_event.keysym == "Return":
                if connectionInstance.connected:
                    communicationInstance.sendToServer(uiInstance.messageInput.value)

                else:
                    self.requestInput(True, uiInstance.inputTextBox.value)

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
        self.chatWindow.set_full_screen()

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
        self.userListTopBorder.bg = self.color
        self.userListRightBorder = Box(userListBox, width=10, height="fill", align="right")
        self.userListRightBorder.bg = self.color
        self.userListBottomBorder = Box(userListBox, width="fill", height=10, align="bottom")
        self.userListBottomBorder.bg = self.color
        self.userListLeftBorder = Box(userListBox, width=10, height="fill", align="left")
        self.userListLeftBorder.bg = self.color

        self.userList = ListBox(userListBox, items=["Users online:"], width=150, height="fill", align="right")
        self.userList.text_color = self.color
        self.userList.text_size = self.fontSizes[0][self.fontIndex]
        self.userList.bg = (255, 255, 255)

        self.header = Text(header, text=f"Welcome {connectionInstance.inputs[0]}", width="fill", height=50)
        self.header.text_color = (255, 255, 255)
        self.header.text_size = self.fontSizes[1][self.fontIndex]
        self.header.bg = self.color

        self.chatHistoryTopBorder = Box(userBox, width="fill", height=10, align="top")
        self.chatHistoryTopBorder.bg = self.color
        self.chatHistoryRightBorder = Box(userBox, width=10, height="fill", align="right")
        self.chatHistoryRightBorder.bg = self.color
        self.chatHistoryBottomBorder = Box(userBox, width="fill", height=10, align="bottom")
        self.chatHistoryBottomBorder.bg = self.color
        self.chatHistoryLeftBorder = Box(userBox, width=10, height="fill", align="left")
        self.chatHistoryLeftBorder.bg = self.color

        self.chatHistory = TextBox(userBox, width="fill", height="fill", align="top", multiline=True)
        self.chatHistory.text_color = self.color
        self.chatHistory.text_size = self.fontSizes[2][self.fontIndex]
        self.chatHistory.bg = (255, 255, 255)
        self.chatHistory.disable()

        messageInputBorder = Box(inputBox, width="fill", height=50, align="top")
        self.messageInputTopBorder = Box(inputBox, width="fill", height=10, align="top")
        self.messageInputTopBorder.bg = self.color
        self.messageInputRightBorder = Box(inputBox, width=10, height="fill", align="right")
        self.messageInputRightBorder.bg = self.color
        self.messageInputBottomBorder = Box(inputBox, width="fill", height=10, align="bottom")
        self.messageInputBottomBorder.bg = self.color
        self.messageInputLeftBorder = Box(inputBox, width=10, height="fill", align="left")
        self.messageInputLeftBorder.bg = self.color

        self.messageInput = TextBox(inputBox, width="fill", align="bottom")
        self.messageInput.text_color = self.color
        self.messageInput.text_size = self.fontSizes[3][self.fontIndex]
        self.messageInput.bg = (255, 255, 255)
        self.messageInput.when_key_pressed = self.keyPressed

        # Threads here will start when the chat is open
        Thread(target=communicationInstance.updateThread).start()

        self.setupWindow.hide()
        self.chatWindow.show()

    def openSetup(self):
        # Creates setup window
        self.setupWindow = App(title="Setup", width=800, height=275)
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
        self.status.text_size = self.fontSizes[4][self.fontIndex]
        self.status.bg = self.animationColor

        self.inputTextBox = TextBox(contents, width=30, align="left")
        self.inputTextBox.text_color = self.color
        self.inputTextBox.text_size = self.fontSizes[5][self.fontIndex]
        self.inputTextBox.bg = self.darkbg

        self.connectText = Text(contents, text="Press Enter to continue", align="right")
        self.connectText.text_color = self.animationColor
        self.connectText.text_size = self.fontSizes[6][self.fontIndex]

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


animationInstance = Animation()
communicationInstance = Communication()
connectionInstance = Connection()
uiInstance = UI()

if __name__ == '__main__':
    uiInstance.openSetup()
