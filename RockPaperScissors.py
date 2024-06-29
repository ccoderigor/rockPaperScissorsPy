#! /usr/bin/python3.10

import random

def main():

	items = ['rock','paper','scissors']

	while True:	
		print('select an option(rock,paper,scissors)')
		user_choice = input('user choice: ')
		robot_choice = random.choice(items)
		print('robot choice: ' + robot_choice)

		if user_choice == 'rock' and robot_choice == 'paper':
			print('the robot wins!!')
		elif user_choice == 'rock' and robot_choice == 'scissors':
			print('you win!!')
		elif user_choice == 'rock' and robot_choice == 'rock':
			print('nobody wins')
		elif user_choice == 'paper' and robot_choice == 'scissors':
			print('the robot wins!!')
		elif user_choice == 'paper' and robot_choice == 'rock':
			print('you win!!')
		elif user_choice == 'paper' and robot_choice == 'paper':
			print('nobody wins')
		elif user_choice == 'scissors' and robot_choice == 'rock':
			print('the robot wins!!')
		elif user_choice == 'scissors' and robot_choice == 'paper':
			print('you win!!')
		elif user_choice == 'scissors' and robot_choice == 'scissors':
			print('nobody wins')
		elif user_choice == 'q':
			return
		else:
			print('choice not existing')

if __name__ == '__main__':
	print('welcome to rock paper scissors')
	print('type q for exit')
	main()
