def user_input():
	user_number = int(input("please enter a number with 4 digit:"))
	while user_number < 1000 or user_number > 9999 :
		user_number = int(input("please re-enter a number, it must have 4 digit !"))
	return user_number


def	try_again_and_again(numbers):
	user_number = numbers[0]
	correct_number = numbers[1]
	nb_of_tries = 0
	while (user_number != correct_number):
		nb_of_tries += 1
		count = 0
		user_number = str(user_number)
		correct_number = str(correct_number)
		check_values = ['•', '•', '•', '•']

		for i in range(0, 4, 1):
			if (user_number[i] == correct_number[i]):
				check_values[i] = user_number[i]
				count += 1
			else:
				continue
	
		if (count == 0):
			print("all input are wrongs sorry try again")
			user_number = user_input
		elif (count < 4) and (count != 0):
			print("try again")
			print("these/this value(s) was/were correct :", '\n')
			for j in check_values:
				print(j, end=' ')
			print('\n')
			user_number = user_input

		return numbers