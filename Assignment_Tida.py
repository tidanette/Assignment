player_name = input("Hello! What is your name? ")
print("Hello " + player_name + "! My name is Tida." )
answer = input("Do you want to play a game? (Y/N) ")
if answer.lower() == "y":
    print ("Let's play a guessing game!")
    fave_colour = "purple"
    no_guesses = 1
    guess = input("Can you guess my favourite colour? ")
    while True:
        if guess.lower() != fave_colour:
            print("Try again " + player_name + ".")
            no_guesses += 1
            guess = input("Can you guess my favourite colour? ")
        elif guess.lower() == fave_colour.lower():
                break
    print ("That's right! Congratulations " + player_name + "! It took you",no_guesses,"guesses!")
if answer.lower() == "n":
    print("Alright then. See you later!")
