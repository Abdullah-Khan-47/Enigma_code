from text_encoder import text_rotary_encryption
from text_decoder import text_rotary_decryption
import argparse
import ast

def main():
    parser = argparse.ArgumentParser(description='File to be processed in Encryption and Decryption mode.')
    parser.add_argument('text', type=str, help='This is text that needs to be encoded/decoded.')
    parser.add_argument('--mode', required=True, choices=['encryption', 'decryption'], help='Specify if you want the inputted text encoded or decoded.')

    parser.add_argument('--first_dict', type=ast.literal_eval, 
                        default={0: 'A', 1: 'B', 2: 'E', 3: 'R', 4: 'C', 5: 'T', 6: 'W', 7: 'G', 8: 'M', 9: 'U', 10: 'Z', 11: 'P', 12: 'X', 13: 'H', 14: 'F', 15: 'J', 16: 'O', 17: 'D', 18: 'N', 19: 'L', 20: 'I', 21: 'S', 22: 'Q', 23: 'V', 24: 'K', 25: 'Y'}, 
                        help='This is the dict for the first rotor')
    parser.add_argument('--second_dict', type=ast.literal_eval, 
                        default={0: 'W', 1: 'V', 2: 'Y', 3: 'J', 4: 'L', 5: 'F', 6: 'X', 7: 'U', 8: 'B', 9: 'T', 10: 'C', 11: 'I', 12: 'G', 13: 'K', 14: 'N', 15: 'S', 16: 'P', 17: 'D', 18: 'R', 19: 'A', 20: 'H', 21: 'E', 22: 'M', 23: 'O', 24: 'Q', 25: 'Z'}, 
                        help='This is the dict for the second rotor')
    parser.add_argument('--third_dict', type=ast.literal_eval, 
                        default={0: 'V', 1: 'D', 2: 'S', 3: 'K', 4: 'R', 5: 'E', 6: 'H', 7: 'C', 8: 'W', 9: 'P', 10: 'J', 11: 'Q', 12: 'L', 13: 'U', 14: 'G', 15: 'T', 16: 'O', 17: 'X', 18: 'Y', 19: 'F', 20: 'A', 21: 'N', 22: 'M', 23: 'Z', 24: 'I', 25: 'B'},
                        help='This is the dict for the third rotor')

    parser.add_argument('--dict1_preset', type=int, default=0, help='Add a value from 1 to 26(for each letter)')
    parser.add_argument('--dict2_preset', type=int, default=0, help='Add a value from 1 to 26(for each letter)')
    parser.add_argument('--dict3_preset', type=int, default=0, help='Add a value from 1 to 26(for each letter)')

    parser.add_argument('--plugboard_lst', nargs="+", default=[], help='Add a multiple tuples as needed')

    # --mode needed above?
    args = parser.parse_args()

    if args.mode == 'encryption':
        print(f'The encrypted text is: {text_rotary_encryption(text=args.text, first_dict=args.first_dict, second_dict=args.second_dict, third_dict=args.third_dict, dict1_preset=args.dict1_preset, dict2_preset=args.dict2_preset, dict3_preset=args.dict3_preset, plugboard_lst=args.plugboard_lst)}')
    elif args.mode == 'decryption':
        print(f'The decrypted text is: {text_rotary_decryption(args.text)}')
    else:
        print('Please specify a mode, either encryption or decryption, and check if text has been added.')
    
if __name__ == "__main__":
    main()
