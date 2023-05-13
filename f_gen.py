#!/usr/bin/env python3

import cgitb
import random

cgitb.enable()


def f_gen():
    user_name = input("What's your name?\n")
    print("Hi", user_name, "This is a random fact generator that prints 1 of 50 facts.\n")

    with open("./50_Facts.txt", "r") as file:
        contents = file.readlines() 

    user_response = input("Would you like to see a random fact?\n")
    
    while user_response == str("Y"):
            # generate a random number between 1 and 50
            fact_num = random.randint(1, 50)

            # display the fact
            print('<html>')
            print('<body>')
            print('<h1>Random Fact Generator</h1>')
            print('<p>Here is a random fact:</p>')
            print('<p>{}</p>'.format(contents[fact_num]))
            print('<p><a href="javascript:history.go(0)">Generate another random fact</a></p>')
            print('</body>')
            print('</html>')
            
            user_response = input("Would you like to see another random fact? (Y/N)\n")
            if user_response != str("Y"):
                break

f_gen()
