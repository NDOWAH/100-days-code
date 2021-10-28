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

#Write your code below this line 👇
"""This program is very inefficient but our focus at this level is just to get the code working. Subsequently,
we shall get adiquate skills that we could use and make the code efficient"""
import random
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors."))

computer_choice = random.randint(0,2)
if user_choice == computer_choice:
  print("It's a draw game")
elif user_choice == 0 and computer_choice == 1:
  print("Sorry, you loose!")
  print("The computer choose", computer_choice)
elif user_choice == 0 and computer_choice == 2:
  print("Congratulation, you won!")
  print("The computer choose", computer_choice)
elif user_choice == 1 and computer_choice == 0:
  print("Sorry, you loose!")
  print("The computer choose", computer_choice)
elif user_choice == 1 and computer_choice == 2:
  print("Sorry, you loose!")
  print("The computer choose", computer_choice)
elif user_choice == 2 and computer_choice == 0:
  print("Sorry, you loose")
  print("The computer choose", computer_choice)
elif user_choice == 2 and computer_choice == 1:
  print("Sorry, you loose")
  print("The computer choose", computer_choice)
elif user_choice == 2 and computer_choice == 1:
  print("Congratulation, you won!")
  print("The computer choose", computer_choice)
elif user_choice == 1 and computer_choice == 2:
  print("Sorry, you loose!")
  print("The computer choose", computer_choice)