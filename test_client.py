# 2/4/2023
# V13.3

import client
from time import localtime, strftime
from platform import system


def test_instantiation():
    # Instantiate objects from client
    client.connection = client.Connection()
    client.animation = client.Animation()
    client.communication = client.Communication()
    client.ui = client.UI()


def test_initialise_inputs():
    # Simulate nothing showing up until the first enter key is presssed
    client.ui.setInputGetter(True, None)

    assert all(item is None for item in client.connection.inputs) is True
    assert client.connection.inputRequest == 0


def test_getting_inputs():
    # Invalid tests are invalid values to be tested
    # Valid tests are the values to test, with color having a different output than input
    invalidTests = [[None, "", 0], [None, "invalidcolor", "white", "red"]]
    validTests = ["Username", ["blue", (0, 0, 255)], "127.0.0.1", "12345", "244177280043", "257713280043", "1144"]

    for test in range(7):
        # Invalid test
        # Every item in invalidTestValues are tested and tested to be invalid
        # Then validTestValue is tested once and compared with expectedValue, expected to pass
        if test == 1:
            # If testing colors, a specfic set of values have to be tested
            invalidTestValues = invalidTests[1]
            validTestValue = validTests[test][0]
            expectedValue = validTests[test][1]
            nextStep = test + 1

        elif test == 6:
            # For the final test, inputRequest has to cycle back to 0
            invalidTestValues = invalidTests[0]
            validTestValue = validTests[test]
            expectedValue = validTestValue
            nextStep = 0

        else:
            invalidTestValues = invalidTests[0]
            validTestValue = validTests[test]
            expectedValue = validTestValue
            nextStep = test + 1

        for val in invalidTestValues:
            # Invalid tests
            # Test that inputRequest does not increment after receiving an invalid input
            client.ui.setInputGetter(True, val)

            assert client.connection.inputs[test] is None
            assert client.connection.inputRequest == test
            assert all(item is None for item in client.connection.inputs[test:6]) is True

        # Valid test
        # Test that inputRequest only increments after receiving a valid input
        client.ui.setInputGetter(True, validTestValue)

        assert client.connection.inputs[test] == expectedValue
        assert client.connection.inputRequest == nextStep

        if test == 6:
            assert all(item is not None for item in client.connection.inputs) is True

        else:
            assert all(item is None for item in client.connection.inputs[nextStep:6]) is True


def test_arrow_keys_in_input():
    # Simulate an arrow key being pressed
    for value in [None, "random string"]:
        client.ui.setInputGetter(False, value)

        assert client.connection.inputRequest == 0
        assert all(item is not None for item in client.connection.inputs) is True


def test_key_separation():
    # Test proper indexing and separation of keys
    client.connection.setConnection()

    assert client.connection.e == 244177
    assert client.connection.d == 257713
    assert client.connection.N == 280043
    assert client.connection.cipherKey == 14


def test_key_retrieval():
    # Test that the keys are the same after encrypting and decrypting
    for key in range(1, 26):
        assert key == client.communication.getrsaDecryptedMessage(
            client.communication.getrsaEncryptedMessage(key, 244177, 280043), 257713, 280043)


def test_string_retrieval():
    # Test that the messages are the same after encrypting and decrypting
    message = "my name is tomm 12345"
    for key in range(1, 26):
        assert message == client.communication.getCaesarDecryptedMessage(
            client.communication.getCaesarEncryptedMessage(message, key), key)

    message = "😁😛😋🤣"
    for key in range(1, 26):
        assert message == client.communication.getCaesarDecryptedMessage(
            client.communication.getCaesarEncryptedMessage(message, key), key)

    # Test that characters outside the alphabet are not encrypted
    message = "12345"

    for key in range(1, 26):
        assert message == client.communication.getCaesarEncryptedMessage(message, key)

    # Test that only characters in the alphabet are encrypted
    message = "abcde"

    for key in range(1, 26):
        assert message != client.communication.getCaesarEncryptedMessage(message, key)


def test_reset_inputs():
    # Should probably run last
    # Test that when a user provides an invalid inputs, every input so far is reset
    # First generate 7 values and test they are not none
    client.connection.inputs = [True for i in range(7)]

    assert all(item is not None for item in client.connection.inputs) is True

    # Reset every value
    client.connection.setInputsAsNone(None)

    assert all(item is None for item in client.connection.inputs) is True


def test_chat_history_retrieval():
    # Create a list of messages, save it into a file and test if it matches

    for message in ["my name is tomm 12345", "😁😛😋🤣"]:
        client.communication.setMessage(message)
        client.communication.setChatHistoryFile("test.txt")

        with open("test.txt", "r") as file:
            line = file.readline()

        assert line == strftime("%H:%M:%S", localtime()) + " {message}\n"


def test_cycling_through_pages():
    # Test that pages are moving properly
    # communication.page refers to the current page whereas ui.page refers to the maximum page

    assert client.communication.page == 0
    assert client.ui.page == 0

    # Test that it's not possible to go below page 0
    client.communication.getPreviousPage()

    assert client.communication.page == 0
    assert client.ui.page == 0

    # Test that it's not possible to go to a page that hasn't been created
    client.communication.getNextPage()

    assert client.communication.page == 0
    assert client.ui.page == 0

    # Create a new page and that the client is on that page
    client.communication.getNewPage(None)
    assert client.communication.page == 1
    assert client.ui.page == 1
    assert client.ui.linesSent == 1

    # Test that the client is on page 0
    client.communication.getPreviousPage()

    assert client.communication.page == 0
    assert client.ui.page == 1

    # Test that the client is on page 1
    client.communication.getNextPage()

    assert client.communication.page == 1
    assert client.ui.page == 1

    # Test that it's not possible to go to a page that hasn't been created
    client.communication.getNextPage()

    assert client.communication.page == 1
    assert client.ui.page == 1


def test_message_counter_increments():
    # Test that for every message received by the server are counted properly

    assert client.ui.linesSent == 1

    client.ui.setFirstMessage(None)

    assert client.ui.linesSent == 2

    client.ui.setSubsequentMessage(None)

    assert client.ui.linesSent == 3

    # Get lineslimit by platform
    if system() == "Darwin":
        val = 19

    else:
        val = 18

    for i in range(3, val + 1):
        # Repeatedly add messages until the line limit is met, ensuring in each iteration that
        # linesSent is incremented properly
        client.communication.setMessage(None)

        if val < i:
            # Test increment is working properly unless a new page is being created
            assert client.ui.linesSent == i + 1

    # If a new page is created, all page values should increment and linesSent should return to 1
    assert client.communication.page == 2
    assert client.ui.page == 2
    assert client.ui.linesSent == 1


def test_lineslimit():
    # To ensure the consistency in UI elements
    if system() == "Darwin":
        assert client.ui.linesLimit == 19

    else:
        assert client.ui.linesLimit == 18