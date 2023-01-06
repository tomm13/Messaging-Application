# 6/1/2023
# V13.3

import server

# Security


def test_generate_port():
    server.securityInstance.generatePort()

    assert len(str(server.connectionInstance.port)) == 5
    assert server.connectionInstance.host != '127.0.0.1'


def test_generate_key():
    server.securityInstance.generateKey()

    assert len(str(server.securityInstance.e)) == 6
    assert len(str(server.securityInstance.d)) == 6
    assert len(str(server.securityInstance.N)) == 6
    assert 1 <= server.securityInstance.cipherKey <= 26

# Test algorithmic accuracy


def test_key_retrieval():
    key = 9
    assert key == server.securityInstance.rsaDecrypt(server.securityInstance.rsaEncrypt(key))


def test_string_retrieval():
    message = "my name is tomm 12345"
    assert message == server.securityInstance.caesarDecrypt(server.securityInstance.caesarEncrypt(message))


def test_username_validation():
    # Length 0, 8 or above is rejected
    assert server.connectionInstance.validateUsername("p p") is False
    assert server.connectionInstance.validateUsername("") is False
    assert server.connectionInstance.validateUsername("12345678") is False
    assert server.connectionInstance.validateUsername("random") is True


def test_message_length_validation():
    # Length 51 or above is rejected
    assert server.connectionInstance.validateMessageLength("123456789012345678901234567890123456789012345678901") is False
    assert server.connectionInstance.validateMessageLength("12345678901234567890123456789012345678901234567890") is True
