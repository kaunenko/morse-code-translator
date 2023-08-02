# Python program Morse Code Translator

"""
VARIABLE KEY
'cipher' -> 'stores the morse translated form of the english string'
'decipher' -> 'stores the english translated form of the morse string'
'citext' -> 'ores morse code of a single character'st
'message' -> 'stores the string to be encoded or decoded'
'words'-> 'store the list of words to be encoded '
"""

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != " ":
            try:
                cipher += MORSE_CODE_DICT[letter.upper()] + ' '
            except KeyError:
                cipher += ' . '

        else:
            cipher += " "

    return cipher


def decrypt(massage):
    citext = ''
    decipher = ''
    words = massage.split('  ')

    for word in words:
        citext = word.split()

        for cileter in citext:
            try:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(cileter)]
            except ValueError:
                decipher += '?'
        decipher += ' '

    return decipher


def main():
    while True:
        choice = input("Choice e to encrypt d to decrypt or any to exit:")
        if choice.upper() == 'E':
            print(encrypt(input("Enter message to encrypt: ")))
        elif choice.upper() == 'D':
            print(decrypt(input("Enter morse code to decrypt: ")))
        else:
            break



if __name__ == '__main__':
    main()
