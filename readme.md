# Enigma Simulation
This Python project implements the inner workings of the three rotor versioned enigma device. The code is meant to simulate how the machine encodes and decodes messages. The code is meant for educational purposes and cryptographic experimentation.

## Code configurations
The enigma machine had a number of components that contributed to the possible configutations that it could generate. These are as follows:

1. The three rotor dials: Calssically the enigma machine had 5 differently arranged rotors. Three of these could be arranged in any order, giving a range of configurations. The rotors could also be configured with an initial position ranging from one to twenty six, representing each letter. This meant that for a given order of rotor dials, there were a total of 26X26X26 configurations, representing the 26 letter positions on each dial. 

2. The plugboard: This allowed for pairing of letters, such that one could be swapped with the other during encryption/decryption, and vice versea. 

