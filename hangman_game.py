import random
import hangman_pattern

word_list = ["apple", "banana", "orange", "strawberry", "grape", "pineapple"]

word = random.choice(word_list)

lives = 6
display = []
exit_game = False

for i in range(len(word)):
    display += "_"

print("**********Hangman Game**********")
print("You have 6 lives to guess the word")
print("Let's start the game")
# print(word)
print(display)

while not exit_game:
    guess = input("Guess The Letter :").lower()
    for item in range(len(word)):
        if word[item] == guess:
            display[item] = guess
    print(display)

    if guess not in word:

        lives -= 1
        print(hangman_pattern.pattern[lives])
        if lives == 0:
            exit_game = True
            print("You Lose")

    if "_" not in display:
        exit_game = True
        print("You Won")
