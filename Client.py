# 25/9/2022
# V13 Beta

import platform
import socket
import colorutils
import sys
from time import sleep, localtime, strftime
from threading import Thread
from guizero import *

class Animation:
    def __init__(self):
        self.runFiller = False
        self.animationRunning = False
        self.readRate = 1

    def animateStatus(self):
        try:
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
                    sleep(uiInstance.rate * 20)

                sleep(self.readRate)

        except Exception as e:
            if connectionInstance.connected:
                print(e)
            else:
                print("Closed thread successfully")

        finally:
            return

    def filler(self, displayMessage):
        try:
            if displayMessage:
                animateThread = Thread(target=self.animateHeader,
                                       args=["You turned filler on", uiInstance.animationColor])
                animateThread.start()

            while animationInstance.runFiller:
                while animationInstance.animationRunning:
                    sleep(uiInstance.waitTime)

                sleep(60)

                time = strftime("%H:%M", localtime())
                animateThread = Thread(target=self.animateHeader, args=[str(time), uiInstance.animationColor])
                animateThread.start()

            animateThread = Thread(target=animationInstance.animateHeader, args=["You turned filler off",
                                                                                 uiInstance.animationColor])
            animateThread.start()

        except Exception as e:
            if connectionInstance.connected:
                print(e)
            else:
                print("Closed thread successfully")

        finally:
            animationInstance.runFiller = False
            return

    def changeBorder(self):
        try:
            while animationInstance.animationRunning:
                sleep(uiInstance.waitTime)
            animationInstance.animationRunning = True

            (R, G, B) = (173, 216, 230)

            while not (R, G, B) == uiInstance.animationColor:
                if R < 240:
                    R += 1
                if G < 230:
                    G += 1
                if B > 140:
                    B -= 1

                uiInstance.chatHistoryTopBorder.bg = (R, G, B)
                uiInstance.userListTopBorder.bg = (R, G, B)
                uiInstance.messageInputTopBorder.bg = (R, G, B)

                sleep(uiInstance.rate)

            (R, G, B) = (173, 216, 230)

            while not (R, G, B) == uiInstance.animationColor:
                if R < 240:
                    R += 1
                if G < 230:
                    G += 1
                if B > 140:
                    B -= 1

                uiInstance.chatHistoryRightBorder.bg = (R, G, B)
                uiInstance.userListRightBorder.bg = (R, G, B)
                uiInstance.messageInputRightBorder.bg = (R, G, B)

                sleep(uiInstance.rate)

            (R, G, B) = (173, 216, 230)

            while not (R, G, B) == uiInstance.animationColor:
                if R < 240:
                    R += 1
                if G < 230:
                    G += 1
                if B > 140:
                    B -= 1

                uiInstance.chatHistoryBottomBorder.bg = (R, G, B)
                uiInstance.userListBottomBorder.bg = (R, G, B)
                uiInstance.messageInputBottomBorder.bg = (R, G, B)

                sleep(uiInstance.rate)

            (R, G, B) = (173, 216, 230)

            while not (R, G, B) == uiInstance.animationColor:
                if R < 240:
                    R += 1
                if G < 230:
                    G += 1
                if B > 140:
                    B -= 1

                uiInstance.chatHistoryLeftBorder.bg = (R, G, B)
                uiInstance.userListLeftBorder.bg = (R, G, B)
                uiInstance.messageInputLeftBorder.bg = (R, G, B)

                sleep(uiInstance.rate)

        except Exception as e:
            if connectionInstance.connected:
                print(e)
            else:
                print("Closed thread successfully")

        finally:
            animationInstance.animationRunning = False
            return

    def fadeColor(self, newColor, displayMessage):
        try:

            if newColor == (240, 230, 140) and not connectionInstance.mod:
                animateThread = Thread(target=self.animateHeader,
                                       args=["You don't have the power to use this color", uiInstance.animationColor])
                animateThread.start()
                return

            if uiInstance.color == newColor and displayMessage:
                animateThread = Thread(target=self.animateHeader,
                                       args=["You can't change to the same color", uiInstance.animationColor])
                animateThread.start()
                return

            while animationInstance.animationRunning:
                sleep(uiInstance.waitTime)
            animationInstance.animationRunning = True

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

            if displayMessage:
                animateThread = Thread(target=self.animateHeader,
                                       args=["You changed the text color", uiInstance.animationColor])
                animateThread.start()

            # Once completed
            uiInstance.color = newColor

        except Exception as e:
            if connectionInstance.connected:
                animateThread = Thread(target=self.animateHeader, args=["You cannot use an undefined color",
                                                                        uiInstance.animationColor])
                animateThread.start()
                print(e)
            else:
                print("Closed thread successfully")

        finally:
            animationInstance.animationRunning = False
            return

    def animateHeader(self, message, color):
        try:
            if len(message) < 10:
                waitMultiplier = 1.0
            elif len(message) < 15:
                waitMultiplier = 1.5
            else:
                waitMultiplier = 2.0

            while animationInstance.animationRunning:
                sleep(uiInstance.waitTime)
            animationInstance.animationRunning = True

            if not uiInstance.darkMode:
                (R, G, B) = (255, 255, 255)

                while not R == color[0] or not G == color[1] or not B == color[2]:
                    # Text fades from white to color
                    if R < color[0]:
                        R += 1
                    if G < color[1]:
                        G += 1
                    if B < color[2]:
                        B += 1
                    if R > color[0]:
                        R -= 1
                    if G > color[1]:
                        G -= 1
                    if B > color[2]:
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

                sleep(self.readRate * waitMultiplier)

                while not R == color[0] or not G == color[1] or not B == color[2]:
                    # Fades background from white to color
                    if R < color[0]:
                        R += 1
                    if G < color[1]:
                        G += 1
                    if B < color[2]:
                        B += 1
                    if R > color[0]:
                        R -= 1
                    if G > color[1]:
                        G -= 1
                    if B > color[2]:
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

                while not R == color[0] or not G == color[1] or not B == color[2]:
                    # Text fades from black to color
                    if R < color[0]:
                        R += 1
                    if G < color[1]:
                        G += 1
                    if B < color[2]:
                        B += 1
                    if R > color[0]:
                        R -= 1
                    if G > color[1]:
                        G -= 1
                    if B > color[2]:
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

                sleep(self.readRate * waitMultiplier)

                while not R == color[0] or not G == color[1] or not B == color[2]:
                    # Fades background from black to color
                    if R > color[0]:
                        R -= 1
                    if G > color[1]:
                        G -= 1
                    if B > color[2]:
                        B -= 1
                    if R < color[0]:
                        R += 1
                    if G < color[1]:
                        G += 1
                    if B < color[2]:
                        B += 1

                    uiInstance.header.bg = (R, G, B)
                    sleep(uiInstance.rate)

                uiInstance.header.value = "Welcome " + connectionInstance.username

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

        except Exception as e:
            if connectionInstance.connected:
                print(e)
            else:
                print("Closed thread successfully")

        finally:
            animationInstance.animationRunning = False
            return

    def switchTheme(self, displayMessage):
        try:
            while animationInstance.animationRunning:
                sleep(uiInstance.waitTime)
            animationInstance.animationRunning = True

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

            uiInstance.chatHistory.text_color = uiInstance.color
            uiInstance.messageInput.text_color = uiInstance.color

            if displayMessage:
                if uiInstance.darkMode:
                    animateThread = Thread(target=self.animateHeader,
                                           args=["You turned dark mode on", uiInstance.animationColor])
                    animateThread.start()
                else:
                    animateThread = Thread(target=self.animateHeader,
                                           args=["You turned light mode on", uiInstance.animationColor])
                    animateThread.start()

        except Exception as e:
            if connectionInstance.connected:
                print(e)
            else:
                print("Closed thread successfully")

        finally:
            animationInstance.animationRunning = False
            return

class Communication:
    def __init__(self):
        self.users = []
        self.chatHistory = []

    def decrypt(self, message):
        message = message.split()
        decryptedMessage = []

        for letter in message:
            letter = int(letter, base=10)
            index = pow(letter, connectionInstance.d, connectionInstance.N)
            decryptedLetter = chr(index)
            decryptedMessage.append(decryptedLetter)

        message = str("".join(decryptedMessage))
        return message

    def update(self):
        try:
            while connectionInstance.connected:
                message = connectionInstance.socket.recv(1024).decode()
                message = self.decrypt(message)

                if message:
                    print(message)

                    if message[0:4] == "/add":
                        message = message[5:].split()
                        message.sort()

                        uiInstance.userList.clear()
                        uiInstance.userList.append("Users Online:")

                        for user in message:
                            if user not in self.users:
                                uiInstance.userList.append(user)
                                self.users.append(user)

                                message = user + " has connected"
                                animateThread = Thread(target=animationInstance.animateHeader, args=[message,
                                                       uiInstance.animationColor])
                                animateThread.start()
                            else:
                                uiInstance.userList.append(user)

                    elif message[0:14] == "/recentmessage":
                        uiInstance.chatHistory.append(message[15:])
                        self.chatHistory.append("[Old]: " + message[15:])
                        uiInstance.linesSent += 1

                    elif message[0:7] == "/remove":
                        if message[8:] == connectionInstance.username:
                            connectionInstance.leave()
                            break
                        user = message[8:]
                        uiInstance.userList.remove(user)
                        self.users.remove(user)
                        message = user + " has disconnected"
                        animateThread = Thread(target=animationInstance.animateHeader,
                                               args=[message, uiInstance.animationColor])
                        animateThread.start()

                    elif message[0:8] == "/display":
                        message = message[9:]
                        animateThread = Thread(target=animationInstance.animateHeader,
                                               args=[message, uiInstance.animationColor])
                        animateThread.start()

                    elif message == "/theme":
                        animateThread = Thread(target=animationInstance.switchTheme, args=[True])
                        animateThread.start()

                    elif message[0:4] == "/mod":
                        if message[5:] == connectionInstance.username and not connectionInstance.mod:
                            uiInstance.animationColor = (240, 230, 140)
                            connectionInstance.mod = True
                            animationInstance.runFiller = True
                            if not uiInstance.darkMode:
                                animateThread = Thread(target=animationInstance.switchTheme, args=[False])
                                animateThread.start()
                            animateThread = Thread(target=animationInstance.changeBorder)
                            animateThread.start()
                            animateThread = Thread(target=animationInstance.fadeColor, args=[uiInstance.animationColor,
                                                                                             False])
                            animateThread.start()
                            fillerThread = Thread(target=animationInstance.filler, args=[False])
                            fillerThread.start()

                    elif message[0:6] == "/color":
                        color = colorutils.web_to_rgb(message[7:])
                        animateThread = Thread(target=animationInstance.fadeColor, args=[color, True])
                        animateThread.start()

                    elif message[0:9] == "/savechat":
                        self.location = message[10:]
                        saveChatThread = Thread(target=communicationInstance.saveChatHistory)
                        saveChatThread.start()

                    elif message == "/disconnect":
                        print("Your username is used by someone else")
                        connectionInstance.leave()
                        break

                    elif message == "/filler":
                        if not animationInstance.runFiller:
                            animationInstance.runFiller = True
                            fillerThread = Thread(target=animationInstance.filler, args=[True])
                            fillerThread.start()

                        else:
                            animationInstance.runFiller = False

                    elif message[0:5] == "/rate":
                        animationInstance.readRate = float(message[6:])

                        animateThread = Thread(target=animationInstance.animateHeader, args=[
                                               "You changed the animation hold to " + str(animationInstance.readRate),
                                               uiInstance.animationColor])
                        animateThread.start()

                    elif message[0:13] == "/savesettings":
                        location = message[14:]
                        savePresetThread = Thread(target=self.savePresets, args=[location])
                        savePresetThread.start()

                    elif message[0:13] == "/loadsettings":
                        location = message[14:]
                        loadPresetThread = Thread(target=self.loadPresets, args=[location])
                        loadPresetThread.start()

                    else:
                        uiInstance.linesSent += 1
                        if uiInstance.linesSent > 15:
                            animateThread = Thread(target=animationInstance.animateHeader, args=["You created a new page",
                                                                                                 uiInstance.animationColor])
                            animateThread.start()
                            uiInstance.chatHistory.clear()
                            uiInstance.linesSent = 2

                        uiInstance.chatHistory.append(message)
                        time = strftime("%H:%M:%S", localtime())
                        message = time + " " + message
                        self.chatHistory.append(message)

        except ConnectionResetError:
            connectionInstance.connected = False
            connectionInstance.leave()
            print("Closed thread successfully")

        finally:
            return

    def sendToServer(self):
        try:
            self.message = uiInstance.messageInput.value
            if self.message:
                if self.message == "/leave":
                    connectionInstance.leave()
                else:
                    if len(self.message) + len(connectionInstance.username) + 2 >= 80:
                        animateThread = Thread(target=animationInstance.animateHeader,
                                               args=["Your message is too long.", uiInstance.animationColor])
                        animateThread.start()

                    else:
                        connectionInstance.socket.send(self.message.encode())
                        uiInstance.messageInput.clear()

        except BrokenPipeError:
            connectionInstance.connected = False
            connectionInstance.leave()

    def saveChatHistory(self):
        if self.location and " " not in self.location:
            file = open(self.location, "w")
            for chatLine in communicationInstance.chatHistory:
                file.write(chatLine + "\n")
            file.close()

            animateThread = Thread(target=animationInstance.animateHeader,
                                   args=["Your file has been saved in " + self.location, uiInstance.animationColor])
            animateThread.start()

        else:
            animateThread = Thread(target=animationInstance.animateHeader,
                                   args=["You can't save to this location", uiInstance.animationColor])
            animateThread.start()

        return

    def savePresets(self, location):
        if location and " " not in location:
            file = open(location, "w")
            if uiInstance.darkMode:
                file.write("/darkmode\n")

            if animationInstance.runFiller:
                file.write("/filler\n")

            file.write("/color " + colorutils.rgb_to_web(uiInstance.color))
            file.close()

            animateThread = Thread(target=animationInstance.animateHeader, args=[
                "Your presets have been saved in " + location, uiInstance.animationColor])
            animateThread.start()

        else:
            animateThread = Thread(target=animationInstance.animateHeader, args=[
                "You can't save your presets here", uiInstance.animationColor])
            animateThread.start()

        return

    def loadPresets(self, location):
        try:
            if location and " " not in location:
                file = open(location, "r")

                animateThread = Thread(target=animationInstance.animateHeader, args=[
                    "Your preset is loading", uiInstance.animationColor])
                animateThread.start()

                for command in file:
                    sleep(1)
                    if command[0:9] == "/darkmode":
                        if not uiInstance.darkMode:
                            animateThread = Thread(target=animationInstance.switchTheme, args=[False])
                            animateThread.start()

                    elif command[0:7] == "/filler":
                        if not animationInstance.runFiller:
                            animationInstance.runFiller = True
                            animateThread = Thread(target=animationInstance.filler, args=[False])
                            animateThread.start()

                    elif command[0:6] == "/color":
                        color = colorutils.web_to_rgb(command[7:])
                        animateThread = Thread(target=animationInstance.fadeColor, args=[color,
                                                                                         False])
                        animateThread.start()

                file.close()

            else:
                animateThread = Thread(target=animationInstance.animateHeader, args=[
                    "You can't open your preset here", uiInstance.animationColor])
                animateThread.start()

        except FileNotFoundError:
            animateThread = Thread(target=animationInstance.animateHeader,
                                   args=["You have no file or directory named " + location, uiInstance.animationColor])
            animateThread.start()

        finally:
            return


class Connection:
    def __init__(self, username, color, host, port, privateKey):
        self.username = username
        self.color = color
        self.host = host
        self.port = port
        self.privateKey = privateKey
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

            if not self.username == "" and not self.username == "Username" and not " " in self.username:
                # Checks: if username is not empty, not Username and does not contain spaces
                if not self.color.casefold() == "khaki":
                    try:
                        self.socket.connect((self.host, self.port))
                        self.socket.send(self.username.encode())
                        self.connected = True

                        uiInstance.status.value = "Connection Success"
                        UI.openChat(uiInstance)

                        uiInstance.color = colorutils.web_to_rgb(connectionInstance.color)

                    except ConnectionRefusedError:
                        uiInstance.status.value = "Connection Refused"

                    except OSError:
                        uiInstance.status.value = "Restart Client"

                    except BrokenPipeError:
                        uiInstance.status.value = "Broken Pipe"
                else:
                    uiInstance.status.value = "Invalid Color"
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

        uiInstance.setupWindow.hide()
        uiInstance.chatWindow.hide()

        self.socket.close()
        print("You have disconnected")
        sys.exit("Terminated process")


class UI:
    def __init__(self):
        self.font = "San Francisco"
        self.fontSize = 22
        self.color = None
        self.animationColor = (173, 216, 230)
        self.bg = (70, 70, 70)
        self.darkbg = (40, 40, 40)
        self.waitTime = 1
        self.linesSent = 1
        self.darkMode = False

        if platform.system() == "Darwin":
            self.rate = 0.00025
        elif platform.system() == "Windows":
            self.rate = 0.00000

    def openChat(self):
        try:
            self.chatWindow = Window(self.setupWindow, width=1280, height=720, title="Chatroom", bg=self.bg)
            self.chatWindow.when_closed = connectionInstance.leave

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

            self.userList = ListBox(userListBox, items=["Users Online:"], width=150, height="fill", align="right")
            self.userList.text_color = connectionInstance.color
            self.userList.bg = (255, 255, 255)
            self.userList.text_size = self.fontSize

            self.header = Text(header, text=("Welcome " + connectionInstance.username), width="fill", height=50)
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

            self.chatHistory = TextBox(userBox, text="Hi!", width="fill", height="fill", align="top", multiline=True)
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
            self.messageInput.when_key_pressed = enterSend

            # Threads start here

            listeningThread = Thread(target=communicationInstance.update)
            listeningThread.start()

            self.setupWindow.hide()
            self.chatWindow.show()

        except:
            print("Your client crashed unexpectedly")
            connectionInstance.leave()

    def openSetup(self):
        self.setupWindow = App(title="Connect", width=800, height=275)
        self.setupWindow.bg = self.bg
        self.setupWindow.font = self.font

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

        usernameInput = TextBox(usernameInputBox, text=connectionInstance.username, width="fill")
        colorInput = TextBox(colorInputBox, text=connectionInstance.color, width="fill")
        hostInput = TextBox(hostInputBox, text=connectionInstance.host, width="fill")
        portInput = TextBox(portInputBox, text=connectionInstance.port, width="fill")
        keyInput = TextBox(keyInputBox, text=connectionInstance.privateKey, width="fill")

        usernameInput.text_color = self.animationColor
        colorInput.text_color = self.animationColor
        hostInput.text_color = self.animationColor
        portInput.text_color = self.animationColor
        keyInput.text_color = self.animationColor

        usernameInput.text_size = self.fontSize - 6
        colorInput.text_size = self.fontSize - 6
        hostInput.text_size = self.fontSize - 6
        portInput.text_size = self.fontSize - 6
        keyInput.text_size = self.fontSize - 6

        usernameInput.bg = self.darkbg
        colorInput.bg = self.darkbg
        hostInput.bg = self.darkbg
        portInput.bg = self.darkbg
        keyInput.bg = self.darkbg

        self.status = Text(verifyBox, text="Not Connected")
        self.status.text_size = self.fontSize + 12

        rightBlocker = Box(verifyBox, width="fill", height=40, align="top")
        attemptConnect = PushButton(verifyBox, text="Connect", command=connectionInstance.connect, args=
        [usernameInput, colorInput, hostInput, portInput, keyInput])

        attemptConnect.text_size = self.fontSize - 6

        build = Text(bottomPadding, text="development: new UI", align="bottom")

        animateThread = Thread(target=animationInstance.animateStatus)
        animateThread.start()

        self.setupWindow.display()


def enterSend(event):
    if event.tk_event.keysym == "Return":
        communicationInstance.sendToServer()


# connectionInstance = Connection("Username", "Chat Color", "Host IP", "Port", "Private Key")
connectionInstance = Connection("tomm", "lightblue", "192.168.1.138", "54817", "506189634349")
uiInstance = UI()
communicationInstance = Communication()
animationInstance = Animation()

UI.openSetup(uiInstance)

