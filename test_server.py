# 18/1/2023
# V13.3

import server


def test_binding_to_socket():
    server.connectionInstance.bindToSocket()

    assert len(str(server.connectionInstance.port)) == 5
    assert server.connectionInstance.host is not None


def test_key_generation():
    server.securityInstance.getKeys()

    for key in [server.securityInstance.e, server.securityInstance.d, server.securityInstance.N]:
        assert len(str(key)) == 6

    assert 1 <= server.securityInstance.cipherKey <= 26


def test_key_retrieval():
    for key in range(1, 26):
        assert key == server.securityInstance.rsaDecrypt(server.securityInstance.rsaEncrypt(key, 244177, 280043), 257713, 280043)


def test_normal_string_retrieval():
    message = "my name is tomm 12345"
    for key in range(1, 26):
        assert message == server.securityInstance.caesarDecrypt(server.securityInstance.caesarEncrypt(message, key), key)


def test_emoji_string_retrieval():
    message = "😁😛😋🤣"
    for key in range(1, 26):
        assert message == server.securityInstance.caesarDecrypt(server.securityInstance.caesarEncrypt(message, key),
                                                                key)


def test_username_validation():
    # Length 0, 8 or above, space and "None" are rejected
    for username in ["p p", "", "12345678", "None"]:
        assert server.connectionInstance.validateUsername(username) is False

    assert server.connectionInstance.validateUsername("random") is True


def test_message_length_validation():
    # Length 51 or above is rejected
    assert server.connectionInstance.validateMessageLength("123456789012345678901234567890123456789012345678901") is False
    assert server.connectionInstance.validateMessageLength("12345678901234567890123456789012345678901234567890") is True
    assert server.connectionInstance.validateMessageLength("a") is True
