import random

amount_of_users_wins = 0
amount_of_computers_wins = 0
total_of_matches = 0
total_of_draws = 0

condition = ['rock', 'paper', 'scissors']
name_of_user = input('Could you please, type your name: ')

while True:
    user_pick = input('Type Rock or Paper or Scissors or Q to quit: ').lower()
    
    if user_pick == 'q':
        print(f"\nAs a result of the game:")
        print(f"The total of matches : {total_of_matches}")
        print(f"{name_of_user}'s wins : {amount_of_users_wins}")
        print(f"Computer's wins : {amount_of_computers_wins}")
        print(f"The total of draws : {total_of_draws}")
        break
        
    if user_pick not in condition:
        print("Invalid input! Please try again.")
        continue

    total_of_matches += 1
    random_number = random.randint(0, 2)
    computer_pick = condition[random_number]
    print(f"Computer picked {computer_pick}.")

    if user_pick == computer_pick:
        print('This is a DRAW!')
        total_of_draws += 1
        
    elif (user_pick == 'rock' and computer_pick == 'scissors') or \
         (user_pick == 'paper' and computer_pick == 'rock') or \
         (user_pick == 'scissors' and computer_pick == 'paper'):
        print('\nThis is your WIN!\n')
        amount_of_users_wins += 1
        
    else:
        print('\nComputers WIN!\n')
        amount_of_computers_wins += 1
