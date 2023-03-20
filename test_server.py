# 16/3/2023
# V13.3

import server


def test_instantiaion():
    # Instantiate objects from server
    server.connectionInstance = server.Connection()
    server.securityInstance = server.Security()
    server.sendInstance = server.Send()


def test_binding_to_socket():
    # Test that the server binds with a valid host and port
    server.connectionInstance.bindToSocket()

    assert len(str(server.connectionInstance.port)) == 5
    assert server.connectionInstance.host is not None


def test_key_generation():
    # Test that the key generation is valid (keys are 6 digit, cipherkey is between 1 and 26)
    server.securityInstance.getKeys()
    
    # Test that N is generated from 2 primes
    for prime in [server.securityInstance.P, server.securityInstance.Q]:
        for i in range(2, prime):
            assert prime % i != 0
    
    # Test that the length of all the components of the key are 6
    for key in [server.securityInstance.e, server.securityInstance.d, server.securityInstance.N]:
        assert len(str(key)) == 6
    
    assert 1 <= server.securityInstance.cipherKey <= 26


def test_key_retrieval():
    # Test that the keys are the same after encrypting and decrypting
    for key in range(1, 26):
        assert key == server.securityInstance.getrsaDecryptedMessage(
            server.securityInstance.getrsaEncryptedMessage(key, 244177, 280043), 257713, 280043)


def test_string_retrieval():
    # Test that the messages are the same after encrypting and decrypting
    message = "my name is tomm 12345"
    for key in range(1, 26):
        assert message == server.securityInstance.getcaesarDecryptedMessage(
            server.securityInstance.getcaesarEncryptedMessage(message, key), key)

    message = "😁😛😋🤣"
    for key in range(1, 26):
        assert message == server.securityInstance.getcaesarDecryptedMessage(
            server.securityInstance.getcaesarEncryptedMessage(message, key), key)
        
    # Test that characters outside the alphabet are not encrypted
    message = "12345"
    
    for key in range(1, 26):
        assert message == server.securityInstance.getcaesarEncryptedMessage(message, key)
    
    # Test that only characters in the alphabet are encrypted
    message = "abcde"
    
    for key in range(1, 26):
        assert message != server.securityInstance.getcaesarEncryptedMessage(message, key)


def test_username_validation():
    # Length 0, 8 or above, space and "None" are rejected
    for username in ["p p", "", "12345678", "None"]:
        assert server.connectionInstance.validateUsername(username) is False

    # Valid username tests
    for username in ["random", "tommy", "ab123"]:
        assert server.connectionInstance.validateUsername(username) is True


def test_message_length_validation():
    # Length 51 or above is rejected
    assert server.connectionInstance.validateMessageLength("123456789012345678901234567890123456789012345678901") is False
    assert server.connectionInstance.validateMessageLength("12345678901234567890123456789012345678901234567890") is True
    assert server.connectionInstance.validateMessageLength("a") is True
