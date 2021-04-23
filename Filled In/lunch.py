import random 

RESTAURANTS = ['Chipotle', 'Burger King', 'PF Chang', 'AAA Sushi', 'Rosa Mexicana']
OUTPUT_FILE = 'recommendations.txt'


def get_lunch_recommendation():
    rec = random.choice(RESTAURANTS)

    with open(OUTPUT_FILE, 'a') as f:
        f.write(rec)

    return rec