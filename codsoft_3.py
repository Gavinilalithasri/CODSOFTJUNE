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

game_images = [rock, paper, scissors]
userscore=0
comscore=0
ch=1
while ch==1:
  user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
  print(game_images[user_choice])
  computer_choice = random.randint(0, 2)
  print("Computer chose:")
  print(game_images[computer_choice])
  if user_choice >= 3 or user_choice < 0: 
     print("You typed an invalid number, you lose!") 
  elif user_choice == 0 and computer_choice == 2:
     print("You win!")
     userscore+=1
  elif computer_choice == 0 and user_choice == 2:
     print("You lose")
     comscore+=1
  elif computer_choice > user_choice:
     print("You lose")
     comscore+=1
  elif user_choice > computer_choice:
     print("You win!")
     userscore+=1
  elif computer_choice == user_choice:
    print("It's a draw")
  print("User score:",userscore)
  print("Computer score:",comscore)
  ch=int(input("Enter your choice(0/1):"))
  