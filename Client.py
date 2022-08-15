##15/8/2022
##V13 RC2

import random
import socket
import time
from threading import Thread
from guizero import *

s = socket.socket()

Host = '192.168.1.138'
Port = 0000
Username = "tomm"
Color = "rainbow"

ColorsList = ["red", "green", "yellow", "blue", "lightblue", "purple", "coral",
              "black", "white", "pink", "brown", "grey", "orange", "rainbow"]
ChatHistory = []

SettingsOpened = False
ConnectWindowOpened = False
ChatroomOpened = False

DarkMode = False
StopRainbow = False
        
Location = " - "
PrivateKey = ""

def InfiniteRainbow(Element):
    R = 255
    G = 0
    B = 0
    Rate = 0.0025
    while True:
        while not G == 255:
            G += 1

            RGB = (R, G, B)

            Element.text_color = RGB
            time.sleep(Rate)

        while not R == 0:
            R -= 1

            RGB = (R, G, B)

            Element.text_color = RGB
            time.sleep(Rate)

        while not B == 255:
            B += 1

            RGB = (R, G, B)

            Element.text_color = RGB
            time.sleep(Rate)
        while not G == 0:
            G -= 1

            RGB = (R, G, B)

            Element.text_color = RGB
            time.sleep(Rate)

        while not R == 255:
            R += 1

            RGB = (R, G, B)

            Element.text_color = RGB
            time.sleep(Rate)

        while not B == 0:
            B -= 1

            RGB = (R, G, B)

            Element.text_color = RGB
            time.sleep(Rate)

def Rainbow(Element):
    R = 255
    G = 0
    B = 0
    Rate = 0.0025
    while True:
        if StopRainbow == False:
            while not G == 255 and StopRainbow == False:
                G += 1

                RGB = (R, G, B)

                Element.text_color = RGB
                time.sleep(Rate)

            while not R == 0 and StopRainbow == False:
                R -= 1

                RGB = (R, G, B)

                Element.text_color = RGB
                time.sleep(Rate)

            while not B == 255 and StopRainbow == False:
                B += 1

                RGB = (R, G, B)

                Element.text_color = RGB
                time.sleep(Rate)
            while not G == 0 and StopRainbow == False:
                G -= 1

                RGB = (R, G, B)

                Element.text_color = RGB
                time.sleep(Rate)

            while not R == 255 and StopRainbow == False:
                R += 1

                RGB = (R, G, B)

                Element.text_color = RGB
                time.sleep(Rate)

            while not B == 0 and StopRainbow == False:
                B -= 1

                RGB = (R, G, B)

                Element.text_color = RGB
                time.sleep(Rate)
        else:
            History.text_color = Color

            if DarkMode == True:
                MessageInput.text_color = "white"
                UserList.text_color = "white"
                
            else:
                MessageInput.text_color = "black"
                UserList.text_color = "black"
     
            break

def SwitchTheme():
    global DarkMode
    global Color
    if ChatroomOpened == True:
        if DarkMode == True:      
            Chatroom.bg = "white"
            UserList.bg = (215, 215, 215)
            
            Chatroom.text_color = "black"                        
            MessageInput.text_color = "black"

            SaveChat.text_color = "black"
            DarkModeToggle.text_color = "black"
            ChangeColorButton.text_color = "black"

            DarkMode = False

        else:
            Chatroom.bg = (70, 70, 70)
            UserList.bg = (40, 40, 40)
            
            Chatroom.text_color = "white"
            MessageInput.text_color = "white"

            DarkMode = True
            
        if not Color.casefold() == "rainbow":
            History.text_color = Color

        SendButton.bg = "white"
        SettingsButton.bg = "white"
        ShowInfoButton.bg = "white"

        SendButton.text_color = "black"
        SettingsButton.text_color = "black"
        ShowInfoButton.text_color = "black"

        Settings.hide()

def ChangeColor():
    global Color
    global StopRainbow
    if (SettingsColorInput.value).casefold() in ColorsList:
        if (SettingsColorInput.value).casefold() == "rainbow":
            StopRainbow = False
            
            RainbowHistoryThread = Thread(target = Rainbow, args = (History,))
            RainbowHistoryThread.start()
            RainbowMessageInputThread = Thread(target = Rainbow, args = (MessageInput,))
            RainbowMessageInputThread.start()
            RainbowUserListThread = Thread(target = Rainbow, args = (UserList,))
            RainbowUserListThread.start()
                       
            Color = "rainbow"
            
        else:            
            StopRainbow = True
    
            Color = SettingsColorInput.value
            History.text_color = Color
            
    else:
        History.append("[Device] Try another Color.")

    Settings.hide()
             
def SaveChatHistory():
    global Location
    Location = ChangeLocation.value

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
        
    ChangeLocation.clear()
    Settings.hide()

def ShowPrivateKey():
    SettingsKeyDisplay.hide_text = False

def RSADecrypt(Message):
    Message = Message.split()
    RSADecryptedMessage = []
    
    for Letter in Message:
        Letter = int(Letter, base = 10)
        Index = pow(Letter, d, N)
        RSADecryptedLetter = chr(Index)
        RSADecryptedMessage.append(RSADecryptedLetter)

    Message = str("".join(RSADecryptedMessage))
    return Message

      
def AlwaysUpdate():
    while True:
        try:
            Message = s.recv(1024).decode()
            Message = RSADecrypt(Message)
            
            if Message[0:4] == "/add":
                Message = Message[5:]
                Message = Message.split()

                UserList.clear()
                UserList.append("Users Online:")
                
                for User in Message:
                    if User == Username:
                        UserList.append((User + " (self)"))
                    else:
                        UserList.append(User)

            elif Message[0:7] == "/remove":
                Message = Message[8:]
                UserList.remove(Message)

            else:         
                History.append(Message)
                ChatHistory.append(Message)
                
        except:
            print("The Server has shut down.")
            break

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

    if SettingsOpened == True:
        Settings.hide()

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
            d = int(PrivateKey[0], base = 10)
            N = int(PrivateKey[1], base = 10)
     
            PrivateKey = ", ".join(PrivateKey)
            if Color in ColorsList:
                if (not Username == "") and (not Username == "Username") and (not " " in Username):
                    try:        
                        Port = int(PortInput.value, base = 10)               
                      
                        s.connect((Host, Port))
                        s.send(Username.encode())

                        Status.value = "Connection Success"
                        Status.text_color = "lightblue"

                        OpenChat()
                    
                    except ConnectionRefusedError:
                        Status.value = "Connection Full"
                        Status.text_color = "yellow"
                        
                    except OSError:
                        Status.value = "Restart Client"
                        Status.text_color = "red"

                    except BrokenPipeError:
                        Chatroom.hide()

                        Status.value = "Broken Pipe"
                        Status.text_color = "red"
                else:
                    Status.value = "Invalid Username"
                    Status.text_color = "yellow"
            else:
                Status.value = "Invalid Color"
                Status.text_color = "yellow"    
        else:
            Status.value = "Invalid Key"
            Status.text_color = "yellow"
    except IndexError:
        Status.value = "Input Error"
        Status.text_color = "yellow"

def OpenInfo():
    Info = Window(Chatroom, width = 800, height = 380, title = "Information")

    InfoText = TextBox(Info, text = "About This Code:", width = "fill")
    InfoText.text_size = 20
    InfoText.text_color = "white"
    InfoText.disable()

    TopHeader = Box(Info, width = "fill", height = 30, align = "top")

    WarningText = TextBox(Info, text = ">If your Client begins to flicker, The Server has stopped all connections.", width = "fill")
    WarningText.text_size = 16
    WarningText.text_color = "white"
    WarningText.disable()

    LeaveText = TextBox(Info, text = ">The Connection automatically closes when you close the Chat Window.", width = "fill")
    LeaveText.text_size = 16
    LeaveText.text_color = "white"
    LeaveText.disable()

    RainbowText = TextBox(Info, text = ">It's highly recommended to not input an Animated Color in succession.", width = "fill")
    RainbowText.text_size = 16
    RainbowText.text_color = "white"
    RainbowText.disable()

def OpenSettings():
    global Settings, SettingsOpened, Color
    Settings = Window(Chatroom, width = 480, height = 650, title = "Settings")

    DetailsTitle = TextBox(Settings, text = "Details:", width = "fill", align = "top")
    DetailsTitle.text_size = 20
    DetailsTitle.disable()

    TopHeader = Box(Settings, width = "fill", height = 30, align = "top")

    BottomBox = Box(Settings, width = "fill", height = "fill", align = "bottom")

    MiddleBox = Box(Settings, width = "fill", height = 100, align = "bottom")

    LeftBox = Box(Settings, width = "fill", height = "fill", align = "left")

    RightBox = Box(Settings, width = "fill", height = "fill", align = "right")

    MiddleHeader = Box(MiddleBox, width = "fill", height = 30)

    SettingsTitle = TextBox(MiddleBox, text = "Advanced:", width = "fill")
    SettingsTitle.text_size = 20
    SettingsTitle.disable()
    
    UsernameDisplay = TextBox(LeftBox, text = ("Username: " + Username), width = "fill")
    UsernameDisplay.text_size = 16
    UsernameDisplay.disable()

    HostDisplay = TextBox(LeftBox, text = ("Host IP: " + str(Host)), width = "fill")
    HostDisplay.text_size = 16
    HostDisplay.disable()
    
    PortDisplay = TextBox(LeftBox, text = ("Port: " + str(Port)), width = "fill")
    PortDisplay.text_size = 16
    PortDisplay.disable()

    DarkmodeBox = Box(BottomBox, width = "fill", height = 70, align = "top")

    DarkmodeText = TextBox(DarkmodeBox, text = ("Dark Mode on: " + str(DarkMode)), width = "fill", align = "left")
    DarkmodeText.text_size = 16
    DarkmodeText.disable()
    
    global DarkModeToggle
    DarkModeToggle = PushButton(DarkmodeBox, text = "Switch Theme", command = SwitchTheme, width = "fill", align = "right")
    DarkModeToggle.text_color = "black"

    ColorBox = Box(BottomBox, width = "fill", height = 100, align = "top")

    Color = Color[0].upper() + Color[1:].lower()
    ColorText = TextBox(ColorBox, text = ("Chat Color: " + Color), width = "fill")
    ColorText.text_size = 16
    ColorText.disable()

    global SettingsColorInput
    SettingsColorInput = TextBox(ColorBox, text = "Change Color", width = "fill", align = "left")
    SettingsColorInput.bg = "white"
    SettingsColorInput.text_size = 16
    SettingsColorInput.text_color = "black"
    
    global ChangeColorButton
    ChangeColorButton = PushButton(ColorBox, text = "Change Color", command = ChangeColor, width = "fill", align = "right")
    ChangeColorButton.text_color = "black"

    SavingBox = Box(BottomBox, width = "fill", height = 100, align = "top")

    SaveLocation = TextBox(SavingBox, text = ("Save Chat History in: " + Location), width = "fill")
    SaveLocation.text_size = 16
    SaveLocation.disable()

    global ChangeLocation
    ChangeLocation = TextBox(SavingBox, text = "Change Location", width = "fill", align = "left")
    ChangeLocation.bg = "white"
    ChangeLocation.text_size = 16
    ChangeLocation.text_color = "black"
    
    global SaveChat
    SaveChat = PushButton(SavingBox, text = "Save Chat History", command = SaveChatHistory, width = "fill", align = "right")
    SaveChat.text_color = "black"

    KeyBox = Box(BottomBox, width = "fill", height = 100, align = "top")

    KeyDetails = TextBox(KeyBox, text = "Private Key Details:", width = "fill")
    KeyDetails.text_size = 16
    KeyDetails.text_color = "white"
    KeyDetails.disable()

    global SettingsKeyDisplay
    SettingsKeyDisplay = TextBox(KeyBox, text = PrivateKey, hide_text = True, width = "fill", align = "left")
    SettingsKeyDisplay.bg = "white"
    SettingsKeyDisplay.text_size = 16
    SettingsKeyDisplay.text_color = "black"    

    ShowKey = PushButton(KeyBox, text = "Show Private Key", command = ShowPrivateKey, width = "fill", align = "right")
    ShowKey.text_color = "black"

    SaveChat.text_color = "black"
    DarkModeToggle.text_color = "black"
    ChangeColorButton.text_color = "black"

    SettingsOpened = True
    Settings.show()

def OpenChat():
    global Chatroom, ChatroomOpened, ConnectWindowOpened
    Chatroom = Window(ConnectWindow, width = 900, height = 500, title = "Chatroom")
    Chatroom.when_closed = Leave
    Chatroom.font = "San Francisco Bold"
    Chatroom.bg = "white"
    Chatroom.text_color = "black"
    ChatroomOpened = True
    
    Header = Box(Chatroom, width = "fill", height = 50, align = "top")

    ButtonBox = Box(Chatroom, width = "fill", align = "bottom")

    UserBox = Box(Chatroom, width = 200, height = "fill", align = "left")

    global UserList
    UserList = ListBox(UserBox, items = ["Users Online:"], height = "fill", scrollbar = True)
    UserList.bg = (215, 215, 215)
    UserList.text_size = 18

    global UsernameDisplayHeader
    UsernameDisplayHeader = Text(Header, text = ("Welcome " + Username), align = "left")
    UsernameDisplayHeader.text_size = 30
    
    global History
    History = TextBox(Chatroom, text = "[Device] Starting Client", height = "fill", width = "fill", multiline = True, scrollbar = True, align = "top")
    History.text_size = 16
    History.disable()

    global SendButton
    SendButton = PushButton(ButtonBox, text = "Send", command = SendToServer, align = "right")
    SendButton.text_color = "black"

    global ShowInfoButton
    ShowInfoButton = PushButton(ButtonBox, text = "Info", command = OpenInfo, align = "left")
    ShowInfoButton.text_color = "black"
        
    global SettingsButton
    SettingsButton = PushButton(ButtonBox, text = "Settings", command = OpenSettings, align = "left")
    SettingsButton.text_color = "black"
    
    global MessageInput
    MessageInput = TextBox(ButtonBox, height = "fill", width = "fill")
    MessageInput.text_size = 24

##Threads start here
    
    global ListeningThread
    ListeningThread = Thread(target = AlwaysUpdate)
    ListeningThread.start()

    RainbowHeaderThread = Thread(target = InfiniteRainbow, args = (UsernameDisplayHeader,))
    RainbowHeaderThread.start()

    if Color == "rainbow":
        RainbowHistoryThread = Thread(target = Rainbow, args = (History,))                        
        RainbowHistoryThread.start()
        RainbowMessageInputThread = Thread(target = Rainbow, args = (MessageInput,))
        RainbowMessageInputThread.start()
        RainbowUserListThread = Thread(target = Rainbow, args = (UserList,))
        RainbowUserListThread.start()
        
    else:
        History.text_color = Color
        MessageInput.text_color = "black"
        UserList.text_color = "black"
        
    ChatroomOpened = True
    ConnectWindowOpened = False
    ConnectWindow.hide()
    Chatroom.show()
   
def OpenConnectWindow():    
    global ConnectWindow, ConnectWindowOpened
    ConnectWindow = App(title = "Connect To Server", height = 275, width = 800)
    ConnectWindow.bg = (70, 70, 70)
    ConnectWindow.font = "San Francisco Bold"
    ConnectWindowOpened = True
    
    InputBox = Box(ConnectWindow, width = "fill", align = "left")
    
    Padding = Box(ConnectWindow, width = 16, height = "fill", align = "right")

    VerifyBox = Box(ConnectWindow, width = 400, height = 150, align = "right")

    global Status
    Status = Text(VerifyBox, text = "Not Connected")
    Status.text_size = 34
    Status.text_color = "red"

    Blocker = Box(VerifyBox, width = "fill", height = 20)

    global AttemptConnect
    AttemptConnect = PushButton(VerifyBox, text = "Connect", command = Connect)
    AttemptConnect.text_size = 16

    UsernameBlocker = Box(InputBox, width = 15, height = 150, align = "right")
    UsernameInputBox = Box(InputBox, width = 275, height = 30)

    ColorBlocker = Box(InputBox, width = 15, height = 120, align = "right")
    ColorInputBox = Box(InputBox, width = 260, height = 30)

    HostBlocker = Box(InputBox, width = 15, height = 90, align = "right")
    HostInputBox = Box(InputBox, width = 245, height = 30)

    PortBlocker = Box(InputBox, width = 15, height = 60, align = "right")
    PortInputBox = Box(InputBox, width = 230, height = 30)

    KeyBlocker = Box(InputBox, width = 15, height = 30, align = "right")
    KeyInputBox = Box(InputBox, width = 215, height = 30)

    global UsernameInput, ColorInput, HostInput, PortInput, KeyInput
    UsernameInput = TextBox(UsernameInputBox, text = "Username", width = "fill")
    UsernameInput.text_size = 16
    UsernameInput.text_color = "lightblue"
    UsernameInput.bg = (40, 40, 40)

    ColorInput = TextBox(ColorInputBox, text = "Chat Color", width = "fill")
    ColorInput.text_size = 16
    ColorInput.text_color = "lightblue"
    ColorInput.bg = (40, 40, 40)
    
    
    HostInput = TextBox(HostInputBox, text = "Host IP", width = "fill")
    HostInput.text_size = 16
    HostInput.text_color = "lightblue"
    HostInput.bg = (40, 40, 40)
    
    PortInput = TextBox(PortInputBox, text = "Port", width = "fill")
    PortInput.text_size = 16
    PortInput.text_color = "lightblue"
    PortInput.bg = (40, 40, 40)

    KeyInput = TextBox(KeyInputBox, text = "Private Key", width = "fill")
    KeyInput.text_size = 16
    KeyInput.text_color = "lightblue"
    KeyInput.bg = (40, 40, 40)

    ConnectWindowOpened = True
    ConnectWindow.display()

OpenConnectWindow()
