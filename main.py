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

import random

game_images= [rock,paper,scissors]

user= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))
computer= random.randint(0,2)

print("User: ",user)
print("Computer: ",computer,"\n\n")

if (user == computer):
		print("User: \n",game_images[user])
		print("Computer: \n",game_images[computer])
		print("\nIT'S A DRAW!")

elif( (user == 0 and computer == 1) or (user == 1 and computer == 2) or (user == 2 and computer == 0) ):
	print("User: \n",game_images[user])
	print("Computer: \n",game_images[computer])
	print("\nYOU LOSE!")

elif( (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1) ):
	print("User: \n",game_images[user])
	print("Computer: \n",game_images[computer])
	print("\nYOU WIN!")

else:
	print("INVALID NUMBER ENTERED")	