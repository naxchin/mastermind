import random
from mastermind_utils import *

print("                     _                      _           _ ")
print("                    | |                    (_)         | |")
print(" _ __ ___   __ _ ___| |_ ___ _ __ _ __ ___  _ _ __   __| |")
print("| '_ ` _ \ / _` / __| __/ _ \ '__| '_ ` _ \| | '_ \ / _` |")
print("| | | | | | (_| \__ \ ||  __/ |  | | | | | | | | | | (_| |")
print("|_| |_| |_|\__,_|___/\__\___|_|  |_| |_| |_|_|_| |_|\__,_|", "\n")

while(1):
	correct_number = random.randint(1000, 9999)
	print(correct_number)

	user_number = user_input()

	if (user_number == correct_number):
		print("You win first try gg !")
	else:
		numbers = [user_number, correct_number]
		result = try_again_and_again(numbers)

