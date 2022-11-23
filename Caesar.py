# 23/11/2022
# Rework handling of index > 26 or < 0

test = "abcdefgABCDEFG 1235649358790213!@(*$£(*&$*(%"
key = 23


def caesarEncrypt(message):
    newMessage = ""
    for letter in message:

        if letter.isalpha():

            if letter.islower():
                step = 97

            elif letter.isupper():
                step = 65

            index = (ord(letter) + key - step) % 26

            newMessage += chr(index + step)

        else:
            newMessage += letter

    return newMessage


def caesarDecrypt(message):
    newMessage = ""
    for letter in message:

        if letter.isalpha():

            if letter.islower():
                step = 97

            elif letter.isupper():
                step = 65

            index = (ord(letter) - key - step) % 26

            newMessage += chr(index + step)

        else:
            newMessage += letter

    return newMessage


encryptedMessage = caesarEncrypt(test)
print(encryptedMessage)

decryptedMessage = caesarDecrypt(encryptedMessage)
print(decryptedMessage)
