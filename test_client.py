# 11/1/2023
# V13.3

import client

# Test inputs getter
# Simulate nothing showing up until the first enter key is presssed


def test_initialise_inputs():
    client.uiInstance.requestInput(True, None)

    assert all(item is None for item in client.connectionInstance.inputs) is True
    assert client.connectionInstance.inputRequest == 0


def test_getting_username():
    # "Choose a username" is displayed, and "Username" is inputted
    client.uiInstance.requestInput(True, "Username")

    assert client.connectionInstance.inputs[0] == "Username"
    assert client.connectionInstance.inputRequest == 1
    assert all(item is None for item in client.connectionInstance.inputs[1:6]) is True


def test_getting_color():
    # Invalid strings, white and red are all rejected
    for color in ["invalidcolor", "white", "red"]:
        client.uiInstance.requestInput(True, color)

        assert client.connectionInstance.inputs[1] is None
        assert client.connectionInstance.inputRequest == 1

    client.uiInstance.requestInput(True, "blue")

    assert client.connectionInstance.inputs[1] == (0, 0, 255)
    assert client.connectionInstance.inputRequest == 2
    assert all(item is None for item in client.connectionInstance.inputs[2:6]) is True


def test_getting_host():
    client.uiInstance.requestInput(True, "127.0.0.1")

    assert client.connectionInstance.inputs[2] == "127.0.0.1"
    assert client.connectionInstance.inputRequest == 3
    assert all(item is None for item in client.connectionInstance.inputs[3:6]) is True


def test_getting_port():
    client.uiInstance.requestInput(True, "12345")

    assert client.connectionInstance.inputs[3] == "12345"
    assert client.connectionInstance.inputRequest == 4
    assert all(item is None for item in client.connectionInstance.inputs[4:6]) is True


def test_getting_publicKey():
    client.uiInstance.requestInput(True, "244177280043")

    assert client.connectionInstance.inputs[4] == "244177280043"
    assert client.connectionInstance.inputRequest == 5
    assert all(item is None for item in client.connectionInstance.inputs[5:6]) is True


def test_getting_privateKey():
    client.uiInstance.requestInput(True, "257713280043")

    assert client.connectionInstance.inputs[5] == "257713280043"
    assert client.connectionInstance.inputs[4][6:12] == client.connectionInstance.inputs[5][6:12]
    assert client.connectionInstance.inputRequest == 6
    assert all(item is None for item in client.connectionInstance.inputs[6:6]) is True


def test_getting_cipherKey():
    client.uiInstance.requestInput(True, "1144")

    assert client.connectionInstance.inputs[6] == "1144"
    assert client.connectionInstance.inputRequest == 0
    assert all(item is not None for item in client.connectionInstance.inputs) is True


def test_arrow_keys_in_input():
    # Simulate an arrow key being pressed
    for value in [None, "random string"]:
        client.uiInstance.requestInput(False, value)

        assert client.connectionInstance.inputRequest == 0
        assert all(item is not None for item in client.connectionInstance.inputs) is True

# Test proper indexing and separation of keys


def test_key_separation():
    assert client.connectionInstance.e == 244177
    assert client.connectionInstance.d == 257713
    assert client.connectionInstance.N == 280043
    assert client.connectionInstance.cipherKey == 14

# Test algorithmic accuracy


def test_key_retrieval():
    for key in range(1, 26):
        assert key == client.communicationInstance.rsaDecrypt(client.communicationInstance.rsaEncrypt(key, 244177, 280043), 257713, 280043)


def test_string_retrieval():
    message = "my name is tomm 12345"
    for key in range(1, 26):
        assert message == client.communicationInstance.caesarDecrypt(client.communicationInstance.caesarEncrypt(message, key), key)

