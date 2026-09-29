import sys


name = input('Type your name: ')
print(f"Welcome {name} to this game.")

answer = input('You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ').lower()

if answer == 'left':
    answer = input('You come to a river, and you can walk around it or swim across? Type "walk" tp walk around and "swim" to swim across: ').lower()
    if answer == 'swim':
        print(f"You swam across and were eaten by an alligator")
    elif answer == 'walk':
        print(f"You walked for many miles, ran out of water and lost the game")
    else:
        print('Not a valid option. You lose')
elif answer == 'right':
    answer = input('You come to a bridge, it looks wobbly, do you fancy to cross it or head back(cross/back)?').lower()
    
    if answer == 'back':
        print(f"You back head back  and lose.")
    elif answer == 'cross':
        answer = input(f"You've crossed the bridge, and meet a stranger. Do you fancy to talk with him? (yes/no)").lower()
        
        if answer == 'yes':
            print('You talk to the stranger and they give you a gold. YOU actually WIN!')
        elif answer == 'no':
            print('You ignore the stranger and they are offended , then you lose.')
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose')
else:
    print('Not a valid option. You lose.')
    
print(f"I appreciate you, {name} for trying this game from your side!")

sys.exit()