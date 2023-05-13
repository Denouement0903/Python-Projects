name = input("What's your name?\n")

print("Hi", name)

def gay_game():
    question = input("Are you gay? (Y/N)\n")
    question2 = input("Do your friends know your gay? (Y/N)\n")

    while True:
        if question == str("Y") and question2 == str("Y"):
            print("Congrats", name)
        elif question == str("N") and question2 == str("N"):
            print(name, "you say you're not gay, and your friends also DO NOT know you're gay?.\nDoesn't that make you gay?.")
        elif question == str("Y") and question2 == str("N"):
            print(name, "it's 2022. You should tell them.\n")
        elif question == str("N") and question2 == str("Y"):
            print(name, "that sounds like denial.\n")
        else:
            print(name, "you can't run from the truth!")
        break

    question3 = input("Would you like to continue? (Y/N)\n")

    if question3 == str("Y"):
        question4 = input("Have you seen the clown that only hides from gay people? (Y/N)\n")
        if question4 == str("Y"):
            print("Me too. Guess you not gay.")
        elif question4 == str("N"):
            print("The clown only reveals itself to straight people. So if you haven't seen it, then you gay.")
    else:
        print("Thanks for playing!")
gay_game()
