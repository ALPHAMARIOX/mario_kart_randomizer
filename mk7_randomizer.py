import random

char = ['Mario', 'Luigi', 'Peach', 'Yoshi', 'Bowser', 'Donkey Kong', 'Toad', 'Koopa Troopa', 'Daisy', 'Wario', 'Rosalina', 'Metal Mario', 'Shy Guy', 'Honey Queen', 'Wiggler', 'Lakitu', 'Mii']

body = ['Standard', 'Gold Standard (Gold Kart)', 'Birthday Girl (Royal Ribbon)', 'Bumble V', 'Bruiser (Growlster)', 'Soda Jet', 'B Dasher',
        'Egg 1', 'Barrel Train', 'Tiny Tug', 'Cact-X', 'Koopa Clown', 'Cloud 9', 'Zucchini (Gherkin)', 'Blue Seven', 'Bolt Buggy', 'Pipe Frame']

tires = ['Standard (Normal)', 'Gold Tires (Gold Wheels)', 'Roller', 'Slim', 'Slick', 'Sponge', 'Mushroom', 'Wood (Wooden)', 'Red Monster', 'Monster']

glider = ['Super Glider', 'Gold Glider', 'Peach Parasol', 'Flower Glider', 'Beast Glider (Ghastly Glider)', 'Swooper (Swoop)', 'Paraglider (Parafoil)']

secure_random = random.SystemRandom()
i = raw_input("Press Enter to Continue (or type n to quit): ")
while i.strip() != '\n':

    print('Your character is ' + secure_random.choice(char) + '.')
    print('Your kart is ' + secure_random.choice(body) + '.')
    print('Your tires are ' + secure_random.choice(tires) + '.')
    print('Your glider is ' + secure_random.choice(glider) + '.')

    i = raw_input("Press Enter to Continue (or type n to quit): ")
    if i.strip() == 'n':
        break

print('Thank you for using the Mario Kart 7 Randomizer.')