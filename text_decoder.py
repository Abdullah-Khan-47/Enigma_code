import random
import sys

# letter list
alph_lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# making three randomly sorted copies that will represent the rotors in the enigma machine
shuf_lst_1 = ['A', 'B', 'E', 'R', 'C', 'T', 'W', 'G', 'M', 'U', 'Z', 'P', 'X', 'H', 'F', 'J', 'O', 'D', 'N', 'L', 'I', 'S', 'Q', 'V', 'K', 'Y']
shuf_lst_2 = ['W', 'V', 'Y', 'J', 'L', 'F', 'X', 'U', 'B', 'T', 'C', 'I', 'G', 'K', 'N', 'S', 'P', 'D', 'R', 'A', 'H', 'E', 'M', 'O', 'Q', 'Z']
shuf_lst_3 = ['V', 'D', 'S', 'K', 'R', 'E', 'H', 'C', 'W', 'P', 'J', 'Q', 'L', 'U', 'G', 'T', 'O', 'X', 'Y', 'F', 'A', 'N', 'M', 'Z', 'I', 'B']

# Giving each a random order because I could not find a 
# historical reference to the original order in any of the five rotors
# Can change later to reflect original orders if data available

# Turning the lists into dictionaries to keep track of letter positions
dict_1 = {}
for pos in range(len(alph_lst)):
    dict_1[pos] = shuf_lst_1[pos]

dict_2 = {}
for pos in range(len(alph_lst)):
    dict_2[pos] = shuf_lst_2[pos]

dict_3 = {}
for pos in range(len(alph_lst)):
    dict_3[pos] = shuf_lst_3[pos]

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

# The reflector
shuf_lst_4 = ['P', 'G', 'L', 'E', 'F', 'S', 'U', 'J', 'Z', 'A', 'H', 'V', 'M', 'R', 'W', 'D', 'B', 'X', 'I', 'C', 'O', 'T', 'Y', 'N', 'Q', 'K']


pair_lst_1 = shuf_lst_4[:13]
pair_lst_2 = shuf_lst_4[13:]
reflector_pairs = list(zip(pair_lst_1, pair_lst_2))

def reflector_encryption(letter, pairs=reflector_pairs):
    for pair in pairs:
        if letter in pair:
            for i in pair:
                if i!=letter:
                    return i
    return None

def pos_rotation(pos_dict):
    new_dict = {}
    for i in pos_dict.items():
        num = i[0]
        char = i[1]

        if num == 25:
            new_dict[0] = char
        else:
            new_dict[num+1] = char
    
    return new_dict

# Making a function that sets the rotor dictionary states based on the length of the text during decryption
def decryption_rotor_stateset(text, first_dict, second_dict, third_dict):
    text_len = len(text)
    # setting the first dict
    for i in range(text_len):
        first_dict = pos_rotation(first_dict)

    for j in range(int(text_len/26)):
        second_dict = pos_rotation(second_dict)

    for k in range(int(text_len/676)):
        third_dict = pos_rotation(third_dict)

    return first_dict, second_dict, third_dict

# Making a decryption function that takes an encrypted text as well as dict states and returns the decrypted text
def text_rotary_decryption(text, first_dict=dict_1, second_dict=dict_2, third_dict=dict_3):

    # Setting the states
    first_dict, second_dict, third_dict = decryption_rotor_stateset(text, first_dict, second_dict, third_dict)

    alph_lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    chr_count = -1
    decrypted_text = ''
    for char in text[::-1]:
        chr_count+=1

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
        if chr_count==len(text)%676 or chr_count%676==len(text)%676:
            third_dict = reverse_pos_rotation(third_dict)

        second_index = list(second_dict.keys())[list(second_dict.values()).index(third_chr_second)]
        second_chr_first = alph_lst[second_index]
        if chr_count==len(text)%26 or chr_count%26==len(text)%26:
            second_dict = reverse_pos_rotation(second_dict)
        
        first_index = list(first_dict.keys())[list(first_dict.values()).index(second_chr_first)]
        origin_char = alph_lst[first_index]
        first_dict = reverse_pos_rotation(first_dict)


        decrypted_text+=origin_char

    return decrypted_text[::-1]
