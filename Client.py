##7/9/2022
##V13 Beta
import platform
import socket
from time import sleep, localtime, strftime
from threading import Thread

import colorutils
from guizero import *

ChatHistory = []

ConnectWindowOpened = False
ChatroomOpened = False

DarkMode = False
StopRainbow = False
AnimationRunning = False

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
    Turn = 1
    while RunFiller == True:
        sleep(60)
        while AnimationRunning == True:
            sleep(5)

        Time = strftime("%H:%M", localtime())
        AnimateThread = Thread(target=AnimateHeader, args=[str(Time), instance.animationColor])
        AnimateThread.start()
        Turn += 1

def ModBorder():
    global AnimationRunning

    (R, G, B) = (173, 216, 230)

    while AnimationRunning == True:
        sleep(WaitTime)
    AnimationRunning = True

    while not (R, G, B) == (240, 230, 140):
        if R < 240:
            R += 1
        if G < 230:
            G += 1
        if B > 140:
            B -= 1

        MainBox.set_border(3, (R, G, B))

    AnimationRunning = False
    return

def FadeToColor(newColor, displayMessage):
    global AnimationRunning
    global Color
    try:
        oldTextColor = colorutils.Color(web=instance.color)
        newTextColor = colorutils.Color(web=newColor)

        if newColor.casefold() == "khaki" and Mod == False:
            AnimateThread = Thread(target=AnimateHeader,
                                   args=["You don't have the power to use this color", instance.animationColor])
            AnimateThread.start()
            return

        if oldTextColor == newTextColor:
            AnimateThread = Thread(target=AnimateHeader,
                                   args=["You can't change to the same color", instance.animationColor])
            AnimateThread.start()
            return

        while AnimationRunning == True:
            sleep(WaitTime)
        AnimationRunning = True

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

            History.text_color = (R, G, B)
            MessageInput.text_color = (R, G, B)

            sleep(Rate)

        if displayMessage == True:
            AnimateThread = Thread(target=AnimateHeader, args=["You changed the text color", instance.animationColor])
            AnimateThread.start()

        # Once completed
        instance.color = newColor

    except:
        AnimateThread = Thread(target=AnimateHeader, args=["You cannot use an undefined color", AnimationColor])
        AnimateThread.start()

    AnimationRunning = False
    return

def AnimateHeader(Message, Color):
    global AnimationRunning

    while AnimationRunning == True:
        sleep(WaitTime)
    AnimationRunning = True

    if DarkMode == False:
        (R, G, B) = (0, 0, 0)

        while not R == 255 or not G == 255 or not B == 255:
            # Text fades from any colour to white
            if R < 255:
                R += 1
            if G < 255:
                G += 1
            if B < 255:
                B += 1

            DisplayHeader.text_color = (R, G, B)
            sleep(Rate)

        DisplayHeader.value = Message

        while not R == Color[0] or not G == Color[1] or not B == Color[2]:
            # Fades background from white to color
            if R > Color[0]:
                R -= 1
            if G > Color[1]:
                G -= 1
            if B > Color[2]:
                B -= 1

            DisplayHeader.bg = (R, G, B)
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

            DisplayHeader.bg = (R, G, B)
            sleep(Rate)

        DisplayHeader.value = "Welcome " + instance.username

        while not R == 0 or not G == 0 or not B == 0:
            # Text fades from white to black
            if R > 0:
                R -= 1
            if G > 0:
                G -= 1
            if B > 0:
                B -= 1

            DisplayHeader.text_color = (R, G, B)
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

            DisplayHeader.text_color = (R, G, B)
            sleep(Rate)

        DisplayHeader.value = Message

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

            DisplayHeader.bg = (R, G, B)
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

            DisplayHeader.bg = (R, G, B)
            sleep(Rate)

        DisplayHeader.value = "Welcome " + instance.username

        while not R == 255 or not G == 255 or not B == 255:
            # Text fades from black to white
            if R < 255:
                R += 1
            if G < 255:
                G += 1
            if B < 255:
                B += 1

            DisplayHeader.text_color = (R, G, B)
            sleep(Rate)

    AnimationRunning = False
    return

def SwitchTheme(DisplayMessage):
    global DarkMode
    global AnimationRunning

    while AnimationRunning == True:
        sleep(WaitTime)
    AnimationRunning = True

    if DarkMode == True:
        while DarkMode == True:
            # To turn Dark Mode off
            (R, G, B) = (255, 255, 255)

            while not (R, G, B) == (0, 0, 0):
                # Text Fades to Black
                R -= 1
                G -= 1
                B -= 1

                UserList.text_color = (R, G, B)
                DisplayHeader.text_color = (R, G, B)
                sleep(Rate)

            while not (R, G, B) == (215, 215, 215):
                # All backgrounds fade from black to white
                R += 1
                G += 1
                B += 1

                DisplayHeader.bg = (R, G, B)
                History.bg = (R, G, B)
                MessageInput.bg = (R, G, B)
                UserList.bg = (R, G, B)
                sleep(Rate)

            while not (R, G, B) == (255, 255, 255):
                R += 1
                G += 1
                B += 1

                DisplayHeader.bg = (R, G, B)
                History.bg = (R, G, B)
                MessageInput.bg = (R, G, B)
                sleep(Rate)

            DarkMode = False

    else:
        while DarkMode == False:
            # To turn Dark Mode on
            R = 0
            G = 0
            B = 0

            while not (R, G, B) == (255, 255, 255):
                # Text Fades to White
                R += 1
                G += 1
                B += 1

                UserList.text_color = (R, G, B)
                DisplayHeader.text_color = (R, G, B)

            while not (R, G, B) == (70, 70, 70):
                # All Background fade to grey
                R -= 1
                G -= 1
                B -= 1

                MessageInput.bg = (R, G, B)
                History.bg = (R, G, B)
                DisplayHeader.bg = (R, G, B)
                UserList.bg = (R, G, B)
                sleep(Rate)

            while not (R, G, B) == (40, 40, 40):
                R -= 1
                G -= 1
                B -= 1

                UserList.bg = (R, G, B)
                sleep(Rate)

            DarkMode = True

    AnimationRunning = False
    History.text_color = instance.color
    MessageInput.text_color = instance.color

    if DisplayMessage == True:
        if DarkMode == True:
            AnimateThread = Thread(target=AnimateHeader,
                                   args=["You turned dark mode on", instance.animationColor])
            AnimateThread.start()
        else:
            AnimateThread = Thread(target=AnimateHeader,
                                   args=["You turned light mode on", instance.animationColor])
            AnimateThread.start()

    return

def SaveChatHistory(Location):
    if Location and not " " in Location:
        File = open(Location, "w")
        for Chat in ChatHistory:
            File.write(Chat)
            File.write("\n")
        File.close()

        AnimateThread = Thread(target=AnimateHeader, args=["Your file has been saved", instance.animationColor])
        AnimateThread.start()

    else:
        AnimateThread = Thread(target=AnimateHeader,
                               args=["You can't save to this location", instance.animationColor])
        AnimateThread.start()

    return

def RSADecrypt(Message):
    Message = Message.split()
    RSADecryptedMessage = []

    for Letter in Message:
        Letter = int(Letter, base=10)
        Index = pow(Letter, instance.d, instance.N)
        RSADecryptedLetter = chr(Index)
        RSADecryptedMessage.append(RSADecryptedLetter)

    Message = str("".join(RSADecryptedMessage))
    return Message

def AlwaysUpdate():
    global LinesSent, Mod, AnimationColor, RunFiller
    Users = []
    while True:
        Message = instance.socket.recv(1024).decode()
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
            if Message[8:] == instance.username:
                instance.leave()
                break
            User = Message[8:]
            UserList.remove(User)
            Users.remove(User)
            Message = User + " has disconnected"
            AnimateThread = Thread(target=AnimateHeader, args=[Message, instance.animationColor])
            AnimateThread.start()

        elif Message[0:8] == "/display":
            Message = Message[9:]
            AnimateThread = Thread(target=AnimateHeader, args=[Message, instance.animationColor])
            AnimateThread.start()

        elif Message == "/theme":
            AnimateThread = Thread(target=SwitchTheme, args=[True])
            AnimateThread.start()

        elif Message[0:4] == "/mod":
            if Message[5:] == instance.username and Mod == False:
                instance.animationColor = (240, 230, 140)
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
            instance.newColor = Message[7:]
            AnimateThread = Thread(target=FadeToColor, args=[instance.newColor, True])
            AnimateThread.start()

        elif Message[0:5] == "/save":
            Location = Message[6:]
            SaveChatThread = Thread(target=SaveChatHistory, args=[Location])
            SaveChatThread.start()

        elif Message == "/disconnect":
            AnimateThread = Thread(target=AnimateHeader, args=["You cannot use this username", instance.animationColor])
            AnimateThread.start()
            while True:
                AnimateThread = Thread(target=AnimateHeader, args=["You are not connected", (216, 36, 41)])
                AnimateThread.start()
                sleep(Rate)

        elif Message == "/filler":
            if RunFiller == False:
                RunFiller = True
                AnimateThread = Thread(target=AnimateHeader, args=["You turned filler on", instance.animationColor])
                AnimateThread.start()
                FillerThread = Thread(target=Filler)
                FillerThread.start()

            else:
                AnimateThread = Thread(target=AnimateHeader, args=["You turned filler off", instance.animationColor])
                AnimateThread.start()
                RunFiller = False

        else:
            LinesSent += 1
            if LinesSent > 15:
                AnimateThread = Thread(target=AnimateHeader, args=["You created a new page", instance.animationColor])
                AnimateThread.start()
                History.clear()
                LinesSent = 2

            ChatHistory.append(Message)
            History.append(Message)


def SendToServer():
    Message = MessageInput.value
    if Message:
        if Message == "/leave":
            instance.leave()
        else:
            if len(Message) + len(instance.username) + 2 >= 80:
                AnimateThread = Thread(target=AnimateHeader,
                                       args=["Your message is too long.", instance.animationColor])
                AnimateThread.start()

            else:
                instance.socket.send(Message.encode())
                MessageInput.clear()

class Connection:
    def __init__(self, username, color, host, port, privateKey):
        self.username = username
        self.color = color
        self.host = host
        self.port = port
        self.privateKey = privateKey
        self.animationColor = (173, 216, 230)
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

                        OpenChat()

                    except ConnectionRefusedError:
                        Status.value = "Connection Full"

                    except OSError:
                        Status.value = "Restart Client"
                        Status.text_color = "red"

                    except BrokenPipeError:
                        Chatroom.hide()

                        Status.value = "Broken Pipe"
                        Status.text_color = "red"
                else:
                    Status.value = "Color Locked"
            else:
                Status.value = "Invalid Username"
        except IndexError:
           Status.value = "Index Error"

        return self.username, self.color, self.host, self.port, self.d, self.N

    def leave(self):
        self.socket.send("/leave".encode())

        if ConnectWindowOpened == True:
            ConnectWindow.hide()

        if ChatroomOpened == True:
            Chatroom.hide()

        self.socket.close()
        print("You have disconnected.")
        quit()

def OpenChat():
    global Chatroom, ChatroomOpened, ConnectWindowOpened
    Chatroom = Window(ConnectWindow, width=1200, height=590, title="Chatroom")
    Chatroom.when_closed = instance.leave
    Chatroom.font = "San Francisco Bold"
    Chatroom.bg = (70, 70, 70)
    ChatroomOpened = True

    topPadding = Box(Chatroom, width="fill", height=50, align="top")
    leftPadding = Box(Chatroom, width=50, height="fill", align="left")
    rightPadding = Box(Chatroom, width=50, height="fill", align="right")
    bottomPadding = Box(Chatroom, width="fill", height=50, align="bottom")

    global MainBox
    MainBox = Blockers(Chatroom, "fill", "fill")
    MainBox.set_border(3, (173, 216, 230))

    Header = Box(MainBox, width="fill", height=40, align="top")

    ButtonBlocker = Box(MainBox, width="fill", height=3, align="bottom")
    ButtonBox = Box(MainBox, width="fill", height=40, align="bottom")

    UserBlocker = Box(MainBox, width="fill", height=3, align="top")
    UserBox = Blockers(MainBox, "fill", "fill")

    global UserList
    UserList = ListBox(UserBox, items=["Users Online:"], width=150, height="fill", align="left")
    UserList.text_color = (0, 0, 0)
    UserList.bg = (215, 215, 215)
    UserList.text_size = 18

    global DisplayHeader
    DisplayHeader = Texts(Header, ("Welcome " + instance.username), 30, (0, 0, 0))
    DisplayHeader.bg = (255, 255, 255)
    DisplayHeader.width = "fill"

    HistoryBlocker = Boxes(UserBox, 3, "fill", "left")

    global History
    History = TextBox(UserBox, "Hi!", "fill", height="fill", multiline=True, align="left")
    History.text_color = instance.color
    History.bg = (255, 255, 255)
    History.text_size = 22
    History.disable()

    global SendButton
    SendButton = Buttons(ButtonBox, "Send", SendToServer)
    SendButton.text_color = (0, 0, 0)
    SendButton.bg = (255, 255, 255)
    SendButton.align = "right"

    global MessageInput
    MessageInput = TextBox(ButtonBox, width="fill", height="fill", align="bottom")
    MessageInput.text_color = instance.color
    MessageInput.bg = (255, 255, 255)
    MessageInput.text_size = 24

    ##Threads start here

    global ListeningThread
    ListeningThread = Thread(target=AlwaysUpdate)
    ListeningThread.start()

    ChatroomOpened = True
    ConnectWindowOpened = False
    ConnectWindow.hide()
    Chatroom.show()

def OpenConnectWindow():
    global ConnectWindow, ConnectWindowOpened, Status

    ConnectWindow = App(title="Connect To Server", height=275, width=800)
    ConnectWindow.bg = (70, 70, 70)
    ConnectWindow.font = "San Francisco Bold"
    ConnectWindowOpened = True

    InputBox = Box(ConnectWindow, width="fill", height=275, align="left")
    rightPadding = Box(ConnectWindow, width=16, height="fill", align="right")
    VerifyBox = Box(ConnectWindow, width=400, height=150, align="right")

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
    usernameInput = TextBoxes(usernameInputBox, instance.username)
    colorInput = TextBoxes(colorInputBox, instance.color)
    hostInput = TextBoxes(hostInputBox, instance.host)
    portInput = TextBoxes(portInputBox, instance.port)
    keyInput = TextBoxes(keyInputBox, instance.privateKey)

    AttemptConnect = PushButton(VerifyBox, text="Connect", command=instance.connect, args=
                                [usernameInput, colorInput, hostInput, portInput, keyInput])
    AttemptConnect.text_size = 16

    ConnectWindowOpened = True
    ConnectWindow.display()

instance = Connection("Username", "Chat Color", "Host IP", "Port", "Private Key")
#instance = Connection("tomm", "lightblue", "192.168.1.138", "49128", "2143, 15251")

OpenConnectWindow()
