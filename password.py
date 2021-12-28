# Password check exercise
n = 2
while True:
	password = input('Please input password:')

	if n > 0:

		if password == 'a123456': #password
			print('Login')
			break
		else:
			n = n - 1 
			print ('Wrong password. You have', n, 'times')

	else:
		print('Wrong password over 3 tims. Please wait 15mins.')
		break