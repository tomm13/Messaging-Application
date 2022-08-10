##10/8/2022
##Adding directory for chat history
##V12 RC

import socket
import time
from threading import Thread
from guizero import *
import sys

s = socket.socket()

Host = '192.168.1.138'
Port = 0000

Username = "tomm"

ChatHistory = []

Connected = False

Location = "[Undefined]"
    
def SaveChatHistory():
    global Location
    Location = ChangeLocation.value

    if Location and not Location == "Change Location":
        File = open(Location, "w")
        for Chat in ChatHistory:
            File.write(Chat)
            File.write("\n")
        File.close()
        
        Message = "has saved the chat"
        s.send(Message.encode())

        History.append(("[Device] Saving Successful. The Chat History has been saved in: " + Location))
        
    else:
        Location = "[Undefined]"
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
    global Host, Port
##    Username = str(UsernameInput.value)

    if Username == "" or Username == "Username":
        Status.value = "Invalid Username"
        Status.text_color = "yellow"

    else:
        try:
##            Host = HostInput.value
            
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
                       
def Leave():
    global Conencted
    Message = Username + " has disconnected"
    s.send(Message.encode())

    Settings.hide()
    Chatroom.hide()
    ConnectWindow.hide()
    
    s.close()
    sys.exit()

    Connected = False

    exit()
    
def OpenSettings():
    global Settings
    Settings = Window(Chatroom, height = 230, width = 500, title = "Settings")

    global HostDisplay
    HostDisplay = Text(Settings, text = ("Host IP: " + str(Host)))
    HostDisplay.text_color = "white"
    
    global PortDisplay
    PortDisplay = Text(Settings, text = ("Port: " + str(Port)))
    PortDisplay.text_color = "white"

    global SaveLocation
    SaveLocation = Text(Settings, text = ("Saving in: " + Location))
    SaveLocation.text_color = "white"

    global ChangeLocation
    ChangeLocation = TextBox(Settings, text = "Change Location", width = 150)
    ChangeLocation.text_color = "white"
    
    global SaveChat
    SaveChat = PushButton(Settings, text = "Save Chat History", command = SaveChatHistory)

    global LeaveChat
    LeaveChat = PushButton(Settings, text = "Leave Chat", command = Leave)

    Settings.show()

def Chat():
    global Chatroom
    Chatroom = Window(ConnectWindow, height = 700, width = 600, title = "Chatroom")
    Chatroom.font = "San Francisco Bold"
    
    global History
    History = TextBox(Chatroom, text = "Welcome to this chat room", height = "fill", width = "fill", multiline = True, scrollbar = True, align = "top")
    History.text_size = 16

    global ButtonBox
    ButtonBox = Box(Chatroom, width = "fill", align = "bottom")

    global SendButton
    SendButton = PushButton(ButtonBox, text = "Send", command = SendToServer, align = "right")

    global SettingsButton
    SettingsButton = PushButton(ButtonBox, text = "Settings", command = OpenSettings, align = "left")

    global MessageInput
    MessageInput = TextBox(ButtonBox, height = "fill", width = "fill")
    
    Chatroom.show()

    ListeningThread = Thread(target = AlwaysUpdate)
    ListeningThread.start()
   
def main():    
    global ConnectWindow
    ConnectWindow = App(title = "Connect to server", height = 230, width = 500)
    ConnectWindow.font = "San Francisco Bold"
    
    global InputBox
    InputBox = Box(ConnectWindow, width = "fill", align = "left")

    global VerifyBox
    VerifyBox = Box(ConnectWindow, width = "fill", align = "right")

    global Status
    Status = Text(VerifyBox, text = "Not Connected")
    Status.text_size = 28
    Status.text_color = "white"

    global AttemptConenct
    AttemptConnect = PushButton(VerifyBox, text = "Connect", command = Connect)

    global UsernameInput, HostInput, PortInput
    UsernameInput = TextBox(InputBox, text = "Username", width = "fill")
    UsernameInput.text_size = 16
    
    HostInput = TextBox(InputBox, text = "Host IP", width = "fill")
    HostInput.text_size = 16
    
    PortInput = TextBox(InputBox, text = "Port", width = "fill")
    PortInput.text_size = 16
    
    HostInput.disable()
    UsernameInput.disable()

    ConnectWindow.display()

main()




       
