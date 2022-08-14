##14/8/2022
##RSA Fully working, Improved Rainbow loops
##V12 RC 7

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

ColorsList = ["red", "green", "yellow", "blue", "purple", "coral", "black", "white", "pimk", "brown", "grey", "rainbow"]
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
            History.append("[Device] Rainbow deactivated")
            History.text_color = Color
                
            break

def SwitchTheme():
    global DarkMode
    global Color
    if ConnectWindowOpened == True:
        if DarkMode == True:      
            Chatroom.bg = "white"
            Chatroom.text_color = "black"

            SaveChat.text_color = "black"
            DarkmodeToggle.text_color = "black"
            ChangeColorButton.text_color = "black"

            DarkMode = False

        else:
            Chatroom.bg = (40, 40, 40)
            Chatroom.text_color = "white"

            DarkMode = True
            
        if not Color.casefold() == "rainbow":
            History.text_color = Color

        SendButton.bg = "white"
        LeaveChat.bg = "white"
        SettingsButton.bg = "white"
            
        SendButton.text_color = "black"
        LeaveChat.text_color = "black"
        SettingsButton.text_color = "black"

        Settings.hide()

def ChangeColor():
    global Color
    global StopRainbow
    if (SettingsColorInput.value).casefold() in ColorsList:
        if (SettingsColorInput.value).casefold() == "rainbow":
            StopRainbow = False
            
            RainbowHistoryThread = Thread(target = Rainbow, args = (History,))
            RainbowHistoryThread.start()
                       
            Color = "rainbow"
            History.append("[Device] Rainbow activated")            
        else:
            StopRainbow = True
            
            Color = SettingsColorInput.value
            History.text_color = Color
            History.append("[Device] Color Changing Successful.")
    else:
        History.append("[Device] Color Changing Unsuccessful. Try another Color.")

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
    
        History.append(("[Device] Saving Successful. The Chat History has been saved in: " + Location))
        Message = "has saved the chat"
        s.send(Message.encode())
        
    else:
        Location = " - "
        History.append("[Device] Saving Unsuccessful. The Chat History has not been saved due to an invalid file location")
        
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
        Message = s.recv(1024).decode()
        Message = RSADecrypt(Message)
        
        History.append(Message)
        ChatHistory.append(Message)

def SendToServer():
    Message = MessageInput.value
    if Message:
        if Message == "/leave":
            Leave()
        else:
            s.send(Message.encode())
            MessageInput.clear()

def Leave():
    global Conencted
    Message = "/leave"
    s.send(Message.encode())

    if SettingsOpened == True:
        Settings.hide()

    if ConnectWindowOpened == True:
        ConnectWindow.hide()
        
    if ChatroomOpened == True:
        Chatroom.hide()    
        ListeningThread.join()

    s.close()
    
    print("Closing Client...")
    quit()

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
                if not Username == "" or Username == "Username":
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
    
def OpenSettings():
    global Settings, SettingsOpened
    Settings = Window(Chatroom, height = 690, width = 500, title = "Settings")
    SettingsOpened = True

    global DetailsTitle
    DetailsTitle = TextBox(Settings, text = "Details:", width = "fill", align = "top")
    DetailsTitle.text_size = 20
    DetailsTitle.disable()

    global TopHeader
    TopHeader = Box(Settings, width = "fill", height = 30, align = "top")

    global BottomBox
    BottomBox = Box(Settings, width = "fill", height = "fill", align = "bottom")

    global MiddleBox
    MiddleBox = Box(Settings, width = "fill", height = 100, align = "bottom")

    global LeftBox
    LeftBox = Box(Settings, width = "fill", height = "fill", align = "left")

    global RightBox
    RightBox = Box(Settings, width = "fill", height = "fill", align = "right")

    global MiddleHeader
    MiddleHeader = Box(MiddleBox, width = "fill", height = 30)

    global SettingsTitle
    SettingsTitle = TextBox(MiddleBox, text = "Configurables:", width = "fill")
    SettingsTitle.text_size = 20
    SettingsTitle.disable()
    
    global UsernameDisplay
    UsernameDisplay = TextBox(LeftBox, text = ("Username: " + Username), width = "fill")
    UsernameDisplay.text_size = 16
    UsernameDisplay.disable()

    global HostDisplay
    HostDisplay = TextBox(LeftBox, text = ("Host IP: " + str(Host)), width = "fill")
    HostDisplay.text_size = 16
    HostDisplay.disable()
    
    global PortDisplay
    PortDisplay = TextBox(LeftBox, text = ("Port: " + str(Port)), width = "fill")
    PortDisplay.text_size = 16
    PortDisplay.disable()

    global DarkmodeBox
    DarkmodeBox = Box(BottomBox, width = "fill", height = 70, align = "top")

    global DarkmodeText
    DarkmodeText = TextBox(DarkmodeBox, text = ("Dark Mode on: " + str(DarkMode)), width = "fill", align = "left")
    DarkmodeText.text_size = 16
    DarkmodeText.disable()

    global DarkmodeToggle
    DarkmodeToggle = PushButton(DarkmodeBox, text = "Switch Theme", command = SwitchTheme, width = "fill", align = "right")
    DarkmodeToggle.text_color = "black"

    global ColorBox
    ColorBox = Box(BottomBox, width = "fill", height = 100, align = "top")

    global ColorText, Color
    Color = Color[0].upper() + Color[1:].lower()
    ColorText = TextBox(ColorBox, text = ("Chat Color: " + Color), width = "fill")
    ColorText.text_size = 16
    ColorText.disable()

    global SettingsColorInput
    SettingsColorInput = TextBox(ColorBox, text = "Change Color", width = "fill", align = "left")
    SettingsColorInput.text_size = 16
    SettingsColorInput.text_color = "white"

    global ChangeColorButton
    ChangeColorButton = PushButton(ColorBox, text = "Change Color", command = ChangeColor, width = "fill", align = "right")
    ChangeColorButton.text_color = "black"

    global SavingBox
    SavingBox = Box(BottomBox, width = "fill", height = 100, align = "top")

    global SaveLocation
    SaveLocation = TextBox(SavingBox, text = ("Save Chat History in: " + Location), width = "fill")
    SaveLocation.text_size = 16
    SaveLocation.disable()

    global ChangeLocation
    ChangeLocation = TextBox(SavingBox, text = "Change Location", width = "fill", align = "left")
    ChangeLocation.text_size = 16
    ChangeLocation.text_color = "white"

    global SaveChat
    SaveChat = PushButton(SavingBox, text = "Save Chat History", command = SaveChatHistory, width = "fill", align = "right")
    SaveChat.text_color = "black"

    global KeyBox
    KeyBox = Box(BottomBox, width = "fill", height = 100, align = "top")

    global KeyDetails
    KeyDetails = TextBox(KeyBox, text = "Private Key Details:", width = "fill")
    KeyDetails.text_size = 16
    KeyDetails.text_color = "white"
    KeyDetails.disable()

    global SettingsKeyDisplay
    SettingsKeyDisplay = TextBox(KeyBox, text = PrivateKey, hide_text = True, width = "fill", align = "left")
    SettingsKeyDisplay.text_size = 16
    SettingsKeyDisplay.text_color = "white"    

    global ShowKey
    ShowKey = PushButton(KeyBox, text = "Show Private Key", command = ShowPrivateKey, width = "fill", align = "right")
    ShowKey.text_color = "black"

    SaveChat.text_color = "black"
    DarkmodeToggle.text_color = "black"
    ChangeColorButton.text_color = "black"

    Settings.show()

def OpenChat():
    global Chatroom, ChatroomOpened
    Chatroom = Window(ConnectWindow, height = 720, width = 1080, title = "Chatroom")
    Chatroom.font = "San Francisco Bold"
    Chatroom.bg = "white"
    Chatroom.text_color = "black"
    ChatroomOpened = True

    global Header
    Header = Box(Chatroom, width = "fill", height = 40, align = "top")

    global ButtonBox
    ButtonBox = Box(Chatroom, width = "fill", align = "bottom")

    global UserBox
    UserBox = Box(Chatroom, width = 200, height = "fill", align = "left")

    global UsernameDisplayHeader
    UsernameDisplayHeader = Text(Header, text = (Username), align = "left")
    UsernameDisplayHeader.text_size = 40
    
    global History
    History = TextBox(Chatroom, text = "[Device] Welcome to this chat room", height = "fill", width = "fill", multiline = True, scrollbar = True, align = "top")
    History.text_size = 24
    History.disable()

    global SendButton
    SendButton = PushButton(ButtonBox, text = "Send", command = SendToServer, align = "right")
    SendButton.text_color = "black"

    global LeaveChat
    LeaveChat = PushButton(ButtonBox, text = "Leave", command = Leave, align = "left")
    LeaveChat.text_color = "black"
        
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
    else:
        History.text_color = Color

    Chatroom.show()
   
def OpenConnectWindow():    
    global ConnectWindow, ConnectWindowOpened
    ConnectWindow = App(title = "Connect To Server", height = 250, width = 550)
    ConnectWindow.font = "San Francisco Bold"
    ConnectWindowOpened = True
    
    global InputBox
    InputBox = Box(ConnectWindow, width = "fill", align = "left")

    global VerifyBox
    VerifyBox = Box(ConnectWindow, width = "fill", align = "right")

    global Status
    Status = Text(VerifyBox, text = "Not Connected")
    Status.text_size = 30
    Status.text_color = "white"

    global AttemptConnect
    AttemptConnect = PushButton(VerifyBox, text = "Connect", command = Connect)

    global UsernameInput, ColorInput, HostInput, PortInput, KeyInput
    UsernameInput = TextBox(InputBox, text = "Username", width = "fill")
    UsernameInput.text_size = 16

    ColorInput = TextBox(InputBox, text = "Chat Color", width = "fill")
    ColorInput.text_size = 16
    
    HostInput = TextBox(InputBox, text = "Host IP", width = "fill")
    HostInput.text_size = 16
    
    PortInput = TextBox(InputBox, text = "Port", width = "fill")
    PortInput.text_size = 16

    KeyInput = TextBox(InputBox, text = "Private Key", width = "fill")
    KeyInput.text_size = 16

    ConnectWindow.display()

OpenConnectWindow()
