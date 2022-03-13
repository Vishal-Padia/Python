name = input("Type your name: ")
print("Welcome", name ,"to the game")

answer = input("You are on a dirt road and it has come to an end and you can go left and right, which way do you want to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can either walk across it or swim across it.Type walk to walk across OR swim to swim across it: ")

    if answer == "swim":
        print("You swam across and got eaten by a alligator")
    elif answer == "walk":
        print("You walked acorss it and walked for miles after coming out of river and you died to dehydration! ")
    else:
        print("Not a valid option")

elif answer == "right":
    answer = input("You came to a bridge and it looks wobbly, do you want to cross it or head back? Type walk to walk over it and back to head back: ")
    if answer == "walk":
        answer = input("You crossed the bridge and meet a stranger. Do you talk with them? Type yes to talk and no to walk past him: ")
        
        if answer == "yes":
            answer = input("You talked with stranger and he offered you a candy! Do you want to eat it? Type yes to eat or no to decline the candy :")
            
            if answer == "yes":
                print("Duh you died! Never accept candies from strangers")
            elif answer == "no":
                print("Good for you that didn't accept the candy, But stranger kidnapped you and killed you, YOU DIED")
            else:
                print("Not a valid option")
        elif answer == "no":
                answer = input("Damn you just walked past the guard of the chest!!! Type collect to recieve the chest or fight to go back to the stranger and fight: ")
                if answer == "collect":
                    print("Congrats! You collected the chest")
                    answer = input("Do you want to open the chest? Type open to see what's in it or keep to just keep it: ")
                    
                    if answer == "open":
                        print("Opening the chest")
                        print("...")
                        answer = input("You opened the empty chest! Type continue to continue with the game or quit to quit the game: ")
                        
                        if answer == "continue":
                            print("Brave of you to still continue with the game")
                            answer = input("You walked past the chest and a board with numbers 69, 420, 999, choose one of the number: ")
                            if answer == "69":
                                print("NOICE! But you choose the wrong number and triggerd the nukes and exploded the whole planet and DIED!")
                            elif answer == "420":
                                print("NOICE! But still you choose the wrong number and the room got filled with poisonious gas and YOU DIED")
                            elif answer == "999":
                                answer = input("Congrats you choose the correct room! You see a chest with a lock, type collect to collect the chest and open to the chest: ")
                                
                                if answer == "keep":
                                    print("Why do want to keep the chest with a lock on when you can open it")
                                    print("You acquired the chest but still Died beacuse it was too heavy and it crushed your skull")
                                
                                elif answer == "open":
                                    print("OPENING THE CHEST")
                                    print("...")
                                    print("Congrats!! you opened the chest")
                                    print("You won the game",name,"!!!")
                                    print("THANKS FOR PLAYING THIS GAME",name)
                        
                    elif answer == "quit":
                        print("You Quit")
                        print("Thanks for playing the game",name,"!!")
                        
                    else:
                        print("Not a valid option")
                
                elif answer == "fight":
                    print("YOU DIED")
                    print("You fought him to the death, Farewell figther *salutes*")
                
                else: 
                    print("Not a valid option")
        
        else:
                print("Not an valid option!")    
    
    elif answer == "back":
         print("You went back and you are headed nowhere and died of hunger")
    
    else:
        print("Not a valid option")
