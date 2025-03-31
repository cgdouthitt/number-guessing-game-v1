"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

# Import the random module.
import random
# Create the start_game function.
def start_game():
# Write your code inside this function.

#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player as well as message before high score is set.
  print("<=======  !!!Welcome to the number guessing game!!!  =======>")
  print("The high score is not set yet. Go for it!!")
#   2. Initial variable setting. 
#     a. Store a random number as the answer/solution.
#     b. Store initial high score as highest possible score.
#     c. Store initial user guesses.
  random_number = random.randint(1, 10)
  high_score = 10
  user_guesses = 0
#   3. Continuously prompt the player for a guess.
#     a. If the guess is greater than the solution, display to the player "It's lower".
#     b. If the guess is less than the solution, display to the player "It's higher".
  while True:
    input_number = input("Guess a number (1 - 10): ")
    user_guesses += 1
    try:
      guessed_int = int(input_number)
      if guessed_int < 1 or guessed_int > 10:
        print("This number is outside the guess range.")
      elif guessed_int > random_number:
        print("It's lower")
      elif guessed_int < random_number:
        print("It's higher")
      else:
        print(f"\nYou got it!! \nIt took you {user_guesses} attempts to guess the number. \n\n<=======  !!Thanks for playing!!  =======>\n")
        play_again = input("Would you like to play again? (y/n): ")
        if play_again.lower() == "y":
          if high_score > user_guesses:
            high_score = int(user_guesses)
          print(f"The current high score is {high_score}")
          user_guesses = 0
          random_number = random.randint(1, 10)
          continue
        else:
          print(f"\n<=======  !!!Thank you for playing. Your high score was {high_score}!!!  =======>")
          break
    except ValueError:
      print("Please enter a number.")
      continue

#   Start the game
start_game()
