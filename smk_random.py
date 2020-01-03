import random

char = ['Mario', 'Luigi', 'Peach', 'Toad', 'Yoshi', 'Koopa Troopa', 'Donkey Kong Jr.', 'Bowser']

secure_random = random.SystemRandom()
i = raw_input("Press Enter to Continue (or type n to quit): ")
while i.strip() != '\n':
	c = secure_random.choice(char)
	print("Your character is " + c + ".")
	
	i = raw_input("Press Enter to Continue (or type n to quit): ")
	if i.strip() == 'n':
		break

print("Thank you for using the SMK randomizer.")