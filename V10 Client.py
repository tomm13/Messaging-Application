##9/8/2022
##Chat history does not duplicate last sent text
##V11 Client

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
##                Port = int(PortInput.value, base=10)
                HostInput.disable()
                PortInput.disable()

                Host = '192.168.1.138'
                Port = 1234
                
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

    HistoryButton = PushButton(Chatroom, text = "Save Chat History", command = SaveChatHistory, align = "bottom")
    
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

    global PortInput, HostInput
    PortInput = TextBox(ConnectWindow, text = "Port", align = "bottom")
    HostInput = TextBox(ConnectWindow, text = "Host IP", align = "bottom")

    global UsernameInput
    UsernameInput = TextBox(ConnectWindow, text = "Username", align = "bottom")

    AttemptConnect = PushButton(ConnectWindow, text = "Connect", command = Connect, align = "bottom")
    
    ConnectWindow.display()

main()




        

