from random import choice

def get_bot_response(user_response):
    #types of food response suggesstions
    bot_response_indian = [""]
    bot_response_italian = [""]
    bot_response_american = [""]
    bot_response_mexican = [""]
    bot_response_japanese = [""]
    bot_response_greek = [""]

    #if statements for user input on type of food
    if user_response == "indian":
        return choice(bot_response_indian)
    elif user_response == "italian":
        return choice(bot_response_italian)
    elif user_response == "american":
        return choice(bot_response_american)
    elif user_response == "japanese":
        return choice(bot_response_japanese)
    elif user_response == "greek":
        return choice(bot_response_greek)
    else:
        return "When in doubt, look at Yelp!"

