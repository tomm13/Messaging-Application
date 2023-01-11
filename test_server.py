# 11/1/2023
# V13.3

import server

# Security


def test_generate_port():
    server.securityInstance.generatePort()

    assert len(str(server.connectionInstance.port)) == 5
    assert server.connectionInstance.host != '127.0.0.1'


def test_generate_key():
    server.securityInstance.generateKey()

    for key in [server.securityInstance.e, server.securityInstance.d, server.securityInstance.N]:
        assert len(str(key)) == 6

    assert 1 <= server.securityInstance.cipherKey <= 26

# Test algorithmic accuracy


def test_key_retrieval():
    for key in range(1, 26):
        assert key == server.securityInstance.rsaDecrypt(server.securityInstance.rsaEncrypt(key, 244177, 280043), 257713, 280043)


def test_string_retrieval():
    message = "my name is tomm 12345"
    for key in range(1, 26):
        assert message == server.securityInstance.caesarDecrypt(server.securityInstance.caesarEncrypt(message, key), key)


def test_username_validation():
    # Length 0, 8 or above, space and "None" are rejected
    for username in ["p p", "", "12345678", "None"]:
        assert server.connectionInstance.validateUsername(username) is False

    assert server.connectionInstance.validateUsername("random") is True


def test_message_length_validation():
    # Length 51 or above is rejected
    assert server.connectionInstance.validateMessageLength("123456789012345678901234567890123456789012345678901") is False
    assert server.connectionInstance.validateMessageLength("12345678901234567890123456789012345678901234567890") is True
