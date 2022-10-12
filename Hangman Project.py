    # Hangman Project


end_of_game = False # This allows game to repeat
    # import word list and art
import Hangman_Word_List
import Hangman_Art
from Hangman_Art import logo, stages

    # Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
chosen_word = random.choice(Hangman_Word_List.word_list)



    # Create an empty List called display. For each letter in the chosen_word, add a "_" to 'display'. 
display = []
word_length = len(chosen_word)
for letter in range(word_length):
    display += "_"

    # Give user 6 lives to guess the word
lives = 6


print(logo)



    # Begin actual game play
while not end_of_game:
    guess = input("Guess a letter: \n").lower()

            # Check if letter has already been guessed
    if guess in display:
        print(f"You have already guessed {guess}")
        
        # Reveal the letter if in chosen_word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        print(f"You guessed {guess}, that is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"Game over. The word was {chosen_word}.")

        # Turn elements into string (get rid of "" between blanks)
    print(f"{' '.join(display)}")
        

    if "_" not in display:
        end_of_game = True
        print("Congrats! You win!")
    
    print(stages[lives])