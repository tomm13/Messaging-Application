balls

def Broadcast(Message):
    print("[Client]", Message)
    for Client in Clients:
        Client.send(Message.encode())

def Listen(ClientSocket):
    while True:
        Message = ClientSocket.recv(1024).decode()
        if Message:
            Broadcast(Message)

for i in range(UserCount):
    global ClientSocket
    ClientSocket, Address = s.accept()
    Clients.append(ClientSocket)
    Broadcast("New connection made")

    UserOnline += 1
    print("[Server] " + str(UserOnline) +
          " of " + str(UserCount) +
          " space(s) are taken")

    ListeningThread = Thread(target = Listen, args = [ClientSocket])
    ListeningThread.start()





