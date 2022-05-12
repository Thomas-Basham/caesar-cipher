import string
import re
import nltk
from nltk.corpus import words, names

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)


word_list = words.words()
name_list = names.words()


def encrypt(message, shift):
    # grab punctuation characters
    punctuation_list = list(string.punctuation)

    encrypted_list = []

    # add to encrypted list
    for letter in message:
        if letter.isspace():
            encrypted_list.append(letter)

        if letter.isdigit():
            encrypted_list.append(letter)

        if letter in punctuation_list:
            encrypted_list.append(letter)

        if letter.isalpha():
            cipher_text = ""
            stay_in_alpha = ord(letter) + shift

            if stay_in_alpha > ord('z'):
                stay_in_alpha -= 26
            fina_letter = chr(stay_in_alpha)
            cipher_text += fina_letter
            encrypted_list.append(cipher_text)

    return ''.join([str(i) for i in encrypted_list])


def decrypt(message, shift):
    return encrypt(message, -shift)


def crack(encrypted_message):

    def count_words(text):

        candidate_words = text.split()

        word_count = 0
        for candidate in candidate_words:
            word = re.sub(r'[^A-Za-z]+', '', candidate)
            if word in word_list or word in name_list:
                word_count += 1
            else:
                pass


        return word_count

    for i in range(26):
        results = encrypt(encrypted_message, i)
        word_count = count_words(results)
        percentage = int(word_count / len(results.split()) * 100)

        if percentage > 90:
            return results
    return ''

