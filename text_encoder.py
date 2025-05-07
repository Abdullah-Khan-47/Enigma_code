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

# Making an encryption function that returns encrypted text based on inputted text, after one pass through the three dicts.
def text_rotary_encryption(text, first_dict=dict_1, second_dict=dict_2, third_dict=dict_3):

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
        

        encrypted_text+=new_char
    
    return encrypted_text

test = text_rotary_encryption('hellohelpallahgivemetheabilitytobeacompetentpersonandblessmewithasuccessfullifeCraftingaperfectfivehundredcharactertextdemandsprecisionEveryletterspaceandmarkmattersensuringwedonotexceedtheexactcountIfasinglecharactergoesbeyondwefailThereforewemeticulouslychoosewordsThisdemonstrationhighlightsourcarefulapproachshortsentencescontrolledlengthmeaningfulcontentFinallyletsconfirmthatthistextmeetsthelimitbycountingeverysinglecharacterpreciselyThisfinallineensureswereachfivehundredexactlyYes')
print(test)