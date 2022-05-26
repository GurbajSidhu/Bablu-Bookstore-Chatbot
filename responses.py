from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup", "yo","Who are you?", "help"):
        return "Hey there, how's it going? \nI am the Bablu bookstore's librarian chatbot! \nI can instantly provide information on the availability of a book in the shop. \n\nWhich book would you like to search for?"


    if user_message in ("1984", "the idiot", "zorba the greek", "the great gatsby", "gates of fire", "dune"):
        return "Success! This book is available at our shop. \nWould you like to pick it up or have it delivered at your home? \n\nIf you want to keep looking, enter another name."

    if user_message in ("pick it up", "pick up"):
        return "Great! Please come visit our store in Old Patiala. \nWe are open Monday-Saturday from 9am-9pm."

    if user_message in ("order", "order it"):
        return "Great! your request has been logged. \nOur shop staff will call you soon for order confirmation. \n\nHave a Great day!"

    if user_message in ("bye", "exit", "thanks"):
        return "Bye! See you again!"

    if user_message in ("bye", "exit"):
        return "Bye! See you again!"

    if user_message in ("bye", "exit"):
        return "Bye! See you again!"

    if user_message in ("bye", "exit"):
        return "Bye! See you again!"

    if user_message in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    if user_message in ("hello", "hi", "sup", "yo"):
        return "Hey there, how's it going?"

    if user_message in ("hello", "hi", "sup", "yo"):
        return "Hey there, how's it going?"

    return ("I am sorry, it seems we do no have this book.")
