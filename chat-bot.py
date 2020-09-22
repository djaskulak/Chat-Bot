from random import choice

def get_bot_response(user_response):
    #types of food response suggesstions
    bot_response_indian = ["samosa", "tikka masala", "chana masala", "saag paneer", 
        "vindaloo", "dal", "curry"]
    bot_response_italian = ["spaghetti", "caprese salad", "ravioli", "gnocchi", 
        "pizza", "charcuterie board", "fettuccine alfredo", "pasta primavera"]
    bot_response_american = ["burger", "fries", "salad", "mac and cheese", 
        "clam chowder", "bbq"]
    bot_response_mexican = ["empenadas", "floutas", "tacos", "burrito", 
        "chillaquiles", "chile relleno", "posole", "menudo"]
    bot_response_japanese = ["sushi", "ramen", "tempura", "soba noodles",
        "sashimi", "miso soup", "edamame", "mochi"]
    bot_response_greek = ["gyro", "dolmas", "moussaka", "souvlaki", "tzatziki",
        "baklava", "spanakopita", "hummus", "greek salad"]

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

print("Welcome to Food Bot!")
print("What type of food are you craving? I will give a suggestion on what to order... ")

user_response = ""

while True:
  user_response = input("What kind of food are you craving? ")
  
  # Quits program when user responds with 'done'
  if user_response == "done":
    break

  bot_response = get_bot_response(user_response)
  print(bot_response)