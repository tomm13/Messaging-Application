##9/8/2022
##Chat history does not work for any follwing clients connected than the first 1
##V12 Client Beta

import socket
import time
from threading import Thread
from guizero import *

global s
s = socket.socket()

global Host
Host = 0

global Port
Port = 0

global ChatHistory
ChatHistory = []

Connected = False

def SaveChatHistory():
    File = open("ChatHistory.txt", "w")
    for Chat in ChatHistory:
        File.write(Chat)
        File.write("\n")
    File.close()
            
    Message = Username + " has saved the chat"
    s.send(Message.encode())

def SendToServer():
    Message = MessageInput.value
    if Message:
        Message = Username + ": " + Message
        s.send(Message.encode())
        
        MessageInput.clear()

def AlwaysUpdate():
    while True:
        Message = s.recv(1024).decode()
        History.append(Message)
        ChatHistory.append(Message)

def Connect():
    global Connected
    global Host
    global Port
    try:
        global Username

        Username = "tomm"
##        Username = str(UsernameInput.value)

        if Username == "" or Username == "Username":
            Status.value = "Invalid Username"
            Status.text_color = "yellow"

        else:
            try:
##                Host = HostInput.value
                Host = '192.168.1.138'
                
                Port = int(PortInput.value, base=10)               
##                Port = 1234
                
                s.connect((Host, Port))

                Connected = True

                s.send(Username.encode())

                Chat()
            
            except ConnectionRefusedError:
                Connected = False

                Status.value = "Connection Full"
                Status.text_color = "yellow"

    except:        
        Connected = False

        Status.value = "Connection Failed"
        Status.text_color = "red"

def Leave():
    Message = Username + " has disconnected"
    s.send(Message.encode())

    Settings.hide()
    Chatroom.hide()
    ConnectWindow.hide()
    
    s.close()
def OpenSettings():
    global Settings
    Settings = Window(Chatroom, height = 300, width = 300, title = "Settings")
    Settings.show()

    global HostDisplay
    HostDisplay = Text(Settings, text = str(Host))
    HostDisplay.text_color = "white"
    
    global PortDisplay
    PortDisplay = Text(Settings, text = str(Port))
    PortDisplay.text_color = "white"

    global SaveChat
    SaveChat = PushButton(Settings, text = "Save Chat History", command = SaveChatHistory)

    global LeaveChat
    LeaveChat = PushButton(Settings, text = "Leave Chat", command = Leave)

def Chat():
    global Chatroom
    Chatroom = Window(ConnectWindow, height = 700, width = 600, title = "Chatroom")
    Chatroom.font = "San Francisco Bold"
    
    global History
    History = TextBox(Chatroom, text = "Welcome to this chat room", height = "fill", width = 200, multiline = True, scrollbar = True, align = "top")
    
    History.text_size = 16

    global MessageInput
    MessageInput = TextBox(Chatroom, align = "bottom")
    
    SendButton = PushButton(Chatroom, text = "Send", command = SendToServer, align = "bottom")

    SettingsButton = PushButton(Chatroom, text = "Settings", command = OpenSettings, align = "bottom")
    
    Chatroom.show()

    ConnectWindow.hide()

    ListeningThread = Thread(target = AlwaysUpdate)
    ListeningThread.start()
   
def main():
    global ConnectWindow
    ConnectWindow = App(title = "Connect to server", height = 150, width = 250)
    ConnectWindow.font = "San Francisco Bold"

    global Status
    Status = Text(ConnectWindow, text = "Not Connected", align = "top")
    Status.text_size = 18
    Status.text_color = "red"

    global PortInput, HostInput, UsernameInput
    PortInput = TextBox(ConnectWindow, text = "Port", align = "bottom")
    HostInput = TextBox(ConnectWindow, text = "Host IP", align = "bottom")
    UsernameInput = TextBox(ConnectWindow, text = "Username", align = "bottom")

    HostInput.disable()
    UsernameInput.disable()

    AttemptConnect = PushButton(ConnectWindow, text = "Connect", command = Connect, align = "bottom")
    
    ConnectWindow.display()

main()




       
