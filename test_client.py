# 16/3/2023
# V13.3

import client
from time import localtime, strftime


def test_instantiation():
    # Instantiate objects from client
    client.connectionInstance = client.Connection()
    client.animationInstance = client.Animation()
    client.communicationInstance = client.Communication()
    client.uiInstance = client.UI()


def test_initialise_inputs():
    # Simulate nothing showing up until the first enter key is presssed
    client.uiInstance.setInputGetter(True, None)

    assert all(item is None for item in client.connectionInstance.inputs) is True
    assert client.connectionInstance.inputRequest == 0


def test_getting_username():
    # Invalid username test
    for input in [None, "", 0]:
        client.uiInstance.setInputGetter(True, input)

        assert client.connectionInstance.inputs[0] is None
        assert client.connectionInstance.inputRequest == 0
        assert all(item is None for item in client.connectionInstance.inputs) is True

    # Valid username test
    client.uiInstance.setInputGetter(True, "Username")

    assert client.connectionInstance.inputs[0] == "Username"
    assert client.connectionInstance.inputRequest == 1
    assert all(item is None for item in client.connectionInstance.inputs[1:6]) is True


def test_getting_color():
    # Invalid strings, white and red are all rejected
    for color in ["invalidcolor", "white", "red"]:
        client.uiInstance.setInputGetter(True, color)

        assert client.connectionInstance.inputs[1] is None
        assert client.connectionInstance.inputRequest == 1

    # Valid color test

    client.uiInstance.setInputGetter(True, "blue")

    assert client.connectionInstance.inputs[1] == (0, 0, 255)
    assert client.connectionInstance.inputRequest == 2
    assert all(item is None for item in client.connectionInstance.inputs[2:6]) is True


def test_getting_host():
    # Invalid host test
    for input in [None, "", 0]:
        client.uiInstance.setInputGetter(True, input)

        assert client.connectionInstance.inputs[2] is None
        assert client.connectionInstance.inputRequest == 2
        assert all(item is None for item in client.connectionInstance.inputs[2:6]) is True

    # Valid host test
    client.uiInstance.setInputGetter(True, "127.0.0.1")

    assert client.connectionInstance.inputs[2] == "127.0.0.1"
    assert client.connectionInstance.inputRequest == 3
    assert all(item is None for item in client.connectionInstance.inputs[3:6]) is True


def test_getting_port():
    # Invalid port test
    for input in [None, "", 0]:
        client.uiInstance.setInputGetter(True, input)

        assert client.connectionInstance.inputs[3] is None
        assert client.connectionInstance.inputRequest == 3
        assert all(item is None for item in client.connectionInstance.inputs[3:6]) is True

    # Valid port test
    client.uiInstance.setInputGetter(True, "12345")

    assert client.connectionInstance.inputs[3] == "12345"
    assert client.connectionInstance.inputRequest == 4
    assert all(item is None for item in client.connectionInstance.inputs[4:6]) is True


def test_getting_publicKey():
    # Invalid publicKey test
    for input in [None, "", 0]:
        client.uiInstance.setInputGetter(True, input)

        assert client.connectionInstance.inputs[4] is None
        assert client.connectionInstance.inputRequest == 4
        assert all(item is None for item in client.connectionInstance.inputs[4:6]) is True

    # Valid publicKey test
    client.uiInstance.setInputGetter(True, "244177280043")

    assert client.connectionInstance.inputs[4] == "244177280043"
    assert client.connectionInstance.inputRequest == 5
    assert all(item is None for item in client.connectionInstance.inputs[5:6]) is True


def test_getting_privateKey():
    # Invalid privateKey test
    for input in [None, "", 0]:
        client.uiInstance.setInputGetter(True, input)

        assert client.connectionInstance.inputs[5] is None
        assert client.connectionInstance.inputRequest == 5
        assert all(item is None for item in client.connectionInstance.inputs[5:6]) is True

    # Valid privateKey test
    client.uiInstance.setInputGetter(True, "257713280043")

    assert client.connectionInstance.inputs[5] == "257713280043"
    assert client.connectionInstance.inputs[4][6:12] == client.connectionInstance.inputs[5][6:12]
    assert client.connectionInstance.inputRequest == 6
    assert all(item is None for item in client.connectionInstance.inputs[6:6]) is True


def test_getting_cipherKey():
    # Invalid cipherKey test
    for input in [None, "", 0]:
        client.uiInstance.setInputGetter(True, input)

        assert client.connectionInstance.inputs[6] is None
        assert client.connectionInstance.inputRequest == 6
        assert all(item is None for item in client.connectionInstance.inputs[6:6]) is True

    # Valid cipherKey test
    client.uiInstance.setInputGetter(True, "1144")

    assert client.connectionInstance.inputs[6] == "1144"
    assert client.connectionInstance.inputRequest == 0
    assert all(item is not None for item in client.connectionInstance.inputs) is True


def test_arrow_keys_in_input():
    # Simulate an arrow key being pressed
    for value in [None, "random string"]:
        client.uiInstance.setInputGetter(False, value)

        assert client.connectionInstance.inputRequest == 0
        assert all(item is not None for item in client.connectionInstance.inputs) is True


def test_key_separation():
    # Test proper indexing and separation of keys
    client.connectionInstance.setConnection()

    assert client.connectionInstance.e == 244177
    assert client.connectionInstance.d == 257713
    assert client.connectionInstance.N == 280043
    assert client.connectionInstance.cipherKey == 14


def test_key_retrieval():
    # Test that the keys are the same after encrypting and decrypting
    for key in range(1, 26):
        assert key == client.communicationInstance.getrsaDecryptedMessage(
            client.communicationInstance.getrsaEncryptedMessage(key, 244177, 280043), 257713, 280043)


def test_string_retrieval():
    # Test that the messages are the same after encrypting and decrypting
    message = "my name is tomm 12345"
    for key in range(1, 26):
        assert message == client.communicationInstance.getCaesarDecryptedMessage(
            client.communicationInstance.getCaesarEncryptedMessage(message, key), key)

    message = "😁😛😋🤣"
    for key in range(1, 26):
        assert message == client.communicationInstance.getCaesarDecryptedMessage(
            client.communicationInstance.getCaesarEncryptedMessage(message, key), key)
    
    # Test that characters outside the alphabet are not encrypted
    message = "12345"

    for key in range(1, 26):
        assert message == client.communicationInstance.getCaesarEncryptedMessage(message, key)

    # Test that only characters in the alphabet are encrypted
    message = "abcde"

    for key in range(1, 26):
        assert message != client.communicationInstance.getCaesarEncryptedMessage(message, key)


def test_reset_inputs():
    # Should probably run last
    # Test that when a user provides an invalid inputs, every input so far is reset
    # First generate 7 values and test they are not none
    client.connectionInstance.inputs = [True for i in range(7)]

    assert all(item is not None for item in client.connectionInstance.inputs) is True

    # Reset every value
    client.connectionInstance.setInputsAsNone(None)

    assert all(item is None for item in client.connectionInstance.inputs) is True


def test_chat_history_retrieval():
    # Create a list of messages, save it into a file and test if it matches

    for message in ["my name is tomm 12345", "😁😛😋🤣"]:
        client.communicationInstance.setMessage(message)
        client.communicationInstance.setChatHistoryFile("test.txt")

        with open("test.txt", "r") as file:
            line = file.readline()

        assert line == strftime("%H:%M:%S", localtime()) + " {message}\n"
