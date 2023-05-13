
while True:
    user_question = input("Do you want to know how to keep a gullible person busy?\n")

    while user_question.lower() in ("yes", "YES", "y", "yeah", "yep", "sure", "Y"):
        user_question = input("Do you want to know how to keep a gullible person busy?\n")

    if user_question == str("no") or str("No"):
        print("You're smarter than you look.")
        break
