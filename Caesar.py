# First draft

test = "im GAY da Bu DEDE da BU da"
key = 23


def encrypt(message):
    newMessage = ""
    for letter in message:

        if letter.isalpha():

            if letter.islower():
                step = 97

            elif letter.isupper():
                step = 65

            index = ord(letter) + key - step

            while index > 25:
                index -= 26

            while index < 0:
                index += 26

            newMessage += chr(index + step)

        else:
            newMessage += letter

    return newMessage


def decrypt(message):
    newMessage = ""
    for letter in message:

        if letter.isalpha():

            if letter.islower():
                step = 97

            elif letter.isupper():
                step = 65

            index = ord(letter) - key - step

            while index > 25:
                index -= 26

            while index < 0:
                index += 26

            newMessage += chr(index + step)

        else:
            newMessage += letter

    return newMessage

encryptedMessage = encrypt(test)
print(encryptedMessage)

decryptedMessage = decrypt(encryptedMessage)
print(decryptedMessage)