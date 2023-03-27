from alpha_cypher import alphabet
from art import logo

def caesar(start_input, shift_num, cipher_direction):
    end_text = ""
    for char in start_input:
        if char in alphabet:    
            letter_position = alphabet.index(char)
            if cipher_direction == "encode":
                new_position = letter_position + shift_num
                if new_position > 25:
                    new_position %= 26
                end_text += alphabet[new_position]
            elif cipher_direction == "decode":
                new_position = letter_position - shift_num
                if new_position < 0:
                    new_position %= 26
                end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}.")


print(logo)
start_again = True
while start_again != False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_input=text, shift_num=shift, cipher_direction=direction)
    
    user_restart = (input("Would you like to restart the cipher program? ")).lower()
    if user_restart == "no":
        start_again = False
