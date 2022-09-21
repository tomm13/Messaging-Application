# 21/9/2022
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

    def filler(self):
        try:
            while animationInstance.runFiller:
                while animationInstance.animationRunning:
                    sleep(uiInstance.waitTime)
                animationInstance.runFiller = True

                sleep(60)

                time = strftime("%H:%M", localtime())
                animateThread = Thread(target=self.animateHeader, args=[str(time), uiInstance.animationColor])
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

            while not (R, G, B) == (240, 230, 140):
                if R < 240:
                    R += 1
                if G < 230:
                    G += 1
                if B > 140:
                    B -= 1

                uiInstance.border.set_border(3, (R, G, B))

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
            oldTextColor = colorutils.Color(web=connectionInstance.color)
            newTextColor = colorutils.Color(web=newColor)

            if newColor.casefold() == "khaki" and not connectionInstance.mod:
                animateThread = Thread(target=self.animateHeader,
                                       args=["You don't have the power to use this color", uiInstance.animationColor])
                animateThread.start()
                return

            if oldTextColor == newTextColor:
                animateThread = Thread(target=self.animateHeader,
                                       args=["You can't change to the same color", uiInstance.animationColor])
                animateThread.start()
                return

            while animationInstance.animationRunning:
                sleep(uiInstance.waitTime)
            animationInstance.animationRunning = True

            (R, G, B) = oldTextColor.rgb

            while not R == newTextColor.red or not G == newTextColor.green or not B == newTextColor.blue:
                if R > newTextColor.red:
                    R -= 1
                if G > newTextColor.green:
                    G -= 1
                if B > newTextColor.blue:
                    B -= 1
                if R < newTextColor.red:
                    R += 1
                if G < newTextColor.green:
                    G += 1
                if B < newTextColor.blue:
                    B += 1

                uiInstance.chatHistory.text_color = (R, G, B)
                uiInstance.messageInput.text_color = (R, G, B)

                sleep(uiInstance.rate)

            if displayMessage:
                animateThread = Thread(target=self.animateHeader,
                                       args=["You changed the text color", uiInstance.animationColor])
                animateThread.start()

            # Once completed
            connectionInstance.color = newColor

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
            while animationInstance.animationRunning:
                sleep(uiInstance.waitTime)
            animationInstance.animationRunning = True

            if not uiInstance.darkMode:
                (R, G, B) = (0, 0, 0)

                while not R == 255 or not G == 255 or not B == 255:
                    # Text fades from any colour to white
                    if R < 255:
                        R += 1
                    if G < 255:
                        G += 1
                    if B < 255:
                        B += 1

                    uiInstance.header.text_color = (R, G, B)
                    sleep(uiInstance.rate)

                uiInstance.header.value = message

                while not R == color[0] or not G == color[1] or not B == color[2]:
                    # Fades background from white to color
                    if R > color[0]:
                        R -= 1
                    if G > color[1]:
                        G -= 1
                    if B > color[2]:
                        B -= 1

                    uiInstance.header.bg = (R, G, B)
                    sleep(uiInstance.rate)

                sleep(self.readRate)

                while not R == 255 or not G == 255 or not B == 255:
                    # Fades background from color to white
                    if R < 255:
                        R += 1
                    if B < 255:
                        B += 1
                    if G < 255:
                        G += 1

                    uiInstance.header.bg = (R, G, B)
                    sleep(uiInstance.rate)

                uiInstance.header.value = "Welcome " + connectionInstance.username

                while not R == 0 or not G == 0 or not B == 0:
                    # Text fades from white to black
                    if R > 0:
                        R -= 1
                    if G > 0:
                        G -= 1
                    if B > 0:
                        B -= 1

                    uiInstance.header.text_color = (R, G, B)
                    sleep(uiInstance.rate)

            else:
                (R, G, B) = (255, 255, 255)

                while not R == 70 or not G == 70 or not B == 70:
                    # Text fades from any colour to black
                    if R > 70:
                        R -= 1
                    if G > 70:
                        G -= 1
                    if B > 70:
                        B -= 1
                    if R < 70:
                        R += 1
                    if G < 70:
                        G += 1
                    if B < 70:
                        B += 1

                    uiInstance.header.text_color = (R, G, B)
                    sleep(uiInstance.rate)

                uiInstance.header.value = message

                while not R == color[0] or not G == color[1] or not B == color[2]:
                    # Fades background from black to color
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

                sleep(self.readRate)

                while not R == 70 or not G == 70 or not B == 70:
                    # Fades background from color to black
                    if R > 70:
                        R -= 1
                    if B > 70:
                        B -= 1
                    if G > 70:
                        G -= 1
                    if R < 70:
                        R += 1
                    if B < 70:
                        B += 1
                    if G < 70:
                        G += 1

                    uiInstance.header.bg = (R, G, B)
                    sleep(uiInstance.rate)

                uiInstance.header.value = "Welcome " + connectionInstance.username

                while not R == 255 or not G == 255 or not B == 255:
                    # Text fades from black to white
                    if R < 255:
                        R += 1
                    if G < 255:
                        G += 1
                    if B < 255:
                        B += 1

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

    def switchTheme(self, DisplayMessage):
        try:
            while animationInstance.animationRunning:
                sleep(uiInstance.waitTime)
            animationInstance.animationRunning = True

            if uiInstance.darkMode:
                while uiInstance.darkMode:
                    # To turn Dark Mode off
                    (R, G, B) = (255, 255, 255)

                    while not (R, G, B) == (0, 0, 0):
                        # Text Fades to Black
                        R -= 1
                        G -= 1
                        B -= 1

                        uiInstance.userList.text_color = (R, G, B)
                        uiInstance.header.text_color = (R, G, B)
                        sleep(uiInstance.rate)

                    while not (R, G, B) == (215, 215, 215):
                        # All backgrounds fade from black to white
                        R += 1
                        G += 1
                        B += 1

                        uiInstance.header.bg = (R, G, B)
                        uiInstance.chatHistory.bg = (R, G, B)
                        uiInstance.messageInput.bg = (R, G, B)
                        uiInstance.userList.bg = (R, G, B)
                        sleep(uiInstance.rate)

                    while not (R, G, B) == (255, 255, 255):
                        R += 1
                        G += 1
                        B += 1

                        uiInstance.header.bg = (R, G, B)
                        uiInstance.chatHistory.bg = (R, G, B)
                        uiInstance.messageInput.bg = (R, G, B)
                        sleep(uiInstance.rate)

                    uiInstance.darkMode = False

            else:
                while not uiInstance.darkMode:
                    # To turn Dark Mode on
                    R = 0
                    G = 0
                    B = 0

                    while not (R, G, B) == (255, 255, 255):
                        # Text Fades to White
                        R += 1
                        G += 1
                        B += 1

                        uiInstance.userList.text_color = (R, G, B)
                        uiInstance.header.text_color = (R, G, B)

                    while not (R, G, B) == (70, 70, 70):
                        # All Background fade to grey
                        R -= 1
                        G -= 1
                        B -= 1

                        uiInstance.messageInput.bg = (R, G, B)
                        uiInstance.chatHistory.bg = (R, G, B)
                        uiInstance.header.bg = (R, G, B)
                        uiInstance.userList.bg = (R, G, B)
                        sleep(uiInstance.rate)

                    while not (R, G, B) == (40, 40, 40):
                        R -= 1
                        G -= 1
                        B -= 1

                        uiInstance.userList.bg = (R, G, B)
                        sleep(uiInstance.rate)

                    uiInstance.darkMode = True

            uiInstance.chatHistory.text_color = connectionInstance.color
            uiInstance.messageInput.text_color = connectionInstance.color

            if DisplayMessage:
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
                            animateThread = Thread(target=animationInstance.animateHeader, args=[message, (124, 252, 0)])
                            animateThread.start()
                        else:
                            uiInstance.userList.append(user)

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
                        animateThread = Thread(target=animationInstance.fadeColor, args=["khaki", False])
                        animateThread.start()
                        fillerThread = Thread(target=animationInstance.filler)
                        fillerThread.start()

                elif message[0:6] == "/color":
                    connectionInstance.newColor = message[7:]
                    animateThread = Thread(target=animationInstance.fadeColor, args=[connectionInstance.newColor, True])
                    animateThread.start()

                elif message[0:5] == "/save":
                    self.location = message[6:]
                    saveChatThread = Thread(target=communicationInstance.saveChatHistory)
                    saveChatThread.start()

                elif message == "/disconnect":
                    print("Your username is used by someone else")
                    connectionInstance.leave()
                    break

                elif message == "/filler":
                    if not animationInstance.runFiller:
                        animationInstance.runFiller = True
                        animateThread = Thread(target=animationInstance.animateHeader, args=["You turned filler on",
                                                                                             uiInstance.animationColor])
                        animateThread.start()
                        fillerThread = Thread(target=animationInstance.filler)
                        fillerThread.start()

                    else:
                        animationInstance.runFiller = False
                        animateThread = Thread(target=animationInstance.animateHeader, args=["You turned filler off",
                                                                                             uiInstance.animationColor])
                        animateThread.start()

                elif message[0:5] == "/rate":
                    animationInstance.readRate = int(message[6:])

                    animateThread = Thread(target=animationInstance.animateHeader, args=["You changed the animation hold to " + str(animationInstance.readRate),
                                                                                         uiInstance.animationColor])
                    animateThread.start()

                else:
                    uiInstance.linesSent += 1
                    if uiInstance.linesSent > 15:
                        animateThread = Thread(target=animationInstance.animateHeader, args=["You created a new page",
                                                                                             uiInstance.animationColor])
                        animateThread.start()
                        uiInstance.chatHistory.clear()
                        uiInstance.linesSent = 2

                    self.chatHistory.append(message)
                    uiInstance.chatHistory.append(message)

        except Exception as e:
            if connectionInstance.connected:
                print(e)
            else:
                print("Closed thread successfully")

        finally:
            return

    def sendToServer(self):
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

    def saveChatHistory(self):
        if self.location and " " not in self.location:
            file = open(self.location, "w")
            for chatLine in communicationInstance.chatHistory:
                file.write(chatLine)
                file.write("\n")
            file.close()

            animateThread = Thread(target=animationInstance.animateHeader,
                                   args=["Your file has been saved", uiInstance.animationColor])
            animateThread.start()

        else:
            animateThread = Thread(target=animationInstance.animateHeader,
                                   args=["You can't save to this location", uiInstance.animationColor])
            animateThread.start()

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
            self.privateKey = privateKeyInput.value.split(", ")
            self.d = int(self.privateKey[0], base=10)
            self.N = int(self.privateKey[1], base=10)

            if not self.username == "" and not self.username == "Username" and not " " in self.username:
                # Checks: if username is not empty, not Username and does not contain spaces
                if not self.color.casefold() == "khaki":
                    try:
                        self.socket.connect((self.host, self.port))
                        self.socket.send(self.username.encode())
                        self.connected = True

                        uiInstance.status.value = "Connection Success"
                        UI.openChat(uiInstance)

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
        self.color = (173, 216, 230)
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
            self.chatWindow = Window(self.setupWindow, width=1200, height=590, title="Chatroom", bg=(70, 70, 70))
            self.chatWindow.when_closed = connectionInstance.leave

            topPadding = Box(self.chatWindow, width="fill", height=50, align="top")
            leftPadding = Box(self.chatWindow, width=50, height="fill", align="left")
            rightPadding = Box(self.chatWindow, width=50, height="fill", align="right")
            bottomPadding = Box(self.chatWindow, width="fill", height=50, align="bottom")

            self.border = Box(self.chatWindow, width="fill", height="fill")
            self.border.set_border(3, (173, 216, 230))

            header = Box(self.border, width="fill", height=40, align="top")
            buttonBlocker = Box(self.border, width="fill", height=3, align="bottom")
            buttonBox = Box(self.border, width="fill", height=40, align="bottom")
            userBlocker = Box(self.border, width="fill", height=3, align="top")
            userBox = Box(self.border, width="fill", height="fill")

            self.userList = ListBox(userBox, items=["Users Online:"], width=150, height="fill", align="left")
            self.userList.text_color = (0, 0, 0)
            self.userList.bg = (215, 215, 215)
            self.userList.text_size = self.fontSize - 2

            self.header = Text(header, text=("Welcome " + connectionInstance.username))
            self.header.text_size = self.fontSize + 8
            self.header.text_color = (0, 0, 0)
            self.header.bg = (255, 255, 255)
            self.header.width = "fill"

            self.chatHistory = TextBox(userBox, "Hi!", "fill", height="fill", multiline=True, align="left")
            self.chatHistory.text_color = connectionInstance.color
            self.chatHistory.bg = (255, 255, 255)
            self.chatHistory.text_size = self.fontSize
            self.chatHistory.disable()

            self.sendButton = PushButton(buttonBox, text="Send", command=communicationInstance.sendToServer)
            self.sendButton.text_color = (0, 0, 0)
            self.sendButton.bg = (255, 255, 255)
            self.sendButton.align = "right"

            self.messageInput = TextBox(buttonBox, width="fill", height="fill", align="bottom")
            self.messageInput.text_color = connectionInstance.color
            self.messageInput.bg = (255, 255, 255)
            self.messageInput.text_size = self.fontSize + 2

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
        self.setupWindow.bg = (70, 70, 70)
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

        build = Text(bottomPadding, text="development: modding and votes", align="bottom")

        animateThread = Thread(target=animationInstance.animateStatus)
        animateThread.start()

        self.setupWindow.display()


# connectionInstance = Connection("Username", "Chat Color", "Host IP", "Port", "Private Key")

connectionInstance = Connection("tomm", "lightblue", "192.168.1.138", "65109", "13457, 22733")
uiInstance = UI()
communicationInstance = Communication()
animationInstance = Animation()

UI.openSetup(uiInstance)
