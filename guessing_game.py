"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

# Import the random module.
import random
# High score
high_score = 0
# Create the start_game function.
def start_game():
# Write your code inside this function.

#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.
  print("<=======  !!!Welcome to the number guessing game!!!  =======>")
  print("The high score is not set yet. Go for it!!")
#   2. Store a random number as the answer/solution.
  random_number = random.randint(1, 10)
#   3. Continuously prompt the player for a guess.
#     a. If the guess is greater than the solution, display to the player "It's lower".
#     b. If the guess is less than the solution, display to the player "It's higher".
  high_score = 10
  user_guesses = 0
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
        print(f"You got it!! \nIt took you {user_guesses} attempts to guess the number. \n<=======  !!Thanks for playing!!  =======>")
        play_again = input("Would you like to play again? (y/n): ")
        if play_again.lower() == "y":
          if high_score > user_guesses:
            high_score = int(user_guesses)
          print(f"The current high score is {high_score}")
          user_guesses = 0
          random_number = random.randint(1, 10)
          continue
        else:
          break
    except ValueError:
      print("Please enter a number.")
      continue
    
#   4. Once the guess is correct, stop looping, inform the user they "Got it"
#      and show how many attempts it took them to get the correct number.
    
#   5. Let the player know the game is ending, or something that indicates the game is over.

# ( You can add more features/enhancements if you'd like to. )


# Kick off the program by calling the start_game function.
start_game()
