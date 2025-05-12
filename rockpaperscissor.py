#rock papaer scissor game
import random
rock = """
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
user_choice=int(input("what do you choose? type 0 for rock, 1 for paper or 2 for scissor"))

if user_choice==0:
  print(rock)
if user_choice==1:
  print(paper)
if user_choice==2:
  print(scissor)
computer_choice=random.randint(0,2)
print(f"computer chose {computer_choice}")
if computer_choice==0:
  print(rock)
if computer_choice==1:
  print(paper)
if computer_choice==2:
  print(scissor)

if user_choice==0 and computer_choice==1:
  print("you win")
elif user_choice==0 and computer_choice==2:
  print("you win")
elif user_choice==1 and computer_choice==2:
  print("you lose")
elif user_choice==1 and computer_choice==0:
  print("you lose")
elif user_choice==2 and computer_choice==0:
  print("you lose")
elif user_choice==2 and computer_choice==1:
  print("you win")
elif user_choice==computer_choice:
  print("draw")
else:
  print("invalid input")
