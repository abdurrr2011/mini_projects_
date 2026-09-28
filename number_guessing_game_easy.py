import random, sys

# r = random.randrange(-5, 11)
# r = random.randint(-5, 11)

top_of = input('Type a number: ')

if top_of.isdigit():
    top_of = int(top_of)
    
    if top_of <= 0:
        print('Please type a number greater than 0 next time.')
        sys.exit()
else:
    print('Please type a number next time.')
    sys.exit()
    
random_number = random.randrange(1, top_of)
guesses = 0

while True:
    guesses += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue
    
    if user_guess == random_number:
        break
        print('You got it!\n')
    else:
        print("You got it wrong!\n(Because you've writen not a number \nOR in other situation your writen number is not equals to guessed number by our Computer)\n")
        if user_guess > random_number:
            print('WARNING: You were above the number!\n')
        else:
            print('WARNING:You were below the number\n')

print(f"You got it in {guesses} guesses.")