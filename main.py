import random

#Base personality response sets
def generate_response_1b(user_input):
  response_set_1b = [
    "\nInteresting!",
    "\nNice one!",
    "\nMe too!"
  ]
  return random.choice(response_set_1b)

def generate_response_2b(user_input):
  response_set_2b = [
    "\nWow!",
    "\nCool!",
    "\nI didn't know that!"
  ]
  return random.choice(response_set_2b)

def generate_response_3b(user_input):
  response_set_3b = [
    "\nTo Answer your question, I'm not quite sure...",
    "\nI'll have to think about that one!",
    "\nHmmm... I don't have an answer right now."
  ]
  return random.choice(response_set_3b)  

def generate_response_4b(user_input):
  response_set_4b = [
    "\nInteresting!",
    "\nNice one!",
    "\nMe too!",    
    "\nWow!",
    "\nCool!",
    "\nI didn't know that!"    
  ]
  return random.choice(response_set_4b)

def generate_response_bad(user_input):
  doing_bad = [
    "\nSame here...",    
    "\nI'm sorry to hear that :(",   
  ]
  return random.choice(doing_bad)

def generate_response_good(user_input):
  doing_good = [
    "\nSame here!",    
    "\nGood to hear! :)",   
  ]
  return random.choice(doing_good)

#Cold personality response sets
def generate_response_1c(user_input):
  response_set_1c = [
    "\nInteresting, considering it's coming from you",
    "\nMk",
    "\nHuh. Cool."
  ]
  return random.choice(response_set_1c)

def generate_response_2c(user_input):
  response_set_2c = [
    "\nHm.",
    "\nOh?",
    "\nAh, alright."
  ]
  return random.choice(response_set_2c)

def generate_response_3c(user_input):
  response_set_3c = [
    "\nUh, could you repeat that?",
    "\nJeez, being nosy now are we?",
    "\nHuh?"
  ]
  return random.choice(response_set_3c)

def generate_response_4c(user_input):
  response_set_4c = [
    "\nCold set 4 response 1",
    "\nCold set 4 response 2",
    "\nCold set 4 response 3"
  ]
  return random.choice(response_set_4c)

#Snarky personality response sets
def generate_response_1s(user_input):
  response_set_1s = [
    "\nSnarky set 1 response 1",
    "\nSnarky set 1 response 2",
    "\nSnarky set 1 response 3"
  ]
  return random.choice(response_set_1s)

def generate_response_2s(user_input):
  response_set_2s = [
    "\nSnarky set 2 response 1",
    "\nSnarky set 2 response 2",
    "\nSnarky set 2 response 3"
  ]
  return random.choice(response_set_2s)

def generate_response_3s(user_input):
  response_set_3s = [
    "\nSnarky set 3 response 1",
    "\nSnarky set 3 response 2",
    "\nSnarky set 3 response 3"
  ]
  return random.choice(response_set_3s)

def generate_response_4s(user_input):
  response_set_4s = [
    "\nSnarky set 4 response 1",
    "\nSnarky set 4 response 2",
    "\nSnarky set 4 response 3"
  ]
  return random.choice(response_set_4s)

# Main code  

def init_chat():
  quit_character = 'q'

  print("Thank you for using ChatBot 2.0! Please remember that the core functionality of this ChatBot revolves around punctuation, so for the best experience, you should use proper punctualization.")
  user_input = input("Which personality would you like? Your options are Basic, Cold, and Snarky.\n\n")
  while 1==1:
    if "Basic" in user_input:
      user_input = input("\nHello, how are you?\n\n")

      while user_input != quit_character:
        if "good" in user_input:
            user_input = input(generate_response_good(user_input) + "\n\n")      
        elif "bad" in user_input:
            user_input = input(generate_response_bad(user_input) + "\n\n")
        elif "!" in user_input:
          if "." in user_input:
            user_input = input(generate_response_4b(user_input) + "\n\n")
          else:
            user_input = input(generate_response_1b(user_input) + "\n\n")
        elif "." in user_input:
          if "!" in user_input:
            user_input = input(generate_response_4b(user_input) + "\n\n")
          else:
            user_input = input(generate_response_2b(user_input) + "\n\n")
        elif "?" in user_input:
            user_input = input(generate_response_3b(user_input) + "\n\n")   
        else:
            user_input = input(generate_response_4b(user_input) + "\n\n")        
    elif "Cold" in user_input:
      user_input = input("\nUh, hi. I'm your chatbot, I guess. So, go ahead. Chat.\n\n")

      while user_input != quit_character:
        if "!" in user_input:
          if "." in user_input:
            user_input = input(generate_response_4c(user_input) + "\n\n")
          else:
            user_input = input(generate_response_1c(user_input) + "\n\n")
        elif "." in user_input:
          if "!" in user_input:
            user_input = input(generate_response_4c(user_input) + "\n\n")
          else:
            user_input = input(generate_response_2c(user_input) + "\n\n")
        elif "?" in user_input:
            user_input = input(generate_response_3c(user_input) + "\n\n")   
        else:
            user_input = input(generate_response_4c(user_input) + "\n\n")          
    elif "Snarky" in user_input:
      user_input = input("\nGeneric snarky intro\n\n")

      while user_input != quit_character:
        if "!" in user_input:
          if "." in user_input:
            user_input = input(generate_response_4s(user_input) + "\n\n")
          else:
            user_input = input(generate_response_1s(user_input) + "\n\n")
        elif "." in user_input:
          if "!" in user_input:
            user_input = input(generate_response_4s(user_input) + "\n\n")
          else:
            user_input = input(generate_response_2s(user_input) + "\n\n")
        elif "?" in user_input:
            user_input = input(generate_response_3s(user_input) + "\n\n")   
        else:
            user_input = input(generate_response_4s(user_input) + "\n\n")        
    else:
      user_input = input("\nPlease enter an available option.\n\n")
    
if __name__ == "__main__":
  init_chat()