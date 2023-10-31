player_name = input("Hello! What is your name? ")
print("Hello " + player_name + "! My name is Tida." )
answer = input("Do you want to play a game? (Y/N) ")
if answer == "Y":
    print ("Let's play a guessing game!")
    fave_colour = input("Can you guess my favourite colour? ")
    if fave_colour == "Purple":
        print ("That's right! Congratulations " + player_name + "!")
    if fave_colour != "Purple":
        print("Try again " + player_name + ".")
if answer == "N":
    print("Alright then. See you later!")
