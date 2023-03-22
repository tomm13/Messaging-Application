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


def test_getting_inputs():
    invalidTests = [[None, "", 0], [None, "invalidcolor", "white", "red"]]
    validTests = ["Username", "blue", "127.0.0.1", "12345", "244177280043", "257713280043", "1144"]
    
    for test in range(7):
        # Invalid test
        if test == 1:
            testValues = invalidTests[0][1]
            
        else:
            testValues = invalidTests[0][0]
            
        for val in testValues:
            # Invalid test
            client.uiInstance.setInputGetter(True, val)

            assert client.connectionInstance.inputs[test] is None
            assert client.connectionInstance.inputRequest == test
            assert all(item is None for item in client.connectionInstance.inputs) is True

            # Valid test
            client.uiInstance.setInputGetter(True, val)

            assert client.connectionInstance.inputs[test] == "Username"
            assert client.connectionInstance.inputRequest == test + 1
            assert all(item is None for item in client.connectionInstance.inputs[test + 1:6]) is True

            
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
