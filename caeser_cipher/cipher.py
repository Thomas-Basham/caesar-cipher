import string
import re




def encrypt(message, shift):
    punctuation_set = list(string.punctuation)
    alphabet_list = list(string.ascii_lowercase)
    alphabet_list_upper = list(string.ascii_uppercase)
    # print(alphabet_list

    shifted_alphabet = []

    index_stack = []
    encrypted = []

    shifted = shift

    # Shift the alphabet
    for i in range(len(alphabet_list)):
        shifted_alphabet.append(alphabet_list[shifted % len(alphabet_list)])
        shifted = shifted + 1

    # retrieve indexes of alphabet
    for letter in message:
        if letter.isspace():
            index_stack.append(letter)
        if letter.isdigit():
            index_stack.append(letter)
        if letter in punctuation_set:
            index_stack.append(letter)
        cipher_text = ""
        if letter.isalpha():
            stay_in_alpha = ord(letter) + shift
            if stay_in_alpha > ord('z'):
                stay_in_alpha -= 26
            fina_letter = chr(stay_in_alpha)
            cipher_text += fina_letter
            index_stack.append(cipher_text)

    print(index_stack)

    # return shifted_alphabet index
    for number in index_stack:
        # if number == " ":
        #     encrypted.append(number)

        if isinstance(number, str):
            encrypted.append(number)
        elif number != " ":
            encrypted.append(shifted_alphabet[number])
    # print(punctuation_set)



    return ''.join([str(i) for i in encrypted])

encrypt("Gimme a 1!", 10)


def decrypt():
    pass


def crack():
    pass
