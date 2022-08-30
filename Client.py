##30/8/2022
##V13 Beta

import socket
from time import sleep
from threading import Thread
from guizero import *

s = socket.socket()

Host = '192.168.1.138'
Port = 0000
Username = "tomm"
Color = "rainbow"

ChatHistory = []

ConnectWindowOpened = False
ChatroomOpened = False

DarkMode = False
StopRainbow = False

IdentifiedSelf = False

Location = " - "
PrivateKey = ""


class Boxes(Box):
    # This is for UI design. This allows creations of box instances.
    def __init__(self, master, width, height, align):
        super().__init__(master, width=width, height=height, align=align)
        self.width = width
        self.height = height
        self.align = align


class Buttons(PushButton):
    # This is for UI design. Allows easier creation of button instances.
    def __init__(self, master, text, width, height, align, command):
        super().__init__(master, text=text, width=width, height=height, align=align, command=command)
        self.text = text
        self.width = width
        self.height = height
        self.align = align
        self.command = command


class InputBoxes(Box):
    # This is for UI design. This creates space for the User-input textboxes to fit in.
    def __init__(self, master, width, height):
        super().__init__(master, width=width, height=height)
        self.width = width
        self.height = height


class InputTextBoxes(TextBox):
    # Allows for creation of User-input instances
    def __init__(self, master, text):
        super().__init__(master, text=text, width="fill")
        self.text = text
        self.text_size = 16
        self.text_color = "lightblue"
        self.bg = (40, 40, 40)


def AnimateHeader(Message, Color):
    R = 0
    G = 0
    B = 0
    Rate = 0.00125

    if DarkMode == False:
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

        DisplayHeader.value = "Welcome " + Username

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

        DisplayHeader.value = "Welcome " + Username

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

def InfiniteRainbow(Element):
    R = 255
    G = 0
    B = 0
    Rate = 0.0025
    while True:
        if StopRainbow == False:
            while not G == 255:
                G += 1

                RGB = (R, G, B)

                Element.text_color = RGB
                sleep(Rate)

            while not R == 0:
                R -= 1

                RGB = (R, G, B)

                Element.text_color = RGB
                sleep(Rate)

            while not B == 255:
                B += 1

                RGB = (R, G, B)

                Element.text_color = RGB
                sleep(Rate)
            while not G == 0:
                G -= 1

                RGB = (R, G, B)

                Element.text_color = RGB
                sleep(Rate)

            while not R == 255:
                R += 1

                RGB = (R, G, B)

                Element.text_color = RGB
                sleep(Rate)

            while not B == 0:
                B -= 1

                RGB = (R, G, B)

                Element.text_color = RGB
                sleep(Rate)
        else:
            while (not G == 255) and (not B == 255):
                G += 1
                B += 1

                RGB = (R, G, B)
                Element.text_color = RGB
                sleep(Rate)

            break


def SwitchTheme():
    global DarkMode
    Rate = 0.00125
    if DarkMode == True:
        while DarkMode == True:
            R = 0
            G = 0
            B = 0

            while not (R, G, B) == (215, 215, 215):
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
            R = 255
            G = 255
            B = 255

            while not (R, G, B) == (70, 70, 70):
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

    UserList.text_color = Color
    History.text_color = Color
    MessageInput.text_color = Color

def SaveChatHistory():
    global Location

    if Location and not Location == "Change Location":
        File = open(Location, "w")
        for Chat in ChatHistory:
            File.write(Chat)
            File.write("\n")
        File.close()

        History.append(("[Device] Saved Chat History in: " + Location))
        Message = "has saved the chat"
        s.send(Message.encode())

    else:
        Location = " - "
        History.append("[Device] Saving Unsuccessful")

def RSADecrypt(Message):
    Message = Message.split()
    RSADecryptedMessage = []

    for Letter in Message:
        Letter = int(Letter, base=10)
        Index = pow(Letter, d, N)
        RSADecryptedLetter = chr(Index)
        RSADecryptedMessage.append(RSADecryptedLetter)

    Message = str("".join(RSADecryptedMessage))
    return Message

def AlwaysUpdate():
    Users = []
    while True:
        Message = s.recv(1024).decode()
        Message = RSADecrypt(Message)

        if Message[0:4] == "/add":
            Message = Message[5:]
            Message = Message.split()

            UserList.clear()
            UserList.append("Users Online:")

            for User in Message:
                if User not in Users:
                    UserList.append(User)
                    Users.append(User)
                    Message = User + " has connected"
                    AnimateHeader(Message, (124, 252, 0))
                else:
                    UserList.append(User)

        elif Message[0:7] == "/remove":
            Message = Message[8:]
            UserList.remove(Message)
            Users.remove(Message)
            Message = Message + " has disconnected"
            AnimateHeader(Message, (216, 36, 41))

        elif Message[0:8] == "/display":
            Message = Message[9:]
            AnimateHeader(Message, (173, 216, 230))

        elif Message == "/theme":
            SwitchTheme()
            sleep(0.1)
            if DarkMode == True:
                AnimateHeader("Dark Mode Turned On", (173, 216, 230))
            else:
                AnimateHeader("Light Mode Turned On", (173, 216, 230))

        else:
            History.append(Message)

def SendToServer():
    Message = MessageInput.value
    if Message:
        if Message == "/leave":
            Leave()
        else:
            s.send(Message.encode())
            MessageInput.clear()

def Leave():
    s.send(("/leave").encode())

    if ConnectWindowOpened == True:
        ConnectWindow.hide()

    if ChatroomOpened == True:
        Chatroom.hide()
        ListeningThread.join()

    s.close()

def Connect():
    global Username
    global Color
    global Host, Port
    global d, N
    global PrivateKey

    Username = str(UsernameInput.value)
    Host = HostInput.value
    Color = (ColorInput.value).casefold()

    PrivateKey = str(KeyInput.value)
    PrivateKey = PrivateKey.split(", ")

    try:
        if PrivateKey[0] and PrivateKey[1]:
            d = int(PrivateKey[0], base=10)
            N = int(PrivateKey[1], base=10)

            PrivateKey = ", ".join(PrivateKey)
            if (not Username == "") and (not Username == "Username") and (not " " in Username):
                try:
                    Port = int(PortInput.value, base=10)

                    s.connect((Host, Port))
                    s.send(Username.encode())

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
                Status.value = "Invalid Username"
        else:
            Status.value = "Invalid Key"
    except IndexError:
        Status.value = "Index Error"


def OpenChat():
    global Chatroom, ChatroomOpened, ConnectWindowOpened
    Chatroom = Window(ConnectWindow, width=900, height=500, title="Chatroom")
    Chatroom.when_closed = Leave
    Chatroom.font = "San Francisco Bold"
    Chatroom.bg = "white"
    Chatroom.text_color = "black"
    ChatroomOpened = True

    Header = Boxes(Chatroom, "fill", 40, "top")
    ButtonBox = Boxes(Chatroom, "fill", 40, "bottom")
    UserBox = Boxes(Chatroom, 150, "fill", "left")

    global UserList
    UserList = ListBox(UserBox, items=["Users Online:"], height="fill", scrollbar=True)
    UserList.text_color = Color
    UserList.bg = (215, 215, 215)
    UserList.text_size = 18

    global DisplayHeader
    DisplayHeader = Text(Header, text=("Welcome " + Username), width="fill")
    DisplayHeader.text_size = 30

    global History
    History = TextBox(Chatroom, text="Hi!", height="fill", width="fill", multiline=True, scrollbar=True, align="top")
    History.text_color = Color
    History.text_size = 22
    History.disable()

    global SendButton
    SendButton = PushButton(ButtonBox, text="Send", command=SendToServer, align="right")
    SendButton.text_color = (0, 0, 0)
    SendButton.bg = (255, 255, 255)

    global MessageInput
    MessageInput = TextBox(ButtonBox, height="fill", width="fill")
    MessageInput.text_color = Color
    MessageInput.text_size = 24

    ##Threads start here

    global ListeningThread, RainbowHeaderThread
    ListeningThread = Thread(target=AlwaysUpdate)
    ListeningThread.start()

    ChatroomOpened = True
    ConnectWindowOpened = False
    ConnectWindow.hide()
    Chatroom.show()

def OpenConnectWindow():
    global ConnectWindow, ConnectWindowOpened

    ConnectWindow = App(title="Connect To Server", height=275, width=800)
    ConnectWindow.bg = (70, 70, 70)
    ConnectWindow.font = "San Francisco Bold"
    ConnectWindowOpened = True

    InputBox = Boxes(ConnectWindow, "fill", 275, "left")
    RightPadding = Boxes(ConnectWindow, 16, "fill", "right")
    VerifyBox = Boxes(ConnectWindow, 400, 150, "right")

    global Status
    Status = Text(VerifyBox, text="Not Connected")
    Status.text_size = 34
    Status.text_color = "white"

    LeftBlocker = Boxes(InputBox, "fill", 60, "top")
    RightBlocker = Boxes(VerifyBox, "fill", 40, "top")

    AttemptConnect = PushButton(VerifyBox, text="Connect", command=Connect)
    AttemptConnect.text_size = 16

    global UsernameInput, ColorInput, HostInput, PortInput, KeyInput

    UsernameBlocker = Boxes(InputBox, 15, 150, "right")
    UsernameInputBox = InputBoxes(InputBox, 275, 30)
    ColorBlocker = Boxes(InputBox, 15, 120, "right")
    ColorInputBox = InputBoxes(InputBox, 260, 30)
    HostBlocker = Boxes(InputBox, 15, 90, "right")
    HostInputBox = InputBoxes(InputBox, 245, 30)
    PortBlocker = Boxes(InputBox, 15, 60, "right")
    PortInputBox = InputBoxes(InputBox, 230, 30)
    KeyBlocker = Boxes(InputBox, 15, 30, "right")
    KeyInputBox = InputBoxes(InputBox, 215, 30)
    UsernameInput = InputTextBoxes(UsernameInputBox, "Username")
    ColorInput = InputTextBoxes(ColorInputBox, "Chat Color")
    HostInput = InputTextBoxes(HostInputBox, "Host IP")
    PortInput = InputTextBoxes(PortInputBox, "Port")
    KeyInput = InputTextBoxes(KeyInputBox, "Private Key")

    ConnectWindowOpened = True
    ConnectWindow.display()

OpenConnectWindow()
