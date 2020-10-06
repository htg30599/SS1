MORSE_CODE_DICT = {

}


def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '
    return cipher


def decrypt(message):
    message += ' '
    decipher = ''
    text = ' '
    for letter in message:
        if(letter != ' '):
            i = 0
            text += letter
        else:
            i += 1

            if i == 2:
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.key())[list(MORSE_CODE_DICT.values()).index(text)]
                text = ' '
    return decipher


def main():
    message = input("Input mes")
    result = encrypt(message.upper())
    print(result)