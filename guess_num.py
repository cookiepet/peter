# Inport exercise
import random

r = random.randint(1, 100)

up_limit = 100
low_limit = 1
count = 0

while True:
	count += 1 # equal to count = count +1
	print('Range:', low_limit, '~', up_limit) # Show range.
	num = input('Please input number:') 
	num = int(num)

	if r == num:
		print('Congrduation! You are right.')
		print ('This is', count, 'times')
		break
	elif r > num:
		low_limit = num
		print('Small than target number.')
	elif r < num:
		up_limit = num
		print('Larger than target number.')

	print ('This is', count, 'times')