##8/8/2022
##attempts at always updating chat history in threads
##v8

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

Connected = False

def SendToServer():
    Message = MessageInput.value
    if Message:
        Message = Username + ": " + Message
        s.send(Message.encode())
        
        MessageInput.clear()

def Update():
    try:
        Message = s.recv(1024).decode()
        History.append(Message)

    except:
        History.append("[Update failed / No message found]")

def AlwaysUpdate():
    while True:
        Update()

def Connect():
    try:
        global Username

        #Username = "tomm"
        Username = str(UsernameInput.value)

        if Username == "" or Username == "Username":
            Status.value = "Invalid Username"
            Status.text_color = "yellow"

        else:
            #Host = HostInput.value
            #Port = int(PortInput.value, base=10)

            Host = '192.168.1.138'
            Port = 5050
            
            s.connect((Host, Port))

            Status.value = "Connected"
            Status.text_color = "green"

            Connected = True

            Chat()
            
    except ConnectionRefusedError:

        Connected = False

        Status.value = "Connection Full"
        Status.text_color = "yellow"

    except Exception as e:

        print(str(e))
        
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

    UpdateButton = PushButton(Chatroom, text = "Update", command = Update, align = "bottom")
    #UpdateButton.disable()
    
    Chatroom.show()

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
    PortInput = TextBox(ConnectWindow, text = "Port (only be changed in code)", align = "bottom")
    HostInput = TextBox(ConnectWindow, text = "Host IP (only be changed in code)", align = "bottom")

    global UsernameInput
    UsernameInput = TextBox(ConnectWindow, text = "Username", align = "bottom")

    AttemptConnect = PushButton(ConnectWindow, text = "Connect", command = Connect, align = "bottom")
    
    ConnectWindow.display()

main()



        

