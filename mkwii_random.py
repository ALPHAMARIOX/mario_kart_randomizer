import random

#Character list, which goes in order of weight class, then the Miis, which have access to all the vehicles, provided you have Miis of all weight classes.
char = ['Baby Mario', 'Baby Luigi', 'Baby Peach', 'Baby Daisy', 'Toad', 'Toadette', 'Koopa Troopa', 'Dry Bones',
        'Mario', 'Luigi', 'Peach', 'Daisy', 'Yoshi', 'Birdo', 'Diddy Kong', 'Bowser Jr.', 'Wario', 'Waluigi',
        'Donkey Kong', 'Bowser', 'King Boo', 'Rosalina', 'Funky Kong', 'Dry Bowser', 'Mii Outfit A', 'Mii Outfit B']

#Lightweight vehicles
vehicle_s = ['Standard Kart', 'Standard Bike', 'Booster Seat (Baby Booster)', 'Bullet Bike', 'Mini Beast (Concerto)',
             'Bit Bike (Nanobike)', 'Cheep Charger', 'Quacker', 'Tiny Titan (Rally Romper)', 'Magikruiser',
             'Blue Falcon', 'Jet Bubble (Bubble Bike)']

#Mediumweight vehicles
vehicle_m = ['Standard Kart', 'Stardard Bike', 'Classic Dragster (Nostalgia 1)', 'Mach Bike', 'Wild Wing',
             'Sugarscoot (Bon Bon)', 'Super Blooper (Turbo Blooper)', 'Zip Zip (Rapide)', 'Daytripper (Royal Racer)',
             'Sneakster (Nitrocycle)', 'Sprinter (B Dasher Mk 2)', 'Dolphin Dasher']

#Heavyweight vehicles
vehicle_l = ['Standard Kart', 'Standard Bike', 'Offroader', 'Flame Runner (Bowser Bike)', 'Flame Flyer', 'Wario Bike',
             'Piranha Prowler', 'Shooting Star (Twinkle Star)', 'Jetsetter (Aero Glider)', 'Spear (Torpedo)',
             'Honeycoupe (Dragonetti)', 'Phantom']

#Battle vehicles, which only have standard karts and bikes. Teams are already randomized in the game.
battle_v = ['Kart', 'Bike']

#Battle modes, coin runners is great for testing coin locations and timings if set properly.
battle_m = ['Balloon Battle', 'Coin Runners']

#Vehicles that the Miis can use. You will need to adjust the miis based on their weight class in-game.
mii_vehicle = ['Standard Kart', 'Standard Bike', 'Booster Seat (Baby Booster)', 'Bullet Bike', 'Mini Beast (Concerto)',
               'Bit Bike (Nanobike)', 'Cheep Charger', 'Quacker', 'Tiny Titan (Rally Romper)', 'Magikruiser',
               'Blue Falcon', 'Jet Bubble (Bubble Bike)', 'Classic Dragster (Nostalgia 1)', 'Mach Bike', 'Wild Wing',
               'Sugarscoot (Bon Bon)', 'Super Blooper (Turbo Blooper)', 'Zip Zip (Rapide)', 'Daytripper (Royal Racer)',
               'Sneakster (Nitrocycle)', 'Sprinter (B Dasher Mk 2)', 'Dolphin Dasher', 'Offroader',
               'Flame Runner (Bowser Bike)', 'Flame Flyer', 'Wario Bike', 'Piranha Prowler',
               'Shooting Star (Twinkle Star)', 'Jetsetter (Aero Glider)', 'Spear (Torpedo)', 'Honeycoupe (Dragonetti)',
               'Phantom']

#Creating a secured random number generator (RNG), followed by input in the console for VS, Battle or to quit.
secure_random = random.SystemRandom()
i = raw_input("Press Enter to Continue, type b for Battle Vehicles (or type n to quit): ")

#This should put the program in an infinite loop until n is type, which breaks from the loop.
while i.strip() != '\n':
    c = secure_random.choice(char)
    print("Your character is " + c + ".")
	
    if i.strip() == 'b':
	    print("Your vehicle is " + secure_random.choice(battle_v) + ".")
	    print("The battle mode selected is " + secure_random.choice(battle_m) + ".")
		
    else:
        if c in char[0:8]:
			print("Your vehicle is " + secure_random.choice(vehicle_s) + ".")
			
        elif c in char[8:16]:
			print("Your vehicle is " + secure_random.choice(vehicle_m) + ".")

        elif c in char[16:24]:
            print("Your vehicle is " + secure_random.choice(vehicle_l) + ".")

        else:
            print("Your vehicle is " + secure_random.choice(mii_vehicle) + ".")

    i = raw_input("Press Enter to Continue, type b for Battle Vehicles (or type n to quit): ")
    if i.strip() == 'n':
        break

print("Thank you for using the MKWii randomizer.")