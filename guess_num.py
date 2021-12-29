# Inport exercise
import random
start_num = input('Please input start number:') 
end_num = input('Please input end number:')
start_num = int(start_num)
end_num = int(end_num)

r = random.randint(start_num, end_num)

up_limit = end_num
low_limit = start_num
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