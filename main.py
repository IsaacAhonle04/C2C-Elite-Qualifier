import random

def generate_response_1b(user_input):
  response_set_1b = [
    "Interesting!",
   # "Nice one!",
   # "Me too!"
  ]
  return random.choice(response_set_1b)

def generate_response_2b(user_input):
  response_set_2b = [
    "Wow!",
    "Cool!",
    "I didn't know that!"
  ]
  return random.choice(response_set_2b)

def generate_response_3b(user_input):
  response_set_3b = [
    "To Answer your question, I'm not quite sure...",
    "I'll have to think about that one!",
    "Hmmm... I don't have an answer right now."
  ]
  return random.choice(response_set_3b)  

def generate_response_4b(user_input):
  response_set_4b = [
    "Interesting!",
    "Nice one!",
    "Me too!",    
    "Wow!",
    "Cool!",
    "I didn't know that!"    
  ]
  return random.choice(response_set_4b)

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
        user_input = input(generate_response_4b(user_input) + "\n")
      else:
        user_input = input(generate_response_1b(user_input) + "\n")
    elif "." in user_input:
      if "!" in user_input:
        user_input = input(generate_response_4b(user_input) + "\n")
      else:
        user_input = input(generate_response_2b(user_input) + "\n")
    elif "?" in user_input:
        user_input = input(generate_response_3b(user_input) + "\n")   
    else:
        user_input = input(generate_response_4b(user_input) + "\n")         


if __name__ == "__main__":
  init_chat()