# 4/1/2023
# V13.3

import client

# Test inputs getter
# Simulate nothing showing up until the first enter key is presssed

def test_initialise_inputs():
    client.uiInstance.requestInput(True, None)

    assert all(item is None for item in client.connectionInstance.inputs) is True

def test_getting_username():
    # "Choose a username" is displayed, and "Username" is inputted
    client.uiInstance.requestInput(True, "Username")

    assert client.connectionInstance.inputs[0] == "Username"
    assert all(item is None for item in client.connectionInstance.inputs[1:6]) is True

def test_getting_color():
    client.uiInstance.requestInput(True, "invalidcolor")

    assert client.connectionInstance.inputs[1] is None

    client.uiInstance.requestInput(True, "red")

    assert client.connectionInstance.inputs[1] == (255, 0, 0)
    assert all(item is None for item in client.connectionInstance.inputs[2:6]) is True

def test_getting_host():
    client.uiInstance.requestInput(True, "127.0.0.1")

    assert client.connectionInstance.inputs[2] == "127.0.0.1"
    assert all(item is None for item in client.connectionInstance.inputs[3:6]) is True

def test_getting_port():
    client.uiInstance.requestInput(True, "12345")

    assert client.connectionInstance.inputs[3] == "12345"
    assert all(item is None for item in client.connectionInstance.inputs[4:6]) is True

def test_getting_publicKey():
    client.uiInstance.requestInput(True, "244177280043")

    assert client.connectionInstance.inputs[4] == "244177280043"
    assert all(item is None for item in client.connectionInstance.inputs[5:6]) is True

def test_getting_privateKey():
    client.uiInstance.requestInput(True, "257713280043")

    assert client.connectionInstance.inputs[5] == "257713280043"
    assert client.connectionInstance.inputs[4][6:12] == client.connectionInstance.inputs[5][6:12]
    assert all(item is None for item in client.connectionInstance.inputs[6:6]) is True

def test_getting_cipherKey():
    client.uiInstance.requestInput(True, "1144")

    assert client.connectionInstance.inputs[6] == "1144"
    assert all(item is not None for item in client.connectionInstance.inputs) is True

def test_arrow_keys_in_input():
    # Simulate an arrow key being pressed
    client.uiInstance.requestInput(False, None)

    assert all(item is not None for item in client.connectionInstance.inputs) is True

    client.uiInstance.requestInput(False, "random string")

    assert all(item is not None for item in client.connectionInstance.inputs) is True

def test_key_separation():
    # Simulate proper deciphering and indexing
    assert client.connectionInstance.e == 244177
    assert client.connectionInstance.d == 257713
    assert client.connectionInstance.N == 280043
    assert client.connectionInstance.cipherKey == 14








