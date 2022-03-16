#This is my first python mini project
#Don't judge me based on this lol ;)
print("Welcome to my quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :) ")

answer = input("Do you like anime? ")
if answer.lower() == "yes": 
    print("Noice! Me Too")
else:
    print("Ehh! You Okay?? ")
    print("Thanks for playing  I GUESS")
    quit()

answer = input("Which is your favourite anime? ")
if ((answer.lower() == "naruto") or (answer.lower() == "black clover") or (answer.lower() == "jujutsu kaisen") or (answer.lower() =="dragon ball Z") or (answer.lower() == "demon slayer") or (answer.lower() == "deathnote")) :
        print("Ohh Great I like " + answer + " too!")
else:
    print("Nahh I haven't seen " + answer + " but I'll add it to my watchlist")

answer = input("Which was your first anime? ")
if ((answer.lower() == "naruto") or (answer.lower() == "deathnote")):
    print("Ohh I also started watching anime from " + answer+ " too!")
else:
    print("Ohh! but mine was Naruto")

answer = input("Do you think ANIME is better than noraml WEBSERIES?")
if answer.lower() == "yes":
    print("Ohh that was expected from you")
elif ((answer.lower() == "i don't know") or (answer.lower() == "idk")):
    print("I also feel the same sometimes!")
else:
    print("Sometimes we have to keep an open mind about other stuffs too!")

print("THANKS FOR PLAYING THIS QUIZ/GAME!")