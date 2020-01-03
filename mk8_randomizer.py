# -*- coding: latin-1 -*-
import random

char = ['Mario', 'Luigi', 'Peach', 'Daisy', 'Yoshi', 'Red Yoshi', 'Blue Yoshi', 'Light-Blue Yoshi', 'Yellow Yoshi', 'Pink Yoshi', 'Black Yoshi', 'White Yoshi', 'Orange Yoshi', 'Toad', 'Koopa Troopa', 'Shy Guy',
        'Green Shy Guy', 'Blue Shy Guy', 'Light-Blue Shy Guy', 'Yellow Shy Guy', 'Pink Shy Guy', 'Black Shy Guy', 'White Shy Guy', 'Orange Shy Guy', 'Baby Mario', 'Baby Luigi', 'Baby Peach', 'Baby Daisy',
        'Bowser', 'Donkey Kong', 'Wario', 'Waluigi', 'Rosalina', 'Metal Mario', 'Lakitu', 'Toadette', 'Baby Rosalina', 'Pink Gold Peach', 'Iggy', 'Roy', 'Lemmy', 'Larry', 'Wendy', 'Ludwig', 'Morton', 'Mii',
        'Tanooki Mario', 'Cat Peach', 'Link', 'Villager Male', 'Villager Female', 'Isabelle', 'Dry Bowser']

body = ['Standard Kart', 'Pipe Frame', 'Mach 8', 'Steel Driver', 'Cat Cruiser', 'Circuit Special', 'Tri-Speeder', 'Badwagon', 'Prancer', 'Biddybuggy (Buggybud)', 'Landship', 'Sneeker (Bounder)',
        'Sports Coupe (Sports Coupé)', 'Gold Standard (Gold Kart)', 'GLA', 'W 25 Silver Arrow', '300 SL Roadster', 'Blue Falcon', 'Tanooki Kart', 'B Dasher', 'Streetle', 'P-Wing', 'Standard Bike',
        'The Duke', 'Flame Rider', 'Varmint', 'Mr. Scooty (Mr Scooty)', 'City Tripper', 'Comet', 'Sport Bike', 'Jet Bike', 'Yoshi Bike', 'Master Cycle', 'Standard ATV (Standard Quad)', 'Wild Wiggler',
        'Teddy Buggy', 'Bone Rattler']

tires = ['Standard (Normal)', 'Monster', 'Roller', 'Slim', 'Slick', 'Metal', 'Button', 'Off-Road', 'Sponge', 'Wood (Wooden)', 'Cushion', 'Blue Standard (Normal Blue)', 'Hot Monster (Funky Monster)',
         ' Azure Roller', 'Crimson Slim', 'Cyber Slick', 'Retro Off-Road', 'Gold Tires (Gold Wheels)', 'GLA Tires (GLA Wheels)', 'Triforce Tires (Triforce Tyres)', 'Leaf Tires (Leaf Tyres)']

glider = ['Super Glider', 'Cloud Glider', 'Wario Wing', 'Waddle Wing', 'Peach Parasol', 'Parachute', 'Parafoil', 'Flower Glider', 'Bowser Kite', 'Plane Glider', 'MKTV Parafoil', 'Gold Glider',
          'Hylian Kite', 'Paper Glider']

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

print('Thank you for using the Mario Kart 8 Randomizer.')