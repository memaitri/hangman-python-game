import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["Doctor"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Create a variable called 'lives' to keep track of the number of lives left.
lives = 6

# Debugging hint (remove later)
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = ["_"] * word_length

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check if already guessed
    if guess in display:
        print("You already guessed this letter. Try another one!")
        continue

    # Check guessed letter
    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        lives -= 1
        print(f"Wrong guess! You have {lives} lives left.")

        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was: {chosen_word}")
            break  # Stop the game immediately

    # Print current progress
    print(f"{' '.join(display)}")

    # Check if user has won
    if "_" not in display:
        end_of_game = True
        print("You win!")

    # Print the hangman stage
    print(stages[lives])
