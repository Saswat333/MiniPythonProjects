import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)
choosen_word = random.choice(word_list)
word_len = len((choosen_word))
lives = 6
end_of_game = False

# Testing code
print(f'Pssst, the solution is {choosen_word}.')

display = []
for _ in range(word_len):
    display += "_"
print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You hvae already guessed {guess}")

    for position in range(word_len):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in choosen_word:
        print(f"You guessed {guess}. that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose !!!")

    print(display)
    if "_" not in display:
        end_of_game = True
        print("You won !!")

    print(stages[lives])