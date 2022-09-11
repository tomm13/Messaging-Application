# 11/9/2022
# V13 Beta Class

import platform
import socket
from time import sleep, localtime, strftime
from threading import Thread

import colorutils
from guizero import *

ChatHistory = []

def animateStatus():
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
            sleep(0.005)

        while not R == 255 or not G == 255 or not B == 255:
            if R < 255:
                R += 1
            if G < 255:
                G += 1
            if B < 255:
                B += 1

            uiInstance.status.text_color = (R, G, B)
            sleep(0.005)

    return

def Filler():
    while uiInstance.runFiller:
        sleep(60)
        while uiInstance.animationRunning:
            sleep(uiInstance.waitTime)
        uiInstance.animationRunning = True

        Time = strftime("%H:%M", localtime())
        AnimateThread = Thread(target=AnimateHeader, args=[str(Time), uiInstance.animationColor])
        AnimateThread.start()

    return

def ModBorder():
    (R, G, B) = (173, 216, 230)

    while uiInstance.animationRunning:
        sleep(uiInstance.waitTime)
    uiInstance.animationRunning = True

    while not (R, G, B) == (240, 230, 140):
        if R < 240:
            R += 1
        if G < 230:
            G += 1
        if B > 140:
            B -= 1

        uiInstance.border.set_border(3, (R, G, B))

    uiInstance.animationRunning = False
    return

def FadeToColor(newColor, displayMessage):
    global Color
    try:
        oldTextColor = colorutils.Color(web=connectionInstance.color)
        newTextColor = colorutils.Color(web=newColor)

        if newColor.casefold() == "khaki" and not connectionInstance.mod:
            AnimateThread = Thread(target=AnimateHeader,
                                   args=["You don't have the power to use this color", uiInstance.animationColor])
            AnimateThread.start()
            return

        if oldTextColor == newTextColor:
            AnimateThread = Thread(target=AnimateHeader,
                                   args=["You can't change to the same color", uiInstance.animationColor])
            AnimateThread.start()
            return

        while uiInstance.animationRunning:
            sleep(uiInstance.waitTime)
        uiInstance.animationRunning = True

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
            animateThread = Thread(target=AnimateHeader, args=["You changed the text color", uiInstance.animationColor])
            animateThread.start()

        # Once completed
        connectionInstance.color = newColor

    except:
        animateThread = Thread(target=AnimateHeader, args=["You cannot use an undefined color", uiInstance.animationColor])
        animateThread.start()

    uiInstance.animationRunning = False
    return

def AnimateHeader(Message, Color):
    while uiInstance.animationRunning:
        sleep(uiInstance.waitTime)
    uiInstance.animationRunning = True

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

        uiInstance.header.value = Message

        while not R == Color[0] or not G == Color[1] or not B == Color[2]:
            # Fades background from white to color
            if R > Color[0]:
                R -= 1
            if G > Color[1]:
                G -= 1
            if B > Color[2]:
                B -= 1

            uiInstance.header.bg = (R, G, B)
            sleep(uiInstance.rate)

        sleep(1)

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

        uiInstance.header.value = Message

        while not R == Color[0] or not G == Color[1] or not B == Color[2]:
            # Fades background from black to color
            if R < Color[0]:
                R += 1
            if G < Color[1]:
                G += 1
            if B < Color[2]:
                B += 1
            if R > Color[0]:
                R -= 1
            if G > Color[1]:
                G -= 1
            if B > Color[2]:
                B -= 1

            uiInstance.header.bg = (R, G, B)
            sleep(uiInstance.rate)

        sleep(1)

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

    uiInstance.animationRunning = False
    return

def SwitchTheme(DisplayMessage):
    while uiInstance.animationRunning:
        sleep(uiInstance.waitTime)
    uiInstance.animationRunning = True

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

    uiInstance.animationRunning = False
    uiInstance.chatHistory.text_color = connectionInstance.color
    uiInstance.messageInput.text_color = connectionInstance.color

    if DisplayMessage:
        if uiInstance.darkMode:
            animateThread = Thread(target=AnimateHeader,
                                   args=["You turned dark mode on", uiInstance.animationColor])
            animateThread.start()
        else:
            animateThread = Thread(target=AnimateHeader,
                                   args=["You turned light mode on", uiInstance.animationColor])
            animateThread.start()

    return

def SaveChatHistory(Location):
    if Location and not " " in Location:
        File = open(Location, "w")
        for Chat in ChatHistory:
            File.write(Chat)
            File.write("\n")
        File.close()

        animateThread = Thread(target=AnimateHeader, args=["Your file has been saved", uiInstance.animationColor])
        animateThread.start()

    else:
        animateThread = Thread(target=AnimateHeader,
                               args=["You can't save to this location", uiInstance.animationColor])
        animateThread.start()

    return

def RSADecrypt(Message):
    Message = Message.split()
    RSADecryptedMessage = []

    for Letter in Message:
        Letter = int(Letter, base=10)
        Index = pow(Letter, connectionInstance.d, connectionInstance.N)
        RSADecryptedLetter = chr(Index)
        RSADecryptedMessage.append(RSADecryptedLetter)

    Message = str("".join(RSADecryptedMessage))
    return Message

def AlwaysUpdate():
    global LinesSent, RunFiller
    Users = []
    while True:
        Message = connectionInstance.socket.recv(1024).decode()
        Message = RSADecrypt(Message)

        if Message:
            print(Message)

        if Message[0:4] == "/add":
            Message = Message[5:]
            Message = Message.split()
            Message.sort()

            uiInstance.userList.clear()
            uiInstance.userList.append("Users Online:")

            for User in Message:
                if User not in Users:
                    uiInstance.userList.append(User)
                    Users.append(User)
                    Message = User + " has connected"
                    animateThread = Thread(target=AnimateHeader, args=[Message, (124, 252, 0)])
                    animateThread.start()
                else:
                    uiInstance.userList.append(User)

        elif Message[0:7] == "/remove":
            if Message[8:] == connectionInstance.username:
                connectionInstance.leave()
                break
            User = Message[8:]
            uiInstance.userList.remove(User)
            Users.remove(User)
            Message = User + " has disconnected"
            animateThread = Thread(target=AnimateHeader, args=[Message, uiInstance.animationColor])
            animateThread.start()

        elif Message[0:8] == "/display":
            Message = Message[9:]
            animateThread = Thread(target=AnimateHeader, args=[Message, uiInstance.animationColor])
            animateThread.start()

        elif Message == "/theme":
            animateThread = Thread(target=SwitchTheme, args=[True])
            animateThread.start()

        elif Message[0:4] == "/mod":
            if Message[5:] == connectionInstance.username and not connectionInstance.mod:
                uiInstance.animationColor = (240, 230, 140)
                global RunFiller
                connectionInstance.mod = True
                RunFiller = True
                if not uiInstance.darkMode:
                    animateThread = Thread(target=SwitchTheme, args=[False])
                    animateThread.start()
                animateThread = Thread(target=ModBorder)
                animateThread.start()
                animateThread = Thread(target=FadeToColor, args=["khaki", False])
                animateThread.start()
                fillerThread = Thread(target=Filler)
                fillerThread.start()

        elif Message[0:6] == "/color":
            connectionInstance.newColor = Message[7:]
            animateThread = Thread(target=FadeToColor, args=[connectionInstance.newColor, True])
            animateThread.start()

        elif Message[0:5] == "/save":
            Location = Message[6:]
            saveChatThread = Thread(target=SaveChatHistory, args=[Location])
            saveChatThread.start()

        elif Message == "/disconnect":
            animateThread = Thread(target=AnimateHeader, args=["You cannot use this username", uiInstance.animationColor])
            animateThread.start()
            while True:
                animateThread = Thread(target=AnimateHeader, args=["You are not connected", (216, 36, 41)])
                animateThread.start()
                sleep(uiInstance.rate)

        elif Message == "/filler":
            if uiInstance.runFiller == False:
                uiInstance.runFiller = True
                animateThread = Thread(target=AnimateHeader, args=["You turned filler on", uiInstance.animationColor])
                animateThread.start()
                fillerThread = Thread(target=Filler)
                fillerThread.start()

            else:
                animateThread = Thread(target=AnimateHeader, args=["You turned filler off", uiInstance.animationColor])
                animateThread.start()
                RunFiller = False

        else:
            uiInstance.linesSent += 1
            if uiInstance.linesSent > 15:
                animateThread = Thread(target=AnimateHeader, args=["You created a new page", uiInstance.animationColor])
                animateThread.start()
                uiInstance.chatHistory.clear()
                uiInstance.linesSent = 2

            ChatHistory.append(Message)
            uiInstance.chatHistory.append(Message)


def SendToServer():
    Message = uiInstance.messageInput.value
    if Message:
        if Message == "/leave":
            connectionInstance.leave()
        else:
            if len(Message) + len(connectionInstance.username) + 2 >= 80:
                animateThread = Thread(target=AnimateHeader,
                                       args=["Your message is too long.", uiInstance.animationColor])
                animateThread.start()

            else:
                connectionInstance.socket.send(Message.encode())
                uiInstance.messageInput.clear()

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
                        uiInstance.status.value = "Connection Full"

                    except OSError:
                        uiInstance.status.value = "Restart Client"

                    except BrokenPipeError:
                        uiInstance.status.value = "Broken Pipe"

                else:
                    uiInstance.status.value = "Color Locked"
            else:
                uiInstance.status.value = "Invalid Username"
        except IndexError:
            uiInstance.status.value = "Invalid Input"

        except ValueError:
            uiInstance.status.value = "Invalid Input"

    def leave(self):
        self.socket.send("/leave".encode())

        uiInstance.setupWindow.hide()
        uiInstance.chatWindow.hide()

        self.socket.close()
        print("You have disconnected.")
        quit()

class UI:
    def __init__(self, font, fontSize):
        self.font = font
        self.fontSize = fontSize
        self.color = connectionInstance.color
        self.animationColor = (173, 216, 230)
        self.bg = (70, 70, 70)
        self.darkbg = (40, 40, 40)
        self.waitTime = 0.75
        self.linesSent = 1
        self.animationRunning = False
        self.darkMode = False
        self.runFiller = False

        if platform.system() == "Darwin":
            self.rate = 0.00025
        elif platform.system() == "Windows":
            self.rate = 0.00000

    def openChat(self):
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
        self.header.text_size = 30
        self.header.text_color = (0, 0, 0)
        self.header.bg = (255, 255, 255)
        self.header.width = "fill"

        self.chatHistory = TextBox(userBox, "Hi!", "fill", height="fill", multiline=True, align="left")
        self.chatHistory.text_color = connectionInstance.color
        self.chatHistory.bg = (255, 255, 255)
        self.chatHistory.text_size = self.fontSize
        self.chatHistory.disable()

        self.sendButton = PushButton(buttonBox, text="Send", command=SendToServer)
        self.sendButton.text_color = (0, 0, 0)
        self.sendButton.bg = (255, 255, 255)
        self.sendButton.align = "right"

        self.messageInput = TextBox(buttonBox, width="fill", height="fill", align="bottom")
        self.messageInput.text_color = connectionInstance.color
        self.messageInput.bg = (255, 255, 255)
        self.messageInput.text_size = self.fontSize + 2

        # Threads start here

        listeningThread = Thread(target=AlwaysUpdate)
        listeningThread.start()

        self.setupWindow.hide()
        self.chatWindow.show()

    def openSetup(self):
        self.setupWindow = App(title="Connect", width=800, height=275)
        self.setupWindow.bg = (70, 70, 70)
        self.setupWindow.font = "San Francisco Bold"

        topPadding = Box(self.setupWindow, width="fill", height=50, align="top")
        bottomPadding = Box(self.setupWindow, width="fill", height=50, align="bottom")
        contents = Box(self.setupWindow, width="fill", height="fill", align="top")

        InputBox = Box(contents, width=400, height=150, align="left")
        rightPadding = Box(contents, width=16, height="fill", align="right")
        VerifyBox = Box(contents, width=384, height=150, align="right")

        usernameBlocker = Box(InputBox, width=15, height=150, align="right")
        usernameInputBox = Box(InputBox, width=275, height=30)
        colorBlocker = Box(InputBox, width=15, height=120, align="right")
        colorInputBox = Box(InputBox, width=260, height=30)
        hostBlocker = Box(InputBox, width=15, height=90, align="right")
        hostInputBox = Box(InputBox, width=245, height=30)
        portBlocker = Box(InputBox, width=15, height=60, align="right")
        portInputBox = Box(InputBox, width=230, height=30)
        keyBlocker = Box(InputBox, width=15, height=30, align="right")
        keyInputBox = Box(InputBox, width=215, height=30)

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

        self.status = Text(VerifyBox, text="Not Connected")
        self.status.text_size = 34

        rightBlocker = Box(VerifyBox, width="fill", height=40, align="top")
        AttemptConnect = PushButton(VerifyBox, text="Connect", command=connectionInstance.connect, args=
                                    [usernameInput, colorInput, hostInput, portInput, keyInput])

        AttemptConnect.text_size = self.fontSize - 6

        build = Text(bottomPadding, text="development", align="bottom")

        animateThread = Thread(target=animateStatus)
        animateThread.start()

        self.setupWindow.display()

#connectionInstance = Connection("Username", "Chat Color", "Host IP", "Port", "Private Key")
connectionInstance = Connection("tommy", "lightblue", "172.20.10.2", "49129", "101, 551")
uiInstance = UI("San Francisco Bold", 22)

UI.openSetup(uiInstance)
