# write 'hello world' to the console
print('hello world')
# Write a rock, paper,scissors, game
# rules: rock beats scissors, scissors beats paper, paper beats rock
# ask the user for their choice
# generate a random choice for the computer
# print out the winner
# ask the user if they want to play again
# if yes, repeat the game
# if no, exit the game
# Path: app.py
# import the random module
import random
# while loop
while True:
    # ask the user for their choice
    user_choice = input('Choose rock, paper, or scissors: ')
    # generate a random choice for the computer
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    # print out the winner
    print(f'You chose {user_choice}, the computer chose {computer_choice}')
    # if the user chose rock
    if user_choice == 'rock':
        # if the computer chose rock
        if computer_choice == 'rock':
            # it's a tie
            print('It\'s a tie!')
        # if the computer chose paper
        elif computer_choice == 'paper':
            # the computer wins
            print('The computer wins!')
        # if the computer chose scissors
        else:
            # the user wins
            print('You win!')
    # if the user chose paper
    elif user_choice == 'paper':
        # if the computer chose rock
        if computer_choice == 'rock':
            # the user wins
            print('You win!')
        # if the computer chose paper
        elif computer_choice == 'paper':
            # it's a tie
            print('It\'s a tie!')
        # if the computer chose scissors
        else:
            # the computer wins
            print('The computer wins!')
    # if the user chose scissors
    else:
        # if the computer chose rock
        if computer_choice == 'rock':
            # the computer wins
            print('The computer wins!')
        # if the computer chose paper
        elif computer_choice == 'paper':
            # the user wins
            print('You win!')
        # if the computer chose scissors
        else:
            # it's a tie
            print('It\'s a tie!')
    # ask the user if they want to play again
    play_again = input('Do you want to play again? (y/n): ')
    # if the user doesn't want to play again