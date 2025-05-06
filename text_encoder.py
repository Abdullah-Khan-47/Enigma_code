import random

# letter list
alph_lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# making three copies that will represent the rotors in the enigma machine
shuf_lst_1 = alph_lst.copy()
shuf_lst_2 = alph_lst.copy()
shuf_lst_3 = alph_lst.copy()

random.shuffle(shuf_lst_1) # Giving each a random order because I could not find a 
random.shuffle(shuf_lst_2) # historical reference to the original order in any of the five rotors
random.shuffle(shuf_lst_3) # Can change later to reflect original orders if data available


