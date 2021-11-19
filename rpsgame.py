
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

imgs = [rock, paper, scissors]

chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if chose >= 3 or chose < 0: 
  print("You typed an invalid number, you lose!") 
else:
  print(imgs[chose])
  pc = random.randint(0, 2)

  print("Computer chose:")
  print(imgs[pc])

  if chose == 0 and pc == 2:
    print("You win!")
  elif pc == 0 and chose == 2:
    print("You lose")
  elif pc > chose:
    print("You lose")
  elif chose > pc:
    print("You win!")
  elif pc == chose:
    print("It's a draw")                    
                      
