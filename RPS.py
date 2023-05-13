import random
from random import randint
from random import randrange #Also generates random integer like randint
import itertools #To repaet a function, but goes on infintely if not specified
import sys #for the exit() method or break in While loops

Player = input("What's your name?\n")
print("Hi", Player, ".\n")
print("This is a Rock Paper Scissors game agianst the Computer.\n")
print("You can guess 1,2 or 3 for Rock, Paper or Scissors, respectively.\n")
print("You get 3 turns.\n")

user_guess = eval(input("What's your 1st guess?: \n"))

random_int = randrange(1,4)

#1st turn
Rock = 1
Paper = 2
Scissors = 3

def rps_game():
    if user_guess == random_int and user_guess == Rock:
        print("The guess was right", random_int, " it was Rock.")
    elif user_guess == random_int and user_guess == Paper:
        print("The guess was right", random_int, " it was Paper.")
    elif user_guess == random_int and user_guess == Scissors:
        print("The guess was right", random_int, "it was Scissors.")
    elif user_guess != random_int:
        print("Sorry wrong answer. It was ", random_int)

#2nd turn
user_guess2 = eval(input("What's your 2nd guess?: \n"))

random_int = randrange(1,4)

Rock = 1
Paper = 2
Scissors = 3

def rps_game2():
    if user_guess2 == random_int and user_guess2 == Rock:
        print("The guess was right", random_int, " it was Rock.")
    elif user_guess2 == random_int and user_guess2 == Paper:
        print("The guess was right", random_int, " it was Paper.")
    elif user_guess2 == random_int and user_guess2 == Scissors:
        print("The guess was right", random_int, "it was Scissors")
    elif user_guess2 != random_int:
        print("Sorry wrong answer. It was ", random_int)


#3rd turn
user_guess3 = eval(input("What's your 3rd guess?: \n"))

random_int = randrange(1,4)

Rock = 1
Paper = 2
Scissors = 3

def rps_game3():
    if user_guess3 == random_int and user_guess3 == Rock:
        print("The guess was right", random_int, " it was Rock.")
    elif user_guess3 == random_int and user_guess3 == Paper:
        print("The guess was right", random_int, " it was Paper.")
    elif user_guess3 == random_int and user_guess3 == Scissors:
        print("The guess was right", random_int, "it was Scissors.")
    elif user_guess3 != random_int:
        print("Sorry wrong answer. It was ", random_int)

rps_game()
rps_game2()
rps_game3()

#Still need a way to keep count.
#Try to make it 2 Player.
