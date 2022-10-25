from logo import logo
import random
from replit import clear
print(logo)

random_num = random.randint(0,100)
  
def guess_number():
  ask_user = int(input("Guess the number: "))
  return ask_user

def easy_game():
  guess_attempts = 10
  print("\nEasy Mode. You have 10 attempts remaining to guess the number.")
  while (guess_attempts > 0):
    num_guessed = guess_number()
    if num_guessed < random_num:
      print("Higher")
      guess_attempts -= 1
      print(f"\nYou have {guess_attempts} guesses remaining.")
    elif num_guessed > 100:
      print("Error. Please guess a number between 1 and 100.")
      print(f"\nYou have {guess_attempts} guesses remaining.")
    elif num_guessed == random_num:
      print("Ding ding! You guessed the number!")
      guess_attempts = -1
    else:
      print("Lower")
      guess_attempts -= 1
      print(f"\nYou have {guess_attempts} guesses remaining.")
  if (guess_attempts == 0):
    continue_game = input("You ran out of guesses. Do you want to play again? Type 'y' or 'n': ")
    if continue_game == "y":
      clear()
      start_game()
    else:
      print("Goodbye!")
  else:
    continue_game = input("\nDo you want to play again? Type 'y' or 'n': ")
    if continue_game == "y":
      clear()
      start_game()
    else:
      print("Goodbye!")

def hard_game():
  guess_attempts = 5
  print("\nHard Mode. You have 5 attempts remaining to guess the number.\n")
  while (guess_attempts > 0):
    num_guessed = guess_number()
    if num_guessed < random_num:
      print("Higher")
      guess_attempts -= 1
      print(f"\nYou have {guess_attempts} guesses remaining.")
    elif num_guessed > 100:
      print("Error. Please guess a number between 1 and 100.")
      print(f"\nYou have {guess_attempts} guesses remaining.")
    elif num_guessed == random_num:
      print("Ding ding! You guessed the number!")
      guess_attempts = -1
    else:
      print("Lower")
      guess_attempts -= 1
      print(f"\nYou have {guess_attempts} guesses remaining.")
  if (guess_attempts == 0):
    continue_game = input("You ran out of guesses. Do you want to play again? Type 'y' or 'n': ")
    if continue_game == "y":
      clear()
      start_game()
    else:
      print("Goodbye!")
  else:
    continue_game = input("\nDo you want to play again? Type 'y' or 'n': ")
    if continue_game == "y":
      clear()
      start_game()
    else:
      print("Goodbye!")

def start_game():
  print("Welcome to the Number Guessing Game!\nI'm thinking of a number between [ 1 and 100 ].\n")
  user_start = input("Do you to play? Type 'y' or 'n': ")
  if (user_start == "y"):
    if input("Choose a difficulty. Type 'easy' or 'hard': ") == "easy":
      easy_game()
    else:
      hard_game()
  else:
    print("Goodbye!")
  
start_game()