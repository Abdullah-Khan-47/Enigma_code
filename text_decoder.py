import random
import sys

# Making a function that reverses pos_rotation for decryption, used to track re-encoding during encryption
def reverse_pos_rotation(pos_dict):
    new_dict = {}
    for i in pos_dict.items():
        num = i[0]
        char = i[1]

        if num != 0:
            new_dict[num-1] = char
        elif num == 0:
            new_dict[25] = char

    return new_dict

# Reflector function to be used in decryption
def reflector_encryption(letter, pairs): # Returns the encoded letter given an input letter and reflector pairings
    for pair in pairs:
        if letter in pair:
            for i in pair:
                if i!=letter:
                    return i
    return None

# Making a decryption function that takes an encrypted text as well as dict states and returns the decrypted text
def text_rotary_decryption(text, first_dict, second_dict, third_dict):
    alph_lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    chr_count = 0
    decrypted_text = ''
    for char in text[::-1]:

        indx = alph_lst.index(char.upper())
        char = first_dict[indx]

        indx = alph_lst.index(char)
        char = second_dict[indx]
        
        indx = alph_lst.index(char)
        char = third_dict[indx]

        #Reflector
        char = reflector_encryption(char)

        third_index = list(third_dict.keys())[list(third_dict.values()).index(char)]
        third_chr_second = alph_lst[third_index]
        second_index = list(second_dict.keys())[list(second_dict.values()).index(third_chr_second)]
        second_chr_first = alph_lst[second_index]
        first_index = list(first_dict.keys())[list(first_dict.values()).index(second_chr_first)]
        origin_char = alph_lst[first_index]
        first_dict = reverse_pos_rotation(first_dict)

        decrypted_text+=origin_char

    return decrypted_text[::-1]
