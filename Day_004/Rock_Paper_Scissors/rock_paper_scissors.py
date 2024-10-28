import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

comp_choice = random.randint(0,2)

if user_choice == comp_choice:
	print(f"Computer chose {comp_choice}. \nIt's a tie. We go again.")
elif user_choice == 2 and comp_choice == 1:
	print(f"Computer chose {comp_choice}. \nYou win!")
elif user_choice == 1 and comp_choice == 0:
	print(f"Computer chose {comp_choice}. \nYou win!")
elif user_choice == 0 and comp_choice == 2:
	print(f"Computer chose {comp_choice}. \nYou win!")
else:
	print(f"Computer chose {comp_choice}. \nYou lose!")