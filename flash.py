#january 23, 4:27
"""a simple flash card app for studing"""

#open app
#gives option if you want to study or add
#study 
"""when they study they should specify file name that exist"""
#add
"""when they add they should specify a file name"""

import os
import json
from random import choice

def start():
	print("""do you want to study or add a flash card? 
	-'s' to study
	-'a' to add flash card
	""")
	start_input = input(': ')

	if start_input == 'q':
		quit()
	elif start_input == 'a':
		add_flash_card()

	elif start_input == 's':
		study_flash_card()


def add_flash_card():
	try:
		with open('flash_card.json' , 'r') as f:
			flash_card = json.load(f)
	except (FileNotFoundError, json.JSONDecodeError):
		flash_card = {}

	while True:
		add_front_input = input('Add front: ')
		if add_front_input == 'q':
			break

		elif add_front_input == 's':
			study_flash_card()

		else:
			add_back_input = input('Add back: ')
		if add_back_input == 'q':
			break

		else:
			flash_card[add_front_input] = add_back_input

	with open('flash_card.json' , 'w') as f:
		json.dump(flash_card, f)

def study_flash_card():
	try:
		with open('flash_card.json' , 'r') as f:
			flash_card = json.load(f)
	except (FileNotFoundError, json.JSONDecodeError):
		flash_card = {}

	if not flash_card:
		print('Empty flash card')
	else:
		for key, value in flash_card.items():
				print(f'\nFront: {key}\n')
				print()
				print(""""do you wanna guess the back of the flash card? (remember it is case sensetive. if the answer is not the exact match it will say you are 'wrong'.)
	- Enter 'n' for 'No I just wanna see the answer.'""")
				guess = 3
				while guess:
					guess_back = input(':')
					if guess_back == 'q':
						break
					if guess_back == 'n':
						print(f'Back: {value}\n')
						break


					elif guess_back == value:
						print('You are correct!')
						print(f'Back: {value}')
						break

					elif guess_back != value:
						
						print(f"""\nthe answer '{guess_back}' is incorrect please guess again(remember it is case sensetive. if the answer is not the exact match it will say you are 'wrong'.
	-and you can always say 'no' by entering 'n'""")
					
						guess -= 1

start()