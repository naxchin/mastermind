def user_input():
	user_number = int(input('please enter a number with 4 digit:'))
	while user_number < 1000 or user_number > 9999 :
		user_number = int(input('please re-enter a number, it must have 4 digit :'))
	return user_number


def	try_again_and_again(numbers_list):
	user_number = str(numbers_list[0])
	correct_number = str(numbers_list[1])
	nb_of_tries = 0
	while (user_number != correct_number):
		nb_of_tries += 1
		count_correct_value = 0
		check_values = ['•', '•', '•', '•']
		for i in range(0, 4, 1):
			if (user_number[i] == correct_number[i]):
				count_correct_value += 1
				check_values[i] = user_number[i]
			else:
				continue
		if (count_correct_value == 0):
			print('all input are wrongs sorry try again', '\n')
			user_number = user_input
		elif (count_correct_value < 4) and (count_correct_value != 0):
			print('the correct value(s) is/are :', '\n')
			for i_array in check_values:
				print(i_array, end=' ')
			print('\n')
			user_number = user_input
	return numbers_list