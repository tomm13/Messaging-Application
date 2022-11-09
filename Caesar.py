# 9/11/2022
# Only accepts integers

test = "012345678"
key = 0
characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
              "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def caesarEncrypt(message):
    newMessage = ""
    for letter in message:

        if letter.isnumeric():
            index = (characters.index(letter) + key) % 36

            newMessage += characters[index]
        else:
            raise ValueError(f"Invalid character {letter}")

    return newMessage


def caesarDecrypt(message):
    newMessage = ""
    for letter in message:

        if letter.isalnum():
            index = (characters.index(letter) - key) % 36

            newMessage += characters[index]

        else:
            raise ValueError(f"Invalid character {letter}")

    return newMessage


encryptedMessage = caesarEncrypt(test)
print(f"encrypted message = {encryptedMessage}")

decryptedMessage = caesarDecrypt(encryptedMessage)
print(f"message = {decryptedMessage}")
