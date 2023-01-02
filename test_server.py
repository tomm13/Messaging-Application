# 2/1/2023
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

def test_key_retrieval():
    key = 9
    assert key == server.securityInstance.rsaDecrypt(server.securityInstance.rsaEncrypt(key))

def test_string_retrieval():
    message = "my name is tomm"
    assert message == server.securityInstance.caesarDecrypt(server.securityInstance.caesarEncrypt(message))

def test_number_retrieval():
    message = "123456789"
    assert message == server.securityInstance.caesarDecrypt(server.securityInstance.caesarEncrypt(message))
