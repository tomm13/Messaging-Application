# 25/1/2023
# V13.3

import client
from time import localtime, strftime


def test_initialise_inputs():
    # Simulate nothing showing up until the first enter key is presssed
    client.uiInstance.requestInput(True, None)

    assert all(item is None for item in client.connectionInstance.inputs) is True
    assert client.connectionInstance.inputRequest == 0


def test_getting_username():
    # "Choose a username" is displayed, and an invalid username is inputted
    client.uiInstance.requestInput(True, None)

    assert client.connectionInstance.inputs[0] is None
    assert client.connectionInstance.inputRequest == 0
    assert all(item is None for item in client.connectionInstance.inputs) is True

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

    # Valid color test

    client.uiInstance.requestInput(True, "blue")

    assert client.connectionInstance.inputs[1] == (0, 0, 255)
    assert client.connectionInstance.inputRequest == 2
    assert all(item is None for item in client.connectionInstance.inputs[2:6]) is True


def test_getting_host():
    # Invalid host test
    client.uiInstance.requestInput(True, None)

    assert client.connectionInstance.inputs[2] is None
    assert client.connectionInstance.inputRequest == 2
    assert all(item is None for item in client.connectionInstance.inputs[2:6]) is True

    # Valid host test
    client.uiInstance.requestInput(True, "127.0.0.1")

    assert client.connectionInstance.inputs[2] == "127.0.0.1"
    assert client.connectionInstance.inputRequest == 3
    assert all(item is None for item in client.connectionInstance.inputs[3:6]) is True


def test_getting_port():
    # Invalid port test
    client.uiInstance.requestInput(True, None)

    assert client.connectionInstance.inputs[3] is None
    assert client.connectionInstance.inputRequest == 3
    assert all(item is None for item in client.connectionInstance.inputs[3:6]) is True

    # Valid port test
    client.uiInstance.requestInput(True, "12345")

    assert client.connectionInstance.inputs[3] == "12345"
    assert client.connectionInstance.inputRequest == 4
    assert all(item is None for item in client.connectionInstance.inputs[4:6]) is True


def test_getting_publicKey():
    # Invalid publicKey test
    client.uiInstance.requestInput(True, None)

    assert client.connectionInstance.inputs[4] is None
    assert client.connectionInstance.inputRequest == 4
    assert all(item is None for item in client.connectionInstance.inputs[4:6]) is True

    # Valid publicKey test
    client.uiInstance.requestInput(True, "244177280043")

    assert client.connectionInstance.inputs[4] == "244177280043"
    assert client.connectionInstance.inputRequest == 5
    assert all(item is None for item in client.connectionInstance.inputs[5:6]) is True


def test_getting_privateKey():
    # Invalid privateKey test
    client.uiInstance.requestInput(True, None)

    assert client.connectionInstance.inputs[5] is None
    assert client.connectionInstance.inputRequest == 5
    assert all(item is None for item in client.connectionInstance.inputs[5:6]) is True

    # Valid privateKey test
    client.uiInstance.requestInput(True, "257713280043")

    assert client.connectionInstance.inputs[5] == "257713280043"
    assert client.connectionInstance.inputs[4][6:12] == client.connectionInstance.inputs[5][6:12]
    assert client.connectionInstance.inputRequest == 6
    assert all(item is None for item in client.connectionInstance.inputs[6:6]) is True


def test_getting_cipherKey():
    # Invalid cipherKey test
    client.uiInstance.requestInput(True, None)

    assert client.connectionInstance.inputs[6] is None
    assert client.connectionInstance.inputRequest == 6
    assert all(item is None for item in client.connectionInstance.inputs[6:6]) is True

    # Valid cipherKey test
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


def test_key_separation():
    # Test proper indexing and separation of keys
    assert client.connectionInstance.e == 244177
    assert client.connectionInstance.d == 257713
    assert client.connectionInstance.N == 280043
    assert client.connectionInstance.cipherKey == 14


def test_key_retrieval():
    for key in range(1, 26):
        assert key == client.communicationInstance.rsaDecrypt(client.communicationInstance.rsaEncrypt(key, 244177, 280043), 257713, 280043)


def test_string_retrieval():
    message = "my name is tomm 12345"
    for key in range(1, 26):
        assert message == client.communicationInstance.caesarDecrypt(client.communicationInstance.caesarEncrypt(message, key), key)

    message = "😁😛😋🤣"
    for key in range(1, 26):
        assert message == client.communicationInstance.caesarDecrypt(client.communicationInstance.caesarEncrypt(message, key), key)


def test_reset_inputs():
    # Should probably run last
    # Test that when a user provides an invalid inputs, every input so far is reset
    # First test that every item has value
    assert all(item is not None for item in client.connectionInstance.inputs) is True

    # Reset every value
    client.connectionInstance.resetInputs(None)

    assert all(item is None for item in client.connectionInstance.inputs) is True


def test_chat_history_retrieval():
    # Create a list of messages and see if it matches

    for message in ["my name is tomm 12345", "😁😛😋🤣"]:
        client.communicationInstance.addMessage(message)
        client.communicationInstance.saveChatHistoryToFile("test.txt")

        with open("test.txt", "r") as file:
            line = file.readline()

        assert line == strftime("%H:%M:%S", localtime()) + " {message}\n"


def test_message_and_page_handling():
    # Test that pages are styled properly
    # First reset the chathistory

    client.communicationInstance.chatHistory = []
    client.uiInstance.linesSent = 0

    pass

    #client.communicationInstance.addMessage()

