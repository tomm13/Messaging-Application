# 2/4/2023
# V13.3.1


from socket import socket
from colorutils import web_to_rgb
from platform import system
from time import sleep, localtime, strftime
from threading import Thread
from guizero import *


class Animation:
    # An indefinite thread (animation thread) runs off a list and checks for items in the list.
    # When there is an item in the list, appended by the rest of the code, the thread indexes the animation
    # "code" and runs the corresponding animation method, passing in any relevant arguments such as message

    def __init__(self):
        self.queue = []
        self.waitMultiplier = 1

    def animateHeaderInChat(self, message):
        # Code 1

        if ui.LDM is False:
            if ui.darkMode is False:
                (R, G, B) = ui.lightbg

                while (R, G, B) != ui.animationColor:
                    # Text fades from white to color
                    if R < ui.animationColor[0]:
                        R += 1
                    if G < ui.animationColor[1]:
                        G += 1
                    if B < ui.animationColor[2]:
                        B += 1
                    if R > ui.animationColor[0]:
                        R -= 1
                    if G > ui.animationColor[1]:
                        G -= 1
                    if B > ui.animationColor[2]:
                        B -= 1

                    ui.header.text_color = (R, G, B)
                    sleep(ui.rate)

                ui.header.value = message

                while (R, G, B) != ui.lightbg:
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

                    ui.header.bg = (R, G, B)
                    sleep(ui.rate)

                sleep(self.waitMultiplier)

                while (R, G, B) != ui.animationColor:
                    # Fades background from white to color
                    if R < ui.animationColor[0]:
                        R += 1
                    if G < ui.animationColor[1]:
                        G += 1
                    if B < ui.animationColor[2]:
                        B += 1
                    if R > ui.animationColor[0]:
                        R -= 1
                    if G > ui.animationColor[1]:
                        G -= 1
                    if B > ui.animationColor[2]:
                        B -= 1

                    ui.header.bg = (R, G, B)
                    sleep(ui.rate)

                ui.header.value = "Welcome " + connection.inputs[0]

                while (R, G, B) != ui.lightbg:
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

                    ui.header.text_color = (R, G, B)
                    sleep(ui.rate)

            else:
                (R, G, B) = ui.darkbg

                while (R, G, B) != ui.animationColor:
                    # Text fades from black to color
                    if R < ui.animationColor[0]:
                        R += 1
                    if G < ui.animationColor[1]:
                        G += 1
                    if B < ui.animationColor[2]:
                        B += 1
                    if R > ui.animationColor[0]:
                        R -= 1
                    if G > ui.animationColor[1]:
                        G -= 1
                    if B > ui.animationColor[2]:
                        B -= 1

                    ui.header.text_color = (R, G, B)
                    sleep(ui.rate)

                ui.header.value = message

                while (R, G, B) != ui.darkbg:
                    # Fades background from color to black
                    if R < ui.darkbg[0]:
                        R += 1
                    if G < ui.darkbg[1]:
                        G += 1
                    if B < ui.darkbg[2]:
                        B += 1
                    if R > ui.darkbg[0]:
                        R -= 1
                    if G > ui.darkbg[1]:
                        G -= 1
                    if B > ui.darkbg[2]:
                        B -= 1

                    ui.header.bg = (R, G, B)
                    sleep(ui.rate)

                sleep(self.waitMultiplier)

                while (R, G, B) != ui.animationColor:
                    # Fades background from black to color
                    if R > ui.animationColor[0]:
                        R -= 1
                    if G > ui.animationColor[1]:
                        G -= 1
                    if B > ui.animationColor[2]:
                        B -= 1
                    if R < ui.animationColor[0]:
                        R += 1
                    if G < ui.animationColor[1]:
                        G += 1
                    if B < ui.animationColor[2]:
                        B += 1

                    ui.header.bg = (R, G, B)
                    sleep(ui.rate)

                ui.header.value = f"Welcome {connection.inputs[0]}"

                while (R, G, B) != ui.darkbg:
                    # Text fades from any color to black
                    if R < ui.darkbg[0]:
                        R += 1
                    if G < ui.darkbg[1]:
                        G += 1
                    if B < ui.darkbg[2]:
                        B += 1
                    if R > ui.darkbg[0]:
                        R -= 1
                    if G > ui.darkbg[1]:
                        G -= 1
                    if B > ui.darkbg[2]:
                        B -= 1

                    ui.header.text_color = (R, G, B)
                    sleep(ui.rate)

        else:
            communication.setMessage(message)

    @staticmethod
    def switchTheme():
        # Code 2
        if ui.LDM is False:
            if ui.darkMode is True:
                while ui.darkMode is True:
                    # To turn Dark Mode off
                    (R, G, B) = (70, 70, 70)

                    while (R, G, B) != ui.lightbg:
                        R += 1
                        G += 1
                        B += 1

                        ui.header.text_color = (R, G, B)
                        ui.chatHistory.bg = (R, G, B)
                        ui.messageInput.bg = (R, G, B)
                        ui.userList.bg = (R, G, B)
                        sleep(ui.rate)

                    ui.darkMode = False

            else:
                while ui.darkMode is False:
                    # To turn Dark Mode on
                    (R, G, B) = ui.lightbg

                    while (R, G, B) != ui.darkbg:
                        R -= 1
                        G -= 1
                        B -= 1

                        ui.header.text_color = (R, G, B)
                        ui.chatHistory.bg = (R, G, B)
                        ui.messageInput.bg = (R, G, B)
                        ui.userList.bg = (R, G, B)
                        sleep(ui.rate)

                    ui.darkMode = True

        else:
            if ui.darkMode is True:
                # To turn Dark Mode off
                (R, G, B) = ui.lightbg

                ui.header.text_color = (R, G, B)
                ui.chatHistory.bg = (R, G, B)
                ui.messageInput.bg = (R, G, B)
                ui.userList.bg = (R, G, B)

                ui.darkMode = False

            else:
                # To turn Dark Mode on
                (R, G, B) = ui.darkbg

                ui.header.text_color = (R, G, B)
                ui.chatHistory.bg = (R, G, B)
                ui.messageInput.bg = (R, G, B)
                ui.userList.bg = (R, G, B)

                ui.darkMode = True

    @staticmethod
    def fadeColorsInChat(newColor):
        # Code 3

        if ui.LDM is False:
            (R, G, B) = ui.color

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

                ui.userList.text_color = (R, G, B)
                ui.chatHistory.text_color = (R, G, B)
                ui.messageInput.text_color = (R, G, B)

                sleep(ui.rate)

        else:
            (R, G, B) = newColor

            ui.userList.text_color = (R, G, B)
            ui.chatHistory.text_color = (R, G, B)
            ui.messageInput.text_color = (R, G, B)

        ui.color = newColor

    @staticmethod
    def fadeBordersInChat(newColor):
        # Code 4

        if ui.LDM is False:
            (R, G, B) = ui.animationColor

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

                ui.header.bg = (R, G, B)
                ui.chatHistoryTopBorder.bg = (R, G, B)
                ui.chatHistoryRightBorder.bg = (R, G, B)
                ui.chatHistoryBottomBorder.bg = (R, G, B)
                ui.chatHistoryLeftBorder.bg = (R, G, B)
                ui.userListTopBorder.bg = (R, G, B)
                ui.userListRightBorder.bg = (R, G, B)
                ui.userListBottomBorder.bg = (R, G, B)
                ui.userListLeftBorder.bg = (R, G, B)
                ui.messageInputTopBorder.bg = (R, G, B)
                ui.messageInputRightBorder.bg = (R, G, B)
                ui.messageInputBottomBorder.bg = (R, G, B)
                ui.messageInputLeftBorder.bg = (R, G, B)

                sleep(ui.rate)

        else:
            (R, G, B) = newColor

            ui.header.bg = (R, G, B)
            ui.chatHistoryTopBorder.bg = (R, G, B)
            ui.chatHistoryRightBorder.bg = (R, G, B)
            ui.chatHistoryBottomBorder.bg = (R, G, B)
            ui.chatHistoryLeftBorder.bg = (R, G, B)
            ui.userListTopBorder.bg = (R, G, B)
            ui.userListRightBorder.bg = (R, G, B)
            ui.userListBottomBorder.bg = (R, G, B)
            ui.userListLeftBorder.bg = (R, G, B)
            ui.messageInputTopBorder.bg = (R, G, B)
            ui.messageInputRightBorder.bg = (R, G, B)
            ui.messageInputBottomBorder.bg = (R, G, B)
            ui.messageInputLeftBorder.bg = (R, G, B)

        ui.animationColor = newColor

    @staticmethod
    def animateHeaderInSetup(message):
        # Code 5

        if ui.LDM is False:
            (R, G, B) = ui.lightbg

            while (R, G, B) != ui.animationColor:
                # Text fades from white to color
                if R < ui.animationColor[0]:
                    R += 1
                if G < ui.animationColor[1]:
                    G += 1
                if B < ui.animationColor[2]:
                    B += 1
                if R > ui.animationColor[0]:
                    R -= 1
                if G > ui.animationColor[1]:
                    G -= 1
                if B > ui.animationColor[2]:
                    B -= 1

                ui.status.text_color = (R, G, B)
                sleep(ui.rate)

            ui.status.value = message

            while (R, G, B) != ui.lightbg:
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

                ui.status.text_color = (R, G, B)
                sleep(ui.rate)

        else:
            ui.status.value = message

    @staticmethod
    def fadeColorsInSetup(newColor):
        # Code 6

        if ui.LDM is False:
            (R, G, B) = ui.color

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

                ui.inputTextBox.text_color = (R, G, B)
                ui.currentText.text_color = (R, G, B)
                ui.status.bg = (R, G, B)

                sleep(ui.rate)

        else:
            (R, G, B) = newColor

            ui.inputTextBox.text_color = (R, G, B)
            ui.currentText.text_color = (R, G, B)
            ui.status.bg = (R, G, B)

        ui.color = newColor
        ui.animationColor = newColor

    @staticmethod
    def fadeIndicator(key, newColor):
        # Code 7

        if key == 0:
            (R, G, B) = web_to_rgb(ui.usernameIndicator.bg)

        elif key == 1:
            (R, G, B) = web_to_rgb(ui.colorIndicator.bg)

        elif key == 2:
            (R, G, B) = web_to_rgb(ui.hostIndicator.bg)

        elif key == 3:
            (R, G, B) = web_to_rgb(ui.portIndicator.bg)

        elif key == 4:
            (R, G, B) = web_to_rgb(ui.publicKeyIndicator.bg)

        elif key == 5:
            (R, G, B) = web_to_rgb(ui.privateKeyIndicator.bg)

        elif key == 6:
            (R, G, B) = web_to_rgb(ui.cipherKeyIndicator.bg)

        else:
            raise ValueError("Invalid indexing of indicators")

        if ui.LDM is False:

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
                    ui.usernameIndicator.bg = (R, G, B)

                elif key == 1:
                    ui.colorIndicator.bg = (R, G, B)

                elif key == 2:
                    ui.hostIndicator.bg = (R, G, B)

                elif key == 3:
                    ui.portIndicator.bg = (R, G, B)

                elif key == 4:
                    ui.publicKeyIndicator.bg = (R, G, B)

                elif key == 5:
                    ui.privateKeyIndicator.bg = (R, G, B)

                elif key == 6:
                    ui.cipherKeyIndicator.bg = (R, G, B)

                sleep(ui.rate)

        else:
            (R, G, B) = newColor

            if key == 0:
                ui.usernameIndicator.bg = (R, G, B)

            elif key == 1:
                ui.colorIndicator.bg = (R, G, B)

            elif key == 2:
                ui.hostIndicator.bg = (R, G, B)

            elif key == 3:
                ui.portIndicator.bg = (R, G, B)

            elif key == 4:
                ui.publicKeyIndicator.bg = (R, G, B)

            elif key == 5:
                ui.privateKeyIndicator.bg = (R, G, B)

            elif key == 6:
                ui.cipherKeyIndicator.bg = (R, G, B)

    @staticmethod
    def animateAfterInputInSetup(newColor):
        # Code 8

        if ui.LDM is False:
            (R, G, B) = ui.darkbg

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

                ui.inputTextBox.bg = (R, G, B)

                sleep(ui.rate)

            while (R, G, B) != ui.darkbg:
                if R > ui.darkbg[0]:
                    R -= 1
                if G > ui.darkbg[1]:
                    G -= 1
                if B > ui.darkbg[2]:
                    B -= 1
                if R < ui.darkbg[0]:
                    R += 1
                if G < ui.darkbg[1]:
                    G += 1
                if B < ui.darkbg[2]:
                    B += 1

                ui.inputTextBox.bg = (R, G, B)

                sleep(ui.rate)

    @staticmethod
    def animateAfterInputInChat(newColor):
        # Code 9

        if ui.LDM is False:
            if ui.darkMode is True:
                (R, G, B) = ui.darkbg

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

                    ui.messageInput.bg = (R, G, B)

                    sleep(ui.rate)

                while (R, G, B) != ui.darkbg:
                    if R > ui.darkbg[0]:
                        R -= 1
                    if G > ui.darkbg[1]:
                        G -= 1
                    if B > ui.darkbg[2]:
                        B -= 1
                    if R < ui.darkbg[0]:
                        R += 1
                    if G < ui.darkbg[1]:
                        G += 1
                    if B < ui.darkbg[2]:
                        B += 1

                    ui.messageInput.bg = (R, G, B)

                    sleep(ui.rate)

            else:
                (R, G, B) = ui.lightbg

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

                    ui.messageInput.bg = (R, G, B)

                    sleep(ui.rate)

                while (R, G, B) != ui.lightbg:
                    if R > ui.bg[0]:
                        R -= 1
                    if G > ui.bg[1]:
                        G -= 1
                    if B > ui.bg[2]:
                        B -= 1
                    if R < ui.bg[0]:
                        R += 1
                    if G < ui.bg[1]:
                        G += 1
                    if B < ui.bg[2]:
                        B += 1

                    ui.messageInput.bg = (R, G, B)

                    sleep(ui.rate)

    @staticmethod
    def animateCurrenttext(message):
        # Code 10

        if ui.LDM is False:
            (R, G, B) = ui.animationColor

            while (R, G, B) != ui.bg:
                # Text fades from color to grey
                if R < ui.bg[0]:
                    R += 1
                if G < ui.bg[1]:
                    G += 1
                if B < ui.bg[2]:
                    B += 1
                if R > ui.bg[0]:
                    R -= 1
                if G > ui.bg[1]:
                    G -= 1
                if B > ui.bg[2]:
                    B -= 1

                ui.currentText.text_color = (R, G, B)
                sleep(ui.rate)

            ui.currentText.value = message

            while (R, G, B) != ui.animationColor:
                # Text fades from grey to color
                if R < ui.animationColor[0]:
                    R += 1
                if G < ui.animationColor[1]:
                    G += 1
                if B < ui.animationColor[2]:
                    B += 1
                if R > ui.animationColor[0]:
                    R -= 1
                if G > ui.animationColor[1]:
                    G -= 1
                if B > ui.animationColor[2]:
                    B -= 1

                ui.currentText.text_color = (R, G, B)
                sleep(ui.rate)

        else:
            ui.currentText.value = message

    def animationThread(self):
        # This thread runs indefinitely and checks the queue for list items, calling
        # The format for this thread is [[Class animation method code, *args]]
        while True:
            if self.queue:
                # Check if queue has duplicate items
                while len(self.queue) > 1 and self.queue[0] == self.queue[1]:
                    self.queue.pop(1)

                if self.queue[0][0] == 1:
                    # Dynamically adjust the animation duration based on length of the message
                    if len(str(self.queue[0][0])) < 10:
                        self.waitMultiplier = 2.0
                    elif len(str(self.queue[0][0])) < 15:
                        self.waitMultiplier = 2.5
                    else:
                        self.waitMultiplier = 3.0

                    self.animateHeaderInChat(self.queue[0][1])

                elif self.queue[0][0] == 2:
                    if (ui.darkMode is True and ui.color == ui.lightbg) \
                            or (ui.darkMode is True and ui.animationColor == ui.lightbg) \
                            or (ui.darkMode is False and ui.color == (0, 0, 0)) \
                            or (ui.darkMode is False and ui.animationColor == (0, 0, 0)):

                        self.queue.append([1, "You cannot change the theme due to contrast"])

                    else:
                        self.switchTheme()

                elif self.queue[0][0] == 3:
                    self.fadeColorsInChat(self.queue[0][1])

                elif self.queue[0][0] == 4:
                    self.fadeBordersInChat(self.queue[0][1])

                elif self.queue[0][0] == 5:
                    if connection.accepted is False:
                        self.animateHeaderInSetup(self.queue[0][1])

                elif self.queue[0][0] == 6:
                    if connection.accepted is False:
                        self.fadeColorsInSetup(self.queue[0][1])

                elif self.queue[0][0] == 7:
                    if connection.accepted is False:
                        self.fadeIndicator(self.queue[0][1], self.queue[0][2])

                elif self.queue[0][0] == 8:
                    if connection.accepted is False:
                        self.animateAfterInputInSetup(self.queue[0][1])

                elif self.queue[0][0] == 9:
                    self.animateAfterInputInChat(self.queue[0][1])

                elif self.queue[0][0] == 10:
                    if connection.accepted is False:
                        self.animateCurrenttext(self.queue[0][1])

                self.queue.pop(0)


class Communication:
    # This handles all the communication from and to the server using the socket class
    # The indefinte thread (update thread) receives all the communication whilst the main thread
    # sends to the server. This class also handles the encyrption and decryption of the messages
    # being sent and received, and processes them as messages or commands accordingly
    # This class also appends all messages received into chatHistory and transcript, where
    # chatHistory stores every message and transcript is a 2D list of messages indexed by page

    def __init__(self):
        self.users = []
        self.chatHistory = []
        self.transcript = [[]]
        self.page = 0

    @staticmethod
    def getrsaEncryptedMessage(key, e, N):
        # Used to encrypt the keys
        newKey = pow(key, e, N)

        return newKey

    @staticmethod
    def getrsaDecryptedMessage(key, d, N):
        # Used to decrypt the keys
        newKey = pow(key, d, N)

        return newKey

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

    def setChatHistoryFile(self, location):
        # Called by /savechat [Location]
        if location and " " not in location:
            with open(location, "w") as file:
                for chatLine in self.chatHistory:
                    file.write(chatLine + "\n")
                file.close()

                animation.queue.append([1, f"Your file has been saved in {str(location)}"])

        else:
            animation.queue.append([1, "You can't save to this location"])

    def setMessageToSend(self, message):
        # Gets the value of the input, encrypts, then broadcasts
        try:
            if message:
                if message == "/leave":
                    connection.leave()

                else:
                    connection.socket.send(self.getCaesarEncryptedMessage(message, connection.cipherKey)
                                                   .encode())

                    ui.setMessageInputAsEmpty()

        except BrokenPipeError as e:
            print(f"An error occured: {e}")
            connection.leave()

    def setUsers(self, users):
        # Called by /add [Users spilt by space], adds every user that are currently online
        users = users.split()
        users.sort()

        if connection.inputs[0] in users:
            # If user is the client itself
            if connection.accepted is None:
                # If the user is being accepted for the first time (as the username has been accepted)
                ui.openChat()

                connection.accepted = True

        ui.setUserListAsEmpty()

        for user in users:
            if user not in self.users:
                self.users.append(user)

                ui.setUsers(user)

            else:
                ui.userList.append(user)

    def setRemovedUser(self, user):
        # Called by /remove [Users split by space], removes user from the list of users online (locally)
        try:
            self.users.remove(user)

            ui.setRemovedUser(user)

        except ValueError as e:
            print(f"An error occured in removeUser: {e}")

    def getPreviousPage(self):
        # Called by /previous, loads the previous page if its not page 0
        if self.page > 0:
            self.page -= 1

            # Tell the UI to display the previous page
            ui.getPreviousPage(self.transcript[self.page])

        else:
            animation.queue.append([1, "You cannot go below this page"])

    def getNextPage(self):
        # Called by /next, loads the next page if its been generated
        if self.page < ui.page:
            self.page += 1

            # Tell the UI to display the next page
            ui.getNextPage(self.transcript[self.page])

        else:
            animation.queue.append([1, "You are at the highest page"])

    def getNewPage(self, message):
        # Sends the client to the new current page and shows input
        self.transcript.append([message])
        self.page = ui.page + 1

        ui.getNewPage(message)

    def setMessage(self, message):
        # Called when the message is not a command
        if ui.linesSent >= ui.linesLimit:
            self.getNewPage(message)

        else:
            # Received input
            self.chatHistory.append(strftime("%H:%M:%S", localtime()) + " {message}")
            if ui.linesSent == 0:
                # Only true for the very first message
                self.transcript[ui.page].append(message)

                ui.setFirstMessage(message)

            else:
                if self.page == ui.page:
                    # If you are viewing the current page then
                    self.transcript[ui.page].append(message)

                    ui.setSubsequentMessage(message)

                else:
                    # If you are viewing an older page then load current page then show input
                    self.page = ui.page

                    ui.setFirstMessage(self.transcript[self.page][0])

                    for line in self.transcript[self.page][1:]:
                        ui.setSubsequentMessage(line)

                    if ui.linesSent >= ui.linesLimit:
                        # If the current page has no space left
                        self.getNewPage(message)

                    else:
                        self.transcript[ui.page].append(message)

                        ui.setSubsequentMessage(message)

    def updateThread(self):
        # Starts when the user is connected and runs indefinitely
        # Looks out for server broadcasts
        while True:
            try:
                message = self.getCaesarDecryptedMessage(connection.socket.recv(1024).decode(),
                                                         connection.cipherKey)

                if message:
                    print(f"Received message: {message}")

                    if message[0:8] == "/display":
                        animation.queue.append([1, message[9:]])

                    elif message == "/theme":
                        animation.queue.append([2])

                    elif message == "/ldm":
                        ui.setLDM()

                    elif message[0:6] == "/color":
                        val = ui.setColor(message[7:])

                        if val is not None:
                            animation.queue.append([3, val])

                    elif message[0:7] == "/border":
                        val = ui.setColor(message[8:])

                        if val is not None:
                            animation.queue.append([4, val])

                    elif message == "/reject":
                        connection.accepted = False
                        connection.setInputsAsNone("an invalid username")

                    elif message[0:8] == "/timeout":
                        animation.queue.append([9, (255, 0, 0)])
                        animation.queue.append([1, message[9:]])

                    elif message == "/next":
                        self.getNextPage()

                    elif message == "/previous":
                        self.getPreviousPage()

                    elif message[0:7] == "/accept":
                        self.setUsers(message[8:])

                    elif message[0:7] == "/remove":
                        self.setRemovedUser(message[8:])

                    elif message[0:9] == "/savechat":
                        self.setChatHistoryFile(message[10:])

                    else:
                        self.setMessage(message)

            except (ConnectionResetError, OSError):
                print("Closed update thread")

                connection.leave()

                break


class Connection:
    # Handles the socket connection with the server, decryption and formatting of the keys
    # And starting the update thread in the communication class once
    def __init__(self):
        # Inputs list such that its formatted as [username, color, host, port, public key, private key, encrypted cipher key]
        self.inputs = [None for i in range(7)]

        # Attributes
        # Connected = when the client connects to the server
        # Accepted = when the username sent has been accepted (None means pending)
        self.socket = socket()
        self.e = None
        self.d = None
        self.N = None
        self.cipherKey = None
        self.connected = False
        self.accepted = False
        self.threadInitialized = False
        self.mod = False
        self.inputRequest = 0

    def setConnection(self):
        # Called when the user has filled out all 7 inputs
        # Connects to the socket, calculates the RSA encryption key, decryption key, and
        # The cipher key.

        try:
            # Inherit the inputted colors to the UI
            ui.color = self.inputs[1]
            ui.animationColor = self.inputs[1]

            # Decouple the public and private keys
            # Decrypt the cipher key
            self.e = int(str(self.inputs[4][0:6]), base=10)
            self.d = int(str(self.inputs[5][0:6]), base=10)
            self.N = int(str(self.inputs[5][6:12]), base=10)
            self.cipherKey = communication.getrsaDecryptedMessage(int(self.inputs[6], base=10), self.d, self.N)

        except ValueError:
            self.setInputsAsNone("invalid keys")

        else:
            try:
                if self.connected is False:
                    # Connect to the server socket once (ever)
                    self.socket.connect((self.inputs[2], int(self.inputs[3], base=10)))
                    self.connected = True

                if self.accepted is False:
                    # Send username to determine if it's acceptable
                    self.socket.send(communication.getCaesarEncryptedMessage(self.inputs[0], self.cipherKey)
                                     .encode())
                    self.accepted = None

                if self.threadInitialized is False:
                    # If the thread has not started, start it once
                    Thread(target=communication.updateThread).start()
                    self.threadInitialized = True

            except (ValueError, TypeError, OverflowError):
                self.setInputsAsNone("an invalid host/ port")

            except (ConnectionRefusedError, OSError, TimeoutError):
                self.setInputsAsNone("a connection error")

    def setInputsAsNone(self, message):
        # Reset inputs in terms of variables and data
        self.inputs = [None for i in range(7)]

        # Reset indicators and UI elements, indicating the error
        ui.setInputsAsNone(message)

    def leave(self):
        # Alert the server that the client is disconnecting, then close the socket
        if connection.connected is True:
            self.socket.send(communication.getCaesarDecryptedMessage("/leave", self.cipherKey).encode())
            self.socket.close()

        ui.leave()


class UI:
    # Handles all interaction with the UI elements, as well as create them
    # The setup window will require input handling to establish a connection (username, host ip etc)
    # Whereas the chatroom window will require input handling to send messages/ commands
    def __init__(self):
        # UI elements (setup)
        self.setupWindow = None
        self.inputTextBox = None
        self.status = None
        self.usernameIndicator = None
        self.colorIndicator = None
        self.hostIndicator = None
        self.portIndicator = None
        self.publicKeyIndicator = None
        self.privateKeyIndicator = None
        self.cipherKeyIndicator = None
        self.currentText = None

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
        self.lightbg = (255, 255, 255)
        self.waitTime = 1
        self.page = 0
        self.linesSent = 0
        self.darkMode = True
        self.hasRequestedInput = False

        # Font sizes list for different OS's
        # [n][0] (so index 0 of every list item) is the appropriate list of font sizes for macOS
        # [n][1] is the appropriate list of font sizes on every other OS
        self.fontSizes = [[22, 17], [36, 26], [24, 19], [32, 28], [32, 23], [22, 19], [24, 17], [22, 19]]

        # Messages List
        # Where [1][n] is the default request message, and [n][1] is the failing message
        self.getInputsMessages = [["Choose a username", "Try a different username"],
                                  ["Choose a color", "Try a different color"],
                                  ["Enter the host IP", "Try a different IP"],
                                  ["Enter the host port", "Try a different port"],
                                  ["Enter the public key", "Try a different public key"],
                                  ["Enter the private key", "Try a different private key"],
                                  ["Enter the cipher key", "Try a different cipher key"]]

        if self.darkMode is True:
            self.themeDependentBg = self.darkbg

        else:
            self.themeDependentBg = self.lightbg

        if system() == "Darwin":
            # For macOS
            self.fontIndex = 0
            self.linesLimit = 19
            self.rate = 0.00035
            self.LDM = False

        else:
            # For other platforms
            self.fontIndex = 1
            self.linesLimit = 18
            self.rate = None
            self.LDM = True

            print("Unfortunately your system does not support animations, and they have been disabled.")

        if __name__ == "__main__":
            # EnableUI displays UI elements and sets their attributes
            self.enableUI = True

        else:
            # Disabling this prevents attribute errors with UI elements that don't exist, and is only used in testing
            self.enableUI = False

    # Methods below alter UI attributes

    def setColor(self, message):
        # Called by /color [Color], and returns a color
        try:
            color = web_to_rgb(message)

            if (self.darkMode is True and color == (0, 0, 0)) or \
                    (self.darkMode is False and color == self.lightbg):
                animation.queue.append([1, "You cannot do this due to contrast"])

                return None

            else:
                return color

        except ValueError:
            animation.queue.append([1, "You cannot use this color as it is undefined"])

            return None

    def setLDM(self):
        # Called by /ldm and changes light mode to dark mode and vice versa
        if system() == "Darwin":
            # For macOS
            if self.LDM is True:
                animation.queue.append([1, "You turned LDM off"])

                self.LDM = False

            else:
                animation.queue.append([1, "You turned LDM on"])

                self.LDM = True

        else:
            animation.queue.append([1, "Animations are disabled on your OS."])

    def getPreviousPage(self, transcript):
        # Called by /previous. Clears the page, then set the first message as "value"
        if self.enableUI is True:
            self.chatHistory.clear()
            self.chatHistory.value = transcript[0]

            for line in transcript[1:]:
                # For every subsequent message, append to the list
                self.chatHistory.append(line)

        if self.LDM is False:
            # Let the user know which page they're on
            animation.queue.append(
                [1, f"You are on page {str(communication.page + 1)} of {str(self.page + 1)}"])

    def getNextPage(self, transcript):
        # Called by /next. Clears the page, then set the first message as "value"
        if self.enableUI is True:
            self.chatHistory.clear()
            self.chatHistory.value = transcript[0]

            for line in transcript[1:]:
                self.chatHistory.append(line)

        if self.LDM is False:
            animation.queue.append(
                [1, f"You are on page {str(communication.page + 1)} of {str(self.page + 1)}"])

    def getNewPage(self, message):
        # Called when the messages on 1 page exceeds the lineslimit
        if self.enableUI is True:
            self.chatHistory.clear()
            self.chatHistory.value = message

        self.page += 1
        self.linesSent = 1

    def setFirstMessage(self, message):
        # When displaying the first message, the value attribute is changed
        if self.enableUI is True:
            self.chatHistory.clear()
            self.chatHistory.value = message

        self.linesSent += 1

    def setSubsequentMessage(self, message):
        # When displaying subsequent messages, the append method is used instead
        if self.enableUI is True:
            self.chatHistory.append(message)

        self.linesSent += 1

    def setUsers(self, user):
        # Called iteratively when a new user is connected, adds every user in the list to the UI
        if self.enableUI is True:
            self.userList.append(user)

        animation.queue.append([1, f"{str(user)} has connected"])

    def setRemovedUser(self, user):
        # Called when a user that's not the client running disconnects, and displays the changes to the UI
        if self.enableUI is True:
            self.userList.remove(user)

        animation.queue.append([1, f"{user} has disconnected"])

    def setUserListAsEmpty(self):
        if self.enableUI is True:
            self.userList.clear()
            self.userList.append("Users online:")

    def setMessageInputAsEmpty(self):
        if self.enableUI is True:
            self.messageInput.clear()

    def leave(self):
        # Is almost always called from the connection leaving method, but could be called
        # Directly when kicked to prevent a doubled "/remove" call
        if connection.accepted is True:
            self.chatWindow.exit_full_screen()
            self.chatWindow.destroy()

        else:
            self.setupWindow.destroy()

    def receivedInvalidInput(self, check):
        # Create an animation to indicate an unsucessful input
        # Create red flash in textbox
        # Display an error message
        # Update completed inputs counter

        animation.queue.append([8, (255, 0, 0)])
        animation.queue.append([5, self.getInputsMessages[check][1]])
        animation.queue.append(
            [10, f"{(7 - connection.inputs.count(None))} of 7 inputs completed"])

    def setInputsAsNone(self, message):
        # Resets the 7 inputs
        # Resets every indiactor to be invisible
        for indicator in range(7):
            animation.queue.append([7, indicator, self.bg])

        # Create a white block cursor for the input after the last one inputted
        for check in range(7):
            if connection.inputRequest == check:
                animation.queue.append([7, check, self.lightbg])

        # Reset the inherited colors and fade to the default colors
        # The animation resets color and animationcolor after running the animation
        animation.queue.append([6, (173, 216, 230)])

        # Reset currentText and create warning
        animation.queue.append([10, f"Inputs reset due to {message}"])

    # Gets the 7 inputs
    def getInputs(self, check, key, value):
        if self.hasRequestedInput is False or key is False:
            # Create an animation to indicate an input request
            # Display an input request
            # Update completed inputs counter
            animation.queue.append([5, self.getInputsMessages[check][0]])
            animation.queue.append([10, f"{(7 - connection.inputs.count(None))} of 7 inputs completed"])

            self.hasRequestedInput = True

        else:
            if not value:
                self.receivedInvalidInput(check)

            else:
                # If the requested input is color
                if check == 1:
                    try:
                        color = web_to_rgb(value)

                        # Prevent matching background and text colors
                        if color == self.lightbg or color == (255, 0, 0):
                            self.receivedInvalidInput(check)

                        else:
                            # The inputted color is accepted, and the UI elements will fade to this new color
                            animation.queue.append([6, color])

                            return color

                    except ValueError:
                        self.receivedInvalidInput(check)

                else:
                    return value

        return None

    def setInputGetter(self, key, value):
        if connection.accepted is False:
            # Creates a series of input requests
            for check in range(7):
                if connection.inputRequest == check:
                    val = self.getInputs(check, key, value)

                    # Get best value (where None is worse than any username)
                    if val is not None:
                        connection.inputs[check] = val
                        connection.inputRequest += 1

                        # Create an animation to indicate a successful input
                        if connection.inputs[1] is not None:
                            # Use the inputted color if given, otherwise use the default lightblue
                            animation.queue.append([8, connection.inputs[1]])

                        else:
                            animation.queue.append([8, self.animationColor])

                        self.hasRequestedInput = False

                    # For testing, UI elements are inaccessible
                    if self.enableUI is True:
                        self.inputTextBox.clear()

                    # Creates white block cursor
                    animation.queue.append([7, check, self.lightbg])

            # Marks every completed input with color
            for check in range(7):
                if connection.inputs[check] and not connection.inputRequest == check:

                    # Use the inputted color if given, otherwise use the default lightblue
                    if connection.inputs[1] is not None:
                        animation.queue.append([7, check, connection.inputs[1]])

                    else:
                        # Copies the default color into the inputs list
                        animation.queue.append([7, check, self.animationColor])

            if connection.inputRequest < 0:
                # To cycle back the cursor when the index reaches below 0
                connection.inputRequest = 6
                self.setInputGetter(key, value)

            if connection.inputRequest > 6:
                # To cycle back the cursor when the index reaches above 6
                connection.inputRequest = 0
                self.setInputGetter(key, value)

            if all(check is not None for check in connection.inputs) and key is True and self.enableUI is True:
                # Connect to the server given every input is valid
                connection.setConnection()

    def setKeyPressed(self, event):
        # Detects key presses with emphasis on enter, escape, left and right
        if event:
            # Left and right keys bypass all if statements in getInputs, therefore will request for inputs every time
            # Whereas enter key does not bypass (as it is True), so it may request with the "try again" message
            # Escape exits full screen
            if event.tk_event.keysym == "Left":
                if 7 > connection.inputRequest > -1:
                    animation.queue.append([7, connection.inputRequest, self.bg])

                    connection.inputRequest -= 1

                    self.setInputGetter(False, self.inputTextBox.value)

            if event.tk_event.keysym == "Right":
                if 7 > connection.inputRequest > -1:
                    animation.queue.append([7, connection.inputRequest, self.bg])

                    connection.inputRequest += 1

                    self.setInputGetter(False, self.inputTextBox.value)

            if event.tk_event.keysym == "Return":
                if connection.accepted:
                    communication.setMessageToSend(self.messageInput.value)

                else:
                    self.setInputGetter(True, self.inputTextBox.value)

            if event.tk_event.keysym == "Escape":
                if connection.accepted:
                    self.chatWindow.exit_full_screen()

            else:
                if connection.accepted is True:
                    self.messageInput.focus()

                else:
                    self.inputTextBox.focus()

    # Methods below create the UI

    def openChat(self):
        # Creates chat window
        self.chatWindow = Window(self.setupWindow, width=1280, height=720, title="Chatroom", bg=self.bg)
        self.chatWindow.when_closed = connection.leave
        self.chatWindow.when_key_pressed = self.setKeyPressed
        self.chatWindow.set_full_screen()

        # Creates 4 gray borders on the edges of the screen
        topPadding = Box(self.chatWindow, width="fill", height=50, align="top")
        leftPadding = Box(self.chatWindow, width=50, height="fill", align="left")
        rightPadding = Box(self.chatWindow, width=50, height="fill", align="right")
        bottomPadding = Box(self.chatWindow, width="fill", height=50, align="bottom")

        # Creates a box from the remaining space left
        self.border = Box(self.chatWindow, width="fill", height="fill")

        # Creates a header that displays notifications
        header = Box(self.border, width="fill", height=50, align="top")
        headerBlocker = Box(self.border, width="fill", height=50, align="top")

        # Creates a listbox that displays a list of connected users
        userListBox = Box(self.border, width=170, height="fill", align="left")
        userListBlocker = Box(self.border, width=50, height="fill", align="left")

        # Creates a listbox that displays the messages up to around 18 at any time
        userBox = Box(self.border, width="fill", height="fill", align="right")

        inputBox = Box(userBox, width="fill", height=120, align="bottom")

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
        self.userList.bg = self.themeDependentBg

        self.header = Text(header, text=f"Welcome {connection.inputs[0]}", width="fill", height=50)
        self.header.text_color = self.themeDependentBg
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
        self.chatHistory.bg = self.themeDependentBg
        self.chatHistory.disable()

        # Creates a textbox to type in
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
        self.messageInput.bg = self.themeDependentBg
        self.messageInput.when_key_pressed = self.setKeyPressed

        self.setupWindow.hide()
        self.chatWindow.show()

    def openSetup(self):
        # Creates setup window
        self.setupWindow = App(title="Setup", width=800, height=275)
        self.setupWindow.bg = self.bg
        self.setupWindow.font = self.font
        self.setupWindow.when_closed = connection.leave
        self.setupWindow.when_key_pressed = self.setKeyPressed

        # Creates 2 gray borders on the top and bottom edges
        topPadding = Box(self.setupWindow, width="fill", height=50, align="top")
        bottomPadding = Box(self.setupWindow, width="fill", height=50, align="bottom")
        contents = Box(self.setupWindow, width="fill", height="fill", align="top")

        # Creates a header that displays messages
        header = Box(contents, width="fill", height=40, align="top")

        # Creates a row of space that contains indicators, used to display completed and in progress inputs
        indicator = Box(contents, width="fill", height=40, align="bottom")

        rightPadding = Box(contents, width=20, height="fill", align="right")
        leftPadding = Box(contents, width=10, height="fill", align="left")

        self.status = Text(header, text="Press Enter to begin", width="fill", height=40)
        self.status.text_color = self.lightbg
        self.status.text_size = self.fontSizes[4][self.fontIndex]
        self.status.bg = self.animationColor

        statusPadding = Box(contents, width="fill", height=30, align="top")

        # Creates a textbox to type into
        self.inputTextBox = TextBox(contents, width=30)
        self.inputTextBox.text_color = self.color
        self.inputTextBox.text_size = self.fontSizes[5][self.fontIndex]
        self.inputTextBox.bg = self.darkbg

        self.usernameIndicator = Box(indicator, width=114, height="fill", align="left")
        self.colorIndicator = Box(indicator, width=114, height="fill", align="left")
        self.hostIndicator = Box(indicator, width=114, height="fill", align="left")
        self.portIndicator = Box(indicator, width=114, height="fill", align="left")
        self.publicKeyIndicator = Box(indicator, width=114, height="fill", align="left")
        self.privateKeyIndicator = Box(indicator, width=114, height="fill", align="left")
        self.cipherKeyIndicator = Box(indicator, width=114, height="fill", align="left")

        self.currentText = Text(bottomPadding, text="", width="fill", height=20)
        self.currentText.text_color = self.color
        self.currentText.text_size = self.fontSizes[7][self.fontIndex]

        # Initialize the animation thread upon starting the code
        Thread(target=animation.animationThread).start()

        self.setupWindow.display()


if __name__ == '__main__':
    animation = Animation()
    communication = Communication()
    connection = Connection()
    ui = UI()

    ui.openSetup()
