
import random 
word_list=["camel","elephant","dog"]

chosen_word=random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over= False
correct_letters = []

while not game_over:
    guess = input("guess a letter : ").lower()
    print(guess)

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
        else:
            display += "_"
    print(display)

    if "_" not in display:
        game_over=True
        print("you won")


# Work in progress
        


