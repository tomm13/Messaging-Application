# 2/4/2023
# V13.3.2

import server


def test_instantiaion():
    # Instantiate objects from server
    server.connection = server.Connection()
    server.security = server.Security()
    server.send = server.Send()


def test_binding_to_socket():
    # Test that the server binds with a valid host and port
    server.connection.bindToSocket()

    assert len(str(server.connection.port)) == 5
    assert server.connection.host is not None
    assert "." in server.connection.host


def test_key_generation():
    # Test that the keys are 6 digit
    server.security.getKeys()

    # Test that N is generated from 2 primes
    for prime in [server.security.P, server.security.Q]:
        for i in range(2, prime):
            assert prime % i != 0

    # Test that the length of all the components of the key are 6
    for key in [server.security.e, server.security.d, server.security.N]:
        assert len(str(key)) == 6

    # Test that the cipherkey is between 1 and 26
    assert 1 <= server.security.cipherKey <= 26


def test_key_retrieval():
    # Test that the keys are the same after encrypting and decrypting
    for key in range(1, 26):
        assert key == server.security.getrsaDecryptedMessage(
            server.security.getrsaEncryptedMessage(key, 244177, 280043), 257713, 280043)


def test_string_retrieval():
    # Test that the messages are the same after encrypting and decrypting
    message = "my name is tomm 12345"
    for key in range(1, 26):
        assert message == server.security.getCaesarDecryptedMessage(
            server.security.getCaesarEncryptedMessage(message, key), key)

    message = "😁😛😋🤣"
    for key in range(1, 26):
        assert message == server.security.getCaesarDecryptedMessage(
            server.security.getCaesarEncryptedMessage(message, key), key)

    # Test that characters outside the alphabet are not encrypted
    message = "12345"

    for key in range(1, 26):
        assert message == server.security.getCaesarEncryptedMessage(message, key)

    # Test that only characters in the alphabet are encrypted
    message = "abcde"

    for key in range(1, 26):
        assert message != server.security.getCaesarEncryptedMessage(message, key)


def test_username_validation():
    # Length 0, 8 or above, space and "None" are rejected
    for username in ["p p", "", "12345678", "None"]:
        assert server.connection.getUsernameValidity(username) is False

    # Valid username tests
    for username in ["random", "tommy", "ab123"]:
        assert server.connection.getUsernameValidity(username) is True


def test_message_length_validation():
    # Length 51 or above is rejected
    assert server.connection.getMessageLengthValidity(
        "123456789012345678901234567890123456789012345678901") is False

    # Length 50 or below is accepted
    assert server.connection.getMessageLengthValidity(
        "12345678901234567890123456789012345678901234567890") is True
    
