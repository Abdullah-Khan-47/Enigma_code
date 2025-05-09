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

# The reflector
shuf_lst_4 = ['P', 'G', 'L', 'E', 'F', 'S', 'U', 'J', 'Z', 'A', 'H', 'V', 'M', 'R', 'W', 'D', 'B', 'X', 'I', 'C', 'O', 'T', 'Y', 'N', 'Q', 'K']
pair_lst_1 = shuf_lst_4[:13]
pair_lst_2 = shuf_lst_4[13:]
reflector_pairs = list(zip(pair_lst_1, pair_lst_2)) # Like the rotors, could not find data on reflector pairs. Can modify if data available

def reflector_encryption(letter, pairs=reflector_pairs): # Returns the encoded letter given an input letter and reflector pairings
    for pair in pairs:
        if letter in pair:
            for i in pair:
                if i!=letter:
                    return i
    return None

# Making a function that moves position in dict by one. Will be used later to change encryption mid message
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
    
# Making a functiom to ensure that letters tuples are not shared between pairs for plugboard switches
def plugboard_share_check(tuplst=[]):
    tups_seen = []
    for t in tuplst:
        for i in t:
            if type(i)!=str:
                print(f'{i} should not be entered, only letters A-Z.')
                return False
            i=i.upper()
            if i in tups_seen:
                print(f'letter {i} should only be entered once for the plugboard.')
                return False
            tups_seen.append(i)
    return True

# Making a function that swaps letter for the plugboard
def plugboard_switches(text, pairs):
    switch_dict = {}
    finallst = []
    for pair in pairs:
        switch_dict[pair[0].upper()] = pair[1].upper()
        switch_dict[pair[1].upper()] = pair[0].upper()

    for char in text:
        if char.upper() in switch_dict:
            finallst.append(switch_dict[char.upper()])

        else:
            finallst.append(char.upper())

    return ''.join(finallst)


# Making an encryption function that returns encrypted text based on inputted text, after one pass through the three dicts.
def text_rotary_encryption(text, first_dict=dict_1, second_dict=dict_2, third_dict=dict_3, dict1_preset=0, dict2_preset=0, dict3_preset=0, plugboard_lst=[]):

    # Checking plugboard letters.
    if len(plugboard_lst)>0:
        lst_check = plugboard_share_check(tuplst=plugboard_lst)
        if lst_check == False:
            print('Problem with plugboard entries, please try again')
            return None

    # Enigma only had 26 dial faces, each for a letter. because of this, we will restrict the preset values
    if dict1_preset>26 or dict2_preset>26 or dict3_preset>26 or dict1_preset<0 or dict2_preset<0 or dict3_preset<0:
        print('Preset values should be 1 to 26. Please retry with a different preset value.')
        return None
    
    else:
        for set1 in range(dict1_preset):
            first_dict = pos_rotation(first_dict)
        for set2 in range(dict1_preset):
            second_dict = pos_rotation(second_dict)
        for set3 in range(dict1_preset):
            third_dict = pos_rotation(third_dict)

    alph_lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    chr_count = 0
    encrypted_text = ''
    for char in text:
        chr_count+=1 # Needed to incorporate dial movement
        indx = alph_lst.index(char.upper())

        # Going through first dict
        first_dict = pos_rotation(first_dict) # movement with every character
        new_char = first_dict[indx]
        indx_renewed = alph_lst.index(new_char)

        # Going through second dict
        if chr_count%26==0: # movement with every 26th character. used for re-encryption on second and third dict, will incorporate later
            second_dict = pos_rotation(second_dict)
        new_char = second_dict[indx_renewed] 
        indx_renewed = alph_lst.index(new_char)

        # Going through third dict
        if chr_count%676==0: # movement with every 26X26th character
            third_dict = pos_rotation(third_dict)
        new_char = third_dict[indx_renewed]
        indx_renewed = alph_lst.index(new_char)

        # Reflector
        new_char = reflector_encryption(new_char)

        # Going back through the dicts
        third_index = list(third_dict.keys())[list(third_dict.values()).index(new_char)]
        new_char = alph_lst[third_index]

        second_index = list(second_dict.keys())[list(second_dict.values()).index(new_char)]
        new_char = alph_lst[second_index]
        first_index = list(first_dict.keys())[list(first_dict.values()).index(new_char)]
        new_char = alph_lst[first_index]

        # Going through the plupboard
        # if len(plugboard_lst)>0:
        #     for pair in plugboard_lst:
        #         for letr in pair:
        #             letr = letr.upper()
        #             if letr==new_char:
        #                 print(letr)
        #                 print(new_char)
        #                 print([l for l in pair if l.upper()!=new_char])
        #                 new_char = [l for l in pair if l.upper()!=new_char][0]
        #                 encrypted_text+=new_char


        
        encrypted_text+=new_char

    # Implementing plugboard swaps using the function used for the reflector
    if len(plugboard_lst)>0:
        encrypted_text = plugboard_switches(encrypted_text, pairs=plugboard_lst)

    return encrypted_text
