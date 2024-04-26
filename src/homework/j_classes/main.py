#class_a
from class_a import *

die = Die()

while True:
    print("Rolling dice...")
    die.roll()
    die.get_rolled_value()
    print(die.__str__())

    while True:
        valid_responses = ['y', 'n']
        response = input("Would you like to continue? ['y','n']: ")

        if response not in valid_responses:
            continue
        else:
            break

    if response == 'y':
        continue
    else:
        break