##7/9/2022
##V13 Beta
import platform
import socket
from time import sleep, localtime, strftime
from threading import Thread

import colorutils
from guizero import *

ChatHistory = []

DarkMode = False
StopRainbow = False

Mod = False
RunFiller = False

WaitTime = 0.75
LinesSent = 1

Location = " - "
privateKey = ""

if platform.system() == "Darwin":
    Rate = 0.00025
elif platform.system() == "Windows":
    Rate = 0.00000


class Boxes(Box):
    # This is for UI design. This allows creations of box instances.
    def __init__(self, master, width, height, align):
        super().__init__(master, width=width, height=height, align=align)
        self.width = width
        self.height = height
        self.align = align


class Buttons(PushButton):
    # This is for UI design. Allows easier creation of button instances.
    def __init__(self, master, text, command):
        super().__init__(master, text=text, command=command)
        self.text = text
        self.command = command


class Blockers(Box):
    # This is for UI design. Generally used for Invisible Padding Boxes. Have no align.
    def __init__(self, master, width, height):
        super().__init__(master, width=width, height=height)
        self.width = width
        self.height = height


class TextBoxes(TextBox):
    # Allows for creation of TextBoxes
    def __init__(self, master, text):
        super().__init__(master, text=text, width="fill")
        self.text = text
        self.text_size = 16
        self.text_color = "lightblue"
        self.bg = (40, 40, 40)


class Texts(Text):
    # Allows for creation of Text Objects
    def __init__(self, master, text, text_size, text_color):
        super().__init__(master, text=text)
        self.text = text
        self.text_size = text_size
        self.text_color = text_color

def Filler():
    while RunFiller:
        sleep(60)
        while uiInstance.animationRunning:
            sleep(WaitTime)
        uiInstance.animationRunning = True

        Time = strftime("%H:%M", localtime())
        AnimateThread = Thread(target=AnimateHeader, args=[str(Time), uiInstance.animationColor])
        AnimateThread.start()

def ModBorder():
    (R, G, B) = (173, 216, 230)

    while uiInstance.animationRunning:
        sleep(WaitTime)
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

        if newColor.casefold() == "khaki" and Mod == False:
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
            sleep(WaitTime)
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

            sleep(Rate)

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
        sleep(WaitTime)
    uiInstance.animationRunning = True

    if not DarkMode:
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
            sleep(Rate)

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
            sleep(Rate)

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
            sleep(Rate)

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
            sleep(Rate)

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
            sleep(Rate)

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
            sleep(Rate)

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
            sleep(Rate)

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
            sleep(Rate)

    uiInstance.animationRunning = False
    return

def SwitchTheme(DisplayMessage):
    global DarkMode

    while uiInstance.animationRunning:
        sleep(WaitTime)
    uiInstance.animationRunning = True

    if DarkMode:
        while DarkMode:
            # To turn Dark Mode off
            (R, G, B) = (255, 255, 255)

            while not (R, G, B) == (0, 0, 0):
                # Text Fades to Black
                R -= 1
                G -= 1
                B -= 1

                uiInstance.userList.text_color = (R, G, B)
                uiInstance.header.text_color = (R, G, B)
                sleep(Rate)

            while not (R, G, B) == (215, 215, 215):
                # All backgrounds fade from black to white
                R += 1
                G += 1
                B += 1

                uiInstance.header.bg = (R, G, B)
                uiInstance.chatHistory.bg = (R, G, B)
                uiInstance.messageInput.bg = (R, G, B)
                uiInstance.userList.bg = (R, G, B)
                sleep(Rate)

            while not (R, G, B) == (255, 255, 255):
                R += 1
                G += 1
                B += 1

                uiInstance.header.bg = (R, G, B)
                uiInstance.chatHistory.bg = (R, G, B)
                uiInstance.messageInput.bg = (R, G, B)
                sleep(Rate)

            DarkMode = False

    else:
        while not DarkMode:
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
                sleep(Rate)

            while not (R, G, B) == (40, 40, 40):
                R -= 1
                G -= 1
                B -= 1

                uiInstance.userList.bg = (R, G, B)
                sleep(Rate)

            DarkMode = True

    uiInstance.animationRunning = False
    uiInstance.chatHistory.text_color = connectionInstance.color
    uiInstance.messageInput.text_color = connectionInstance.color

    if DisplayMessage:
        if DarkMode:
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
    global LinesSent, Mod, RunFiller
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

            UserList.clear()
            UserList.append("Users Online:")

            for User in Message:
                if User not in Users:
                    UserList.append(User)
                    Users.append(User)
                    Message = User + " has connected"
                    AnimateThread = Thread(target=AnimateHeader, args=[Message, (124, 252, 0)])
                    AnimateThread.start()
                else:
                    UserList.append(User)

        elif Message[0:7] == "/remove":
            if Message[8:] == connectionInstance.username:
                connectionInstance.leave()
                break
            User = Message[8:]
            UserList.remove(User)
            Users.remove(User)
            Message = User + " has disconnected"
            AnimateThread = Thread(target=AnimateHeader, args=[Message, uiInstance.animationColor])
            AnimateThread.start()

        elif Message[0:8] == "/display":
            Message = Message[9:]
            AnimateThread = Thread(target=AnimateHeader, args=[Message, uiInstance.animationColor])
            AnimateThread.start()

        elif Message == "/theme":
            AnimateThread = Thread(target=SwitchTheme, args=[True])
            AnimateThread.start()

        elif Message[0:4] == "/mod":
            if Message[5:] == connectionInstance.username and Mod == False:
                uiInstance.animationColor = (240, 230, 140)
                global RunFiller
                Mod = True
                RunFiller = True
                if DarkMode == False:
                    AnimateThread = Thread(target=SwitchTheme, args=[False])
                    AnimateThread.start()
                AnimateThread = Thread(target=ModBorder)
                AnimateThread.start()
                AnimateThread = Thread(target=FadeToColor, args=["khaki", False])
                AnimateThread.start()
                FillerThread = Thread(target=Filler)
                FillerThread.start()

        elif Message[0:6] == "/color":
            connectionInstance.newColor = Message[7:]
            AnimateThread = Thread(target=FadeToColor, args=[connectionInstance.newColor, True])
            AnimateThread.start()

        elif Message[0:5] == "/save":
            Location = Message[6:]
            SaveChatThread = Thread(target=SaveChatHistory, args=[Location])
            SaveChatThread.start()

        elif Message == "/disconnect":
            AnimateThread = Thread(target=AnimateHeader, args=["You cannot use this username", uiInstance.animationColor])
            AnimateThread.start()
            while True:
                AnimateThread = Thread(target=AnimateHeader, args=["You are not connected", (216, 36, 41)])
                AnimateThread.start()
                sleep(Rate)

        elif Message == "/filler":
            if RunFiller == False:
                RunFiller = True
                AnimateThread = Thread(target=AnimateHeader, args=["You turned filler on", uiInstance.animationColor])
                AnimateThread.start()
                FillerThread = Thread(target=Filler)
                FillerThread.start()

            else:
                AnimateThread = Thread(target=AnimateHeader, args=["You turned filler off", uiInstance.animationColor])
                AnimateThread.start()
                RunFiller = False

        else:
            LinesSent += 1
            if LinesSent > 15:
                AnimateThread = Thread(target=AnimateHeader, args=["You created a new page", uiInstance.animationColor])
                AnimateThread.start()
                History.clear()
                LinesSent = 2

            ChatHistory.append(Message)
            History.append(Message)


def SendToServer():
    Message = MessageInput.value
    if Message:
        if Message == "/leave":
            connectionInstance.leave()
        else:
            if len(Message) + len(connectionInstance.username) + 2 >= 80:
                AnimateThread = Thread(target=AnimateHeader,
                                       args=["Your message is too long.", uiInstance.animationColor])
                AnimateThread.start()

            else:
                connectionInstance.socket.send(Message.encode())
                MessageInput.clear()

class Connection:
    def __init__(self, username, color, host, port, privateKey):
        self.username = username
        self.color = color
        self.host = host
        self.port = port
        self.privateKey = privateKey
        self.socket = socket.socket()

    def connect(self, usernameInput, colorInput, hostInput, portInput, privateKeyInput):
        self.username = usernameInput.value
        self.color = colorInput.value
        self.host = hostInput.value
        self.port = int(portInput.value, base=10)
        self.privateKey = privateKeyInput.value.split(", ")

        try:
            self.d = int(self.privateKey[0], base=10)
            self.N = int(self.privateKey[1], base=10)
            # Checks: if the private key is formatted correctly

            if not self.username == "" and not self.username == "Username" and not " " in self.username:
                # Checks: if username is not empty, not Username and does not contain spaces
                if not self.color.casefold() == "khaki":
                    try:
                        self.socket.connect((self.host, self.port))
                        self.socket.send(self.username.encode())

                        Status.value = "Connection Success"
                        Status.text_color = "lightblue"

                        UI.openChat(uiInstance)

                    except ConnectionRefusedError:
                        Status.value = "Connection Full"

                    except OSError:
                        Status.value = "Restart Client"
                        Status.text_color = "red"

                    except BrokenPipeError:
                        setupWindow.hide()

                        Status.value = "Broken Pipe"
                        Status.text_color = "red"
                else:
                    Status.value = "Color Locked"
            else:
                Status.value = "Invalid Username"
        except IndexError:
           Status.value = "Index Error"

    def leave(self):
        self.socket.send("/leave".encode())

        setUp.hide()
        setupWindow.hide()

        self.socket.close()
        print("You have disconnected.")
        quit()

class UI:
    def __init__(self, font, fontSize):
        self.font = font
        self.fontSize = fontSize
        self.color = connectionInstance.color
        self.animationColor = (173, 216, 230)
        self.animationRunning = False

    def openChat(self):
        global setupWindow, setupWindowOpened, setUpOpened
        setupWindow = Window(setUp, width=1200, height=590, title="setupWindow")
        setupWindow.when_closed = connectionInstance.leave
        setupWindow.font = self.color
        setupWindow.bg = (70, 70, 70)

        topPadding = Box(setupWindow, width="fill", height=50, align="top")
        leftPadding = Box(setupWindow, width=50, height="fill", align="left")
        rightPadding = Box(setupWindow, width=50, height="fill", align="right")
        bottomPadding = Box(setupWindow, width="fill", height=50, align="bottom")

        global MainBox
        MainBox = Blockers(setupWindow, "fill", "fill")
        MainBox.set_border(3, (173, 216, 230))
        self.border = MainBox

        Header = Box(MainBox, width="fill", height=40, align="top")

        ButtonBlocker = Box(MainBox, width="fill", height=3, align="bottom")
        ButtonBox = Box(MainBox, width="fill", height=40, align="bottom")

        UserBlocker = Box(MainBox, width="fill", height=3, align="top")
        UserBox = Blockers(MainBox, "fill", "fill")

        global UserList
        UserList = ListBox(UserBox, items=["Users Online:"], width=150, height="fill", align="left")
        UserList.text_color = (0, 0, 0)
        UserList.bg = (215, 215, 215)
        UserList.text_size = self.fontSize - 4

        self.userList = UserList

        global DisplayHeader
        DisplayHeader = Texts(Header, ("Welcome " + connectionInstance.username), 30, (0, 0, 0))
        DisplayHeader.bg = (255, 255, 255)
        DisplayHeader.width = "fill"

        self.header = DisplayHeader

        HistoryBlocker = Boxes(UserBox, 3, "fill", "left")

        global History
        History = TextBox(UserBox, "Hi!", "fill", height="fill", multiline=True, align="left")
        History.text_color = connectionInstance.color
        History.bg = (255, 255, 255)
        History.text_size = self.fontSize
        History.disable()

        self.chatHistory = History

        global SendButton
        SendButton = Buttons(ButtonBox, "Send", SendToServer)
        SendButton.text_color = (0, 0, 0)
        SendButton.bg = (255, 255, 255)
        SendButton.align = "right"

        global MessageInput
        MessageInput = TextBox(ButtonBox, width="fill", height="fill", align="bottom")
        MessageInput.text_color = connectionInstance.color
        MessageInput.bg = (255, 255, 255)
        MessageInput.text_size = self.fontSize + 2

        self.messageInput = MessageInput

        ##Threads start here

        global ListeningThread
        ListeningThread = Thread(target=AlwaysUpdate)
        ListeningThread.start()

        setupWindowOpened = True
        setUpOpened = False
        setUp.hide()
        setupWindow.show()

    def openSetup(self):
        global setUp, setUpOpened, Status

        setUp = App(title="Connect To Server", height=275, width=800)
        setUp.bg = (70, 70, 70)
        setUp.font = "San Francisco Bold"
        setUpOpened = True

        InputBox = Box(setUp, width="fill", height=275, align="left")
        rightPadding = Box(setUp, width=16, height="fill", align="right")
        VerifyBox = Box(setUp, width=400, height=150, align="right")

        Status = Texts(VerifyBox, "Not Connected", 34, (255, 255, 255))

        leftBlocker = Box(InputBox, width="fill", height=60, align="top")
        rightBlocker = Box(VerifyBox, width="fill", height=40, align="top")

        usernameBlocker = Box(InputBox, width=15, height=150, align="right")
        usernameInputBox = Blockers(InputBox, 275, 30)
        colorBlocker = Box(InputBox, width=15, height=120, align="right")
        colorInputBox = Blockers(InputBox, 260, 30)
        hostBlocker = Box(InputBox, width=15, height=90, align="right")
        hostInputBox = Blockers(InputBox, 245, 30)
        portBlocker = Box(InputBox, width=15, height=60, align="right")
        portInputBox = Blockers(InputBox, 230, 30)
        keyBlocker = Box(InputBox, width=15, height=30, align="right")
        keyInputBox = Blockers(InputBox, 215, 30)
        usernameInput = TextBoxes(usernameInputBox, connectionInstance.username)
        colorInput = TextBoxes(colorInputBox, connectionInstance.color)
        hostInput = TextBoxes(hostInputBox, connectionInstance.host)
        portInput = TextBoxes(portInputBox, connectionInstance.port)
        keyInput = TextBoxes(keyInputBox, connectionInstance.privateKey)

        AttemptConnect = PushButton(VerifyBox, text="Connect", command=connectionInstance.connect, args=
                                    [usernameInput, colorInput, hostInput, portInput, keyInput])
        AttemptConnect.text_size = self.fontSize - 4

        setUpOpened = True
        setUp.display()

#connectionInstance = Connection("Username", "Chat Color", "Host IP", "Port", "Private Key")
connectionInstance = Connection("tomm", "lightblue", "192.168.1.138", "49129", "4205, 21389")

uiInstance = UI("San Francisco Bold", 22)
UI.openSetup(uiInstance)
