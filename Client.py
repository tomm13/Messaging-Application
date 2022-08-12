##12/8/2022
##UI improvements to settings menu, global chat color, rgb with hsv, full inputs, optimised for windows (2)
##V12 RC 3

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

Connected = False

SettingsOpened = False
ConnectWindowOpened = False
ChatroomOpened = False

DarkMode = False
StopRainbowThread = False
        
Location = " - "

def Rainbow():
    R = 255
    G = 0
    B = 0
    Rate = 0.0025
    while True:
        if StopRainbowThread == False:
            while not G == 255 and StopRainbowThread == False:
                G += 1

                RGB = (R, G, B)

                History.text_color = RGB
                time.sleep(Rate)

            while not R == 0 and StopRainbowThread == False:
                R -= 1

                RGB = (R, G, B)

                History.text_color = RGB
                time.sleep(Rate)

            while not B == 255 and StopRainbowThread == False:
                B += 1

                RGB = (R, G, B)

                History.text_color = RGB
                time.sleep(Rate)
            while not G == 0 and StopRainbowThread == False:
                G -= 1

                RGB = (R, G, B)

                History.text_color = RGB
                time.sleep(Rate)

            while not R == 255 and StopRainbowThread == False:
                R += 1

                RGB = (R, G, B)

                History.text_color = RGB
                time.sleep(Rate)

            while not B == 0 and StopRainbowThread == False:
                B -= 1

                RGB = (R, G, B)

                History.text_color = RGB
                time.sleep(Rate)
        else:
            History.append("[Device] Rainbow deactivated")
            History.text_color = Color
            break

def ChangeColor():
    global Color
    global StopRainbowThread
    if (ColorInput.value).casefold() in ColorsList:
        if (ColorInput.value).casefold() == "rainbow":
            StopRainbowThread = False
            
            global RainbowThread
            RainbowThread = Thread(target = Rainbow)
            RainbowThread.start()
            
            global Color
            Color = "rainbow"
            History.append("[Device] Rainbow activated")
            
        else:
            StopRainbowThread = True
            Color = ColorInput.value
            History.text_color = Color
    else:
        History.append("[Device] Color Changing Unsuccessful. Try another Color.")

    Settings.hide()

def SwitchTheme():
    global DarkMode
    global Color
    if ConnectWindowOpened == True:
        if DarkMode == True:
            
##Turns dark mode off
            
            Chatroom.bg = "white"
            Chatroom.text_color = "black"

##Add elements from Settings to prevent Darkmode changes

            SaveChat.text_color = "black"
            DarkmodeToggle.text_color = "black"
            ChangeColorButton.text_color = "black"

            DarkMode = False
            
        else:
            
##Turns dark mode on
            
            Chatroom.bg = (40, 40, 40)
            Chatroom.text_color = "white"

            DarkMode = True

##Add elements from ChatWindow to prevent Darkmode changes
            
        if not Color.casefold() == "rainbow":
            History.text_color = Color

        SendButton.bg = "white"
        LeaveChat.bg = "white"
        SettingsButton.bg = "white"
            
        SendButton.text_color = "black"
        LeaveChat.text_color = "black"
        SettingsButton.text_color = "black"

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

def SendToServer():
    Message = MessageInput.value
    if Message:
        if Message == "/leave":
            Leave()
        else:
            s.send(Message.encode())
            MessageInput.clear()

def AlwaysUpdate():
    while True:
        Message = s.recv(1024).decode()
        History.append(Message)
        ChatHistory.append(Message)

def Connect():
    global Connected
    global Username
    global Color
    global Host, Port
##    Username = str(UsernameInput.value)
##    Host = HostInput.value
    Color = (ColorInput.value).casefold()

    if Color in ColorsList:
        if not Username == "" or Username == "Username":
            try:        
                Port = int(PortInput.value, base=10)               
              
                s.connect((Host, Port))
                s.send(Username.encode())

                Connected = True

                Status.value = "Connection Success"
                Status.text_color = "green"

                Chat()
            
            except ConnectionRefusedError:
                Connected = False

                Status.value = "Connection Full"
                Status.text_color = "yellow"
                
            except OSError:
                Connected = False
                
                Status.value = "Restart Client"
                Status.text_color = "red"

            except BrokenPipeError:
                Connected = False

                Chatroom.hide()

                Status.value = "Broken Pipe"
                Status.text_color = "red"
        else:
            Status.value = "Invalid Username"
            Status.text_color = "yellow"
    else:
        Status.value = "Invalid Color"
        Status.text_color = "yellow"
                   
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

    Connected = False
    
    print("Closing Client...")
    quit()
    
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
    DarkmodeBox = Box(BottomBox, width = "fill", height = 50, align = "top")

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

    global ColorInput
    ColorInput = TextBox(ColorBox, text = "Change Color", width = "fill", align = "left")
    ColorInput.text_size = 16
    ColorInput.text_color = "white"

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

##default light mode
    SaveChat.text_color = "black"
    DarkmodeToggle.text_color = "black"
    ChangeColorButton.text_color = "black"

    Settings.show()

def Chat():
    global Chatroom, ChatroomOpened
    Chatroom = Window(ConnectWindow, height = 700, width = 600, title = "Chatroom")
    Chatroom.font = "San Francisco Bold"
    ChatroomOpened = True

    global Header
    Header = Box(Chatroom, width = "fill", height = 40, align = "top")

    global UsernameDisplayHeader
    UsernameDisplayHeader = Text(Header, text = (Username), align = "left")
    UsernameDisplayHeader.text_color = "white"
    UsernameDisplayHeader.text_size = 26
    
    global History
    History = TextBox(Chatroom, text = "[Device] Welcome to this chat room", height = "fill", width = "fill", multiline = True, scrollbar = True, align = "top")
    History.text_size = 16
    History.disable()

    global ButtonBox
    ButtonBox = Box(Chatroom, width = "fill", align = "bottom")

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
    
##doesnt make this light mode 10/10
    Chatroom.bg = "white"
    Chatroom.text_color = "black"

    if (ColorInput.value).casefold() == "rainbow":
        global RainbowThread
        RainbowThread = Thread(target = Rainbow)
        RainbowThread.start()
    else:
        History.text_color = Color
    
    Chatroom.show()

    global ListeningThread
    ListeningThread = Thread(target = AlwaysUpdate)
    ListeningThread.start()
   
def main():    
    global ConnectWindow, ConnectWindowOpened
    ConnectWindow = App(title = "Connect To Server", height = 230, width = 500)
    ConnectWindow.font = "San Francisco Bold"
    ConnectWindowOpened = True
    
    global InputBox
    InputBox = Box(ConnectWindow, width = "fill", align = "left")

    global VerifyBox
    VerifyBox = Box(ConnectWindow, width = "fill", align = "right")

    global Status
    Status = Text(VerifyBox, text = "Not Connected")
    Status.text_size = 28
    Status.text_color = "white"

    global AttemptConnect
    AttemptConnect = PushButton(VerifyBox, text = "Connect", command = Connect)

    global UsernameInput, ColorInput, HostInput, PortInput
    UsernameInput = TextBox(InputBox, text = "Username", width = "fill")
    UsernameInput.text_size = 16

    ColorInput = TextBox(InputBox, text = "Chat Color", width = "fill")
    ColorInput.text_size = 16
    
    HostInput = TextBox(InputBox, text = "Host IP", width = "fill")
    HostInput.text_size = 16
    
    PortInput = TextBox(InputBox, text = "Port", width = "fill")
    PortInput.text_size = 16

    HostInput.disable()
    UsernameInput.disable()
##    ColorInput.disable()

    ConnectWindow.display()

main()




       
