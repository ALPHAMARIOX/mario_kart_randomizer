import random

char = ['Mario', 'Luigi', 'Peach', 'Daisy', 'Yoshi', 'Birdo', 'Waluigi', 'Baby Mario', 'Baby Luigi', 'Koopa Troopa', 'Koopa Paratroopa', 'Diddy Kong', 'Bowser Jr.', 'Toad',
        'Toadette', 'Donkey Kong', 'Bowser', 'Wario', 'King Boo', 'Petey Piranha']

vehicle_s = ['Goo-Goo Buggy', 'Rattle Buggy', 'Toad Kart', 'Toadette Kart', 'Koopa Dasher', 'Para-Wing', 'Barrel Train', 'Bullet Dasher', 'Parade Kart']

vehicle_m = ['Red Fire', 'Green Fire', 'Heart Coach', 'Bloom Coach', 'Turbo Yoshi', 'Turbo Birdo', 'Waluigi Racer', 'Parade Kart']

vehicle_l = ['DK Jumbo', 'Koopa King', 'Wario Car', 'Piranha Pipes', 'Boo Pipes', 'Parade Kart']

secure_random = random.SystemRandom()
i = raw_input("Press Enter to Continue (or type n to quit): ")
while i.strip() != '\n':
    c = secure_random.choice(char)
    h = secure_random.choice(char)
	
    print('Your characters are ' + c + ' and ' + h + '.')
	
    if c in char[15:20] or h in char[15:20]:
		print('Your vehicle is ' + secure_random.choice(vehicle_l) + '.')
	
    elif c in char[0:7] or h in char[0:7]:
		print ('Your vehicle is ' + secure_random.choice(vehicle_m) + '.')
		
    elif c in char[7:15] or h in char[7:15]:
		print ('Your vehicle is ' + secure_random.choice(vehicle_s) + '.')

    i = raw_input("Press Enter to Continue (or type n to quit): ")
    if i.strip() == 'n':
        break

print('Thank you for using the Mario Kart Double Dash Randomizer.')