##11/8/2022
##UI fixes, dark mode, etc
##V12 RC 2

import tkinter
import socket
import time
from threading import Thread
from guizero import *

s = socket.socket()

Host = '192.168.1.138'
Port = 0000

Username = "tomm"

ColorsList = ["red", "green", "yellow", "blue", "purple"]
ChatHistory = []

Connected = False

SettingsOpened = False
ConnectWindowOpened = False
ChatroomOpened = False

DarkMode = True
        
Location = " - "

def ChangeColor():
    global Color
    if (ColorInput.value).casefold() in ColorsList:
        Color = ColorInput.value
        History.text_color = Color
        History.append("[Device] Color Changing Successful.")
        
    else:
        History.append("[Device] Color Changing Unsuccessful. Try another Color.")

    Settings.hide()

def SwitchTheme():
    global DarkMode
    if ConnectWindowOpened == True:
        if DarkMode == True:
            Chatroom.bg = "white"
            Chatroom.text_color = "black"

##Add Buttons from Settings to prevent Darkmode changes

            SaveChat.text_color = "black"
            DarkmodeToggle.text_color = "black"
            ChangeColorButton.text_color = "black"

            DarkMode = False
            
        else:
            Chatroom.bg = None
            Chatroom.text_color = "white"

            DarkMode = True

##Add Buttons from ChatWindow to prevent Darkmode changes

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
    Message = "has disconnected"
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
    DetailsTitle = TextBox(Settings, text = "Details and File Save Location", width = "fill", align = "top")
    DetailsTitle.text_size = 20
    DetailsTitle.disable()

    global TopHeader
    TopHeader = Box(Settings, width = "fill", height = 50, align = "top")

    global BottomBox
    BottomBox = Box(Settings, width = "fill", height = "fill", align = "bottom")

    global MiddleBox
    MiddleBox = Box(Settings, width = "fill", height = 140, align = "bottom")

    global LeftBox
    LeftBox = Box(Settings, width = "fill", height = "fill", align = "left")

    global RightBox
    RightBox = Box(Settings, width = "fill", height = "fill", align = "right")

    global MiddleHeader
    MiddleHeader = Box(MiddleBox, width = "fill", height = 50)

    global SettingsTitle
    SettingsTitle = TextBox(MiddleBox, text = "Configurables", width = "fill")
    SettingsTitle.text_size = 20
    SettingsTitle.disable()

    global BottomHeader
    BottomHeader = Box(MiddleBox, width = "fill", height = 50)
    
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
    
    global SaveLocation
    SaveLocation = TextBox(RightBox, text = ("Save Chat History in: " + Location), width = "fill")
    SaveLocation.text_size = 16
    SaveLocation.disable()

    global ChangeLocation
    ChangeLocation = TextBox(RightBox, text = "Change Location", width = "fill")
    ChangeLocation.text_size = 16
    ChangeLocation.text_color = "white"
    
    global SaveChat
    SaveChat = PushButton(RightBox, text = "Save Chat History", command = SaveChatHistory)
    SaveChat.text_color = "black"

    global DarkmodeText
    DarkmodeText = TextBox(BottomBox, text = ("Dark Mode on: " + str(DarkMode)), width = "fill")
    DarkmodeText.text_size = 16
    DarkmodeText.disable()

    global DarkmodeToggle
    DarkmodeToggle = PushButton(BottomBox, text = "Switch Theme", command = SwitchTheme)
    DarkmodeToggle.text_color = "black"

    global ColorText, Color
    Color = Color[0].upper() + Color[1:].lower()
    ColorText = TextBox(BottomBox, text = ("Chat Color: " + Color), width = "fill")
    ColorText.text_size = 16
    ColorText.disable()

    global ColorInput
    ColorInput = TextBox(BottomBox, text = "Change Color", width = "fill")
    ColorInput.text_size = 16
    ColorInput.text_color = "white"

    global ChangeColorButton
    ChangeColorButton = PushButton(BottomBox, text = "Change Color", command = ChangeColor)
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
    History.text_color = Color
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

    ConnectWindow.display()

main()




       
