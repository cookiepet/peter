# Inport exercise
import random

r = random.randint(1, 100)

while True:
	num = input('Please input number (1~100):') 
	num = int(num)
	if r == num:
		print('Congrduation! You are right.')
		break
	elif r > num:
		print('Small than target number.')
	elif r < num:
		print('Larger than target number.')
