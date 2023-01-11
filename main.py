import random

#Responds randomly with one of four preprogrammed responses

def generate_response(user_input):
  responses = [
    "Great!",
    "we gave a seasonal special!",
    " Awesome!"
    "Our menu is limited but delicious!"
  ]
  return random.choice(responses)

user_input = input("Hello are you ready to order?\n")

user_input = input(generate_response(user_input) + "Would you like chicken fajitas or tacos?\n")

  