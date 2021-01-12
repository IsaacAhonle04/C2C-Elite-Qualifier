import random

def generate_response_1(user_input):
  response_set_1 = [
    "Interesting!",
    "Nice one!",
    "Me too!"
  ]
  return random.choice(response_set_1)

def generate_response_2(user_input):
  response_set_2 = [
    "Wow!",
    "Cool!",
    "I didn't know that!"
  ]
  return random.choice(response_set_2)

def generate_response_3(user_input):
  response_set_3 = [
    "To Answer your question, I'm not quite sure...",
    "I'll have to think about that one!",
    "Hmmm... I don't have an answer right now."
  ]
  return random.choice(response_set_3)  

def generate_response_4(user_input):
  response_set_4 = [
    "Interesting!",
    "Nice one!",
    "Me too!",    
    "Wow!",
    "Cool!",
    "I didn't know that!"    
  ]
  return random.choice(response_set_4)

def generate_response_bad(user_input):
  doing_bad = [
    "Same here...",    
    "I'm sorry to hear that :(",   
  ]
  return random.choice(doing_bad)

def generate_response_good(user_input):
  doing_good = [
    "Same here!",    
    "Good to hear! :)",   
  ]
  return random.choice(doing_good)

def init_chat():
  quit_character = 'q'

  user_input = input("Hello, how are you?\n")

  while user_input != quit_character:
    if "good" in user_input:
        user_input = input(generate_response_good(user_input) + "\n")      
    elif "bad" in user_input:
        user_input = input(generate_response_bad(user_input) + "\n")
    elif "!" in user_input:
      if "." in user_input:
        user_input = input(generate_response_4(user_input) + "\n")
      else:
        user_input = input(generate_response_1(user_input) + "\n")
    elif "." in user_input:
      if "!" in user_input:
        user_input = input(generate_response_4(user_input) + "\n")
      else:
        user_input = input(generate_response_2(user_input) + "\n")
    elif "?" in user_input:
        user_input = input(generate_response_3(user_input) + "\n")   
    else:
        user_input = input(generate_response_4(user_input) + "\n")         


if __name__ == "__main__":
  init_chat()