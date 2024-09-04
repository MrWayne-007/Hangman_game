
import random 
word_list=["camel","elephant","dog"]

chosen_word=random.choice(word_list)
print(chosen_word)

guess = input("guess a letter : ").lower()
print(guess)

for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("wrong")
        


