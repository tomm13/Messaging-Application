import pytest
import client, server, socket

def test_setup():
    client.uiInstance.openSetup()
    client.uiInstance.requestInput(True)

def test_default_color():
    assert client.uiInstance.animationColor == (173, 216, 230)
    assert client.uiInstance.animationColor[0:2]

def test_inputs():
    client.connectionInstance.username = "tomm"
    client.connectionInstance.color = "lightblue"
    client.connectionInstance.host = socket.gethostbyname(socket.gethostname())
    client.connectionInstance.port = "49125"
    client.connectionInstance.publicKey = "817351935383"
    client.connectionInstance.privateKey = "138055935383"
    client.connectionInstance.encryptedCipherKey = "441945"

    client.connectionInstance.hasUsername = True
    client.connectionInstance.hasColor = True
    client.connectionInstance.hasHost = True
    client.connectionInstance.hasPort = True
    client.connectionInstance.hasPublicKey = True
    client.connectionInstance.hasPrivateKey = True
    client.connectionInstance.hasCipherKey = True

    assert len(client.connectionInstance.port) == 5
    assert len(client.connectionInstance.publicKey) == 12
    assert len(client.connectionInstance.privateKey) == 12
    assert client.connectionInstance.publicKey[6:12] == client.connectionInstance.privateKey[6:12]

def test_joining_failure():
    client.connectionInstance.connect()

    assert client.connectionInstance.connected == False
