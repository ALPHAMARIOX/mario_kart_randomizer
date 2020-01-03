import random

char = ['Mario', 'Luigi', 'Peach', 'Yoshi', 'Toad', 'Donkey Kong',
        'Wario', 'Bowser', 'Daisy', 'Dry Bones', 'Waluigi', 'R.O.B']

vehicle = ['B Dasher', 'Standard MR', 'Shooting Star', 'Poltergust 4000', 'Standard LG', "Streamliner",
           'Royale', 'Standard PC', 'Light Tripper', 'Egg 1', 'Standard YS', 'Cucumber',
           'Mushmellow', 'Standard TD', '4-Wheel Cradle', 'Rambi Rider', 'Standard DK', 'Wildlife',
           'Brute', 'Standard WR', 'Dragonfly', 'Tyrant', 'Standard BW', 'Hurricane',
           'Power Flower', 'Standard DS', 'Light Dancer', 'Banisher', 'Standard DB', 'Dry Bomber',
           'Gold Mantis', 'Standard WL', 'Zipper', 'ROB-BLS', 'Standard RB', 'ROB-LGS']

secure_random = random.SystemRandom()
i = raw_input("Press Enter to Continue (or type n to quit): ")
while i.strip() != '\n':

    print('Your character is ' + secure_random.choice(char) + '.')
    print('Your kart is ' + secure_random.choice(vehicle) + '.')

    i = raw_input("Press Enter to Continue (or type n to quit): ")
    if i.strip() == 'n':
        break

print('Thank you for using the Mario Kart DS Randomizer.')
