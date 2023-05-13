import time

friends = ["f0", "f2", "f3", "f4", "f5"] #if you want to print a specific item in list it starts iterating from 0

question1 = input("Have you been socializing enough?\n")




def F_Rem():
    while question1 == str("N"):
        days_1  = 1 #259200 seconds is 3 days
        time.sleep(days_1) #the program sleeps for x days
        print("You haven't been to", friends[0], "in", days_1, " day.")
        days_2 = 2
        time.sleep(days_2)
        print("You haven't been to", friends[1], "in", days_2, "days.")
        break
F_Rem()
