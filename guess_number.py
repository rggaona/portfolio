import random

easy_level = 10
hard_level = 5

def check_answer (answer, guess, lives):
  if answer > guess:
    print("Too high")
    return lives -1
  elif answer < guess:
    print("Too low")
    return lives -1
  else:
    print(f"you got it! The answer was {answer}")

def set_difficult ():
  difficult = input("Choose a difficult. Type 'easy' or 'hard': ")
  if difficult == "easy":
    return easy_level
  else:
    return hard_level

def game():
  print("Welcome to the Number Guessing Game")
  print("I'm thinking of a number betweeen 1 and 100.")
  answer = random.randint(1,100)

  lives = set_difficult()
  guess = 0

  while guess != answer:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    lives = check_answer(guess, answer, lives)
    if lives == 0:
      print("You've run put of lives, you lose.")
      return
    elif guess != answer:
      print("guess again")

game()
