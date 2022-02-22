#ROCK, PAPER, SCISSORS
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


#User's play & defining variables
play = input('LET\'S PLAY!\nWhat do you choose? Choose \"rock\", \"paper\", or \"scissors\":\n' ).lower()
weapon = [rock,paper,scissors]
import random
computers_play = random.choice(weapon)

#Weed out the typos...
if play != "rock" and play != "paper" and play != "scissors":
  print("Oops! Try again.")

#Let the game begin!
elif play == "rock":
  print(f"\nYou chose: {rock}")
  print(f"\nComputer chose: {computers_play}")
  
elif play == "paper":
  print(f"\nYou chose: {paper}")
  print(f"\nComputer chose: {computers_play}")

elif play == "scissors":
  print(f"\nYou chose: {scissors}")
  print(f"\nComputer chose: {computers_play}")

#Who wins?
if play == "rock" and computers_play == rock:
  print("IT'S A DRAW!")
elif play == "rock" and computers_play == paper:
  print("COMPUTER WINS!")
elif play == "rock" and computers_play == scissors:
  print("YOU WIN!")
elif play == "paper" and computers_play == rock:
  print("YOU WIN!")
elif play == "paper" and computers_play == paper:
  print("IT'S A DRAW!")
elif play == "paper" and computers_play == scissors:
  print("COMPUTER WINS!")
elif play == "scissors" and computers_play == rock:
  print("COMPUTER WINS!")
elif play == "scissors" and computers_play == paper:
  print("YOU WIN!")
elif play == "scissors" and computers_play == scissors:
  print("IT'S A DRAW!")