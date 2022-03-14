import random
from typing import Tuple

top_of_range = input("Type a number: ")
guesses = 0

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please a type number greater than 0 next time")
        quit()
else:
    print("Please enter a number")
    quit()        


random_number = random.randint(0, top_of_range)

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number")
        continue        
    
    if user_guess == random_number:
        print("You got it mate!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")