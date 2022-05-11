import string
from itertools import cycle

# alphabet = {
#         'a' : '1',
#         'b' : '2',
#         'c' : '3',
#         'd' : '4',
#         'e' : '5',
#         'f' : '6',
#         'g' : '7',
#         'h' : '8',
#         'i' : '9',
#         'j' : '10',
#         'k' : '11',
#         'l' : '12',
#         'm' : '13',
#         'n' : '14',
#         'o' : '15',
#         'p' : '16',
#         'q' : '17',
#         'r' : '18',
#         's' : '19',
#         't' : '20',
#         'u' : '21',
#         'v' : '22',
#         'w' : '23',
#         'x' : '24',
#         'y' : '25',
#         'z' : '26'
#     }
# print(alphabet)

alphabet_list = list(string.ascii_lowercase)
print(alphabet_list)

def encrypt(string, shift):
    res = []
    k = shift
    index_stack = []
    encrypted = []
    for i in range(len(alphabet_list)):
        res.append(alphabet_list[k % len(alphabet_list)])
        k = k + 1
    for letter in string:
        if letter in alphabet_list:
            index_stack.append(alphabet_list.index(letter))
    for number in index_stack:
        encrypted.append(res[number])

    return ''.join([str(i) for i in encrypted])


encrypt('apple', 1)

# def encrypt_with_dict(string, shift):
#     stack = []
#     temp = list(alphabet)
#     for letter in string:
#         if letter in alphabet:
#             stack.append(temp[temp.index(letter) + shift])
#     return ''.join([str(i) for i in stack])

def decrypt():
    pass


def crack():
    pass
