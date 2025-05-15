# Enigma Simulation
This Python project implements the inner workings of the three rotor versioned enigma device. The code is meant to simulate how the machine encodes and decodes messages. The code is meant for educational purposes and cryptographic experimentation.

## Enigma Configurations
The enigma machine had a number of components that contributed to the possible configutations that it could generate. These are as follows:

1. The three rotor dials: Calssically the enigma machine had 5 differently ordered rotors. Three of these could be plugged in any order, giving a range of configurations. The rotors could also be configured with an initial position ranging from one to twenty six, representing each letter. This meant that for a given order of rotor dials, there were a total of 26X26X26 configurations, representing the 26 letter positions on each dial. 

2. The plugboard: This allowed for pairing of letters, such that one could be swapped with the other during encryption/decryption and vice versea. Given that there are 26 letters, we have a total of 0 to 13 possible letter pairs(0≤p≤13). Once a pair cable is plugged in, there will be two less plugs available for the next cable. This meant that for a given value of p, the following equation could be used to find the permutations: 
C(26, 2p) × (2p − 1) × (2p − 3) × (2p − 5) × · · · × 1

You can read more about the total possible(and practical) settings that were possible using enigma here: 
https://uregina.ca/~kozdron/Teaching/Cornell/135Summer06/Handouts/enigma.pdf

## Usage
On the terminal, you can use the run_machine.py file to encrypt and/or decrypt.

### Setting Mode
Set the mode to either "encryption" or "decryption" based on what you would like to do. For example, to encrypting the text 'helloworld', you would run the following:
python run_machine.py 'helloworld' --mode 'encryption'  # returns 'VHEAVPDYOW'

In order to decrypt this text, you would run the following:
python run_machine.py 'VHEAVPDYOW' --mode 'decryption'  # returns 'HELLOWORLD'

### Changing Initial State
The outputs in the previous example were based on base settings. You also have the ability to change these base settings and make your message secure. You have three main options in this case.
First, you can change the base rotors themselves...
Second, you can change the initial dial settings on one or more of the three chosen rotors...
Third, you can choose to swap letter pairs using the plugboard...

