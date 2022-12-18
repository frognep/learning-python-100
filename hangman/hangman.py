import random
from os import system
from hangman_words import word_list
from hangman_art import logo, stages

end_of_game = False
chosen_word = random.choice(word_list)
user_lives = 6

print(logo)

# test
# print(f"pssst, word is {chosen_word}")

# Creates _'s as place holders for letters in chosen_word
display = []
for char in chosen_word:
    display += "_"

# Stores user guesses
guesses = []

while not end_of_game and not user_lives == 0:
    guess = input("Guess a letter: ").lower()

    system("clear")

    if guess in guesses:
        print(f"You have already guessed {guess}.")
    
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = guess

    if not guess in chosen_word and guess not in guesses:
      print(f"{guess} is not in the word. You lose a life.")
      user_lives -= 1
    
    guesses += guess

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    if not "_" in display:
        end_of_game = True
        print("You win.")
    
    if user_lives == 0:
        print("You have ran out of lives. You lose.")
        print(f"Word was {chosen_word}.")
        
    print(stages[user_lives])