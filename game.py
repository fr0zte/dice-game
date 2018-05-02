# Import modules
import time
import random

# Initialise variables
points = 0
playing = True

try:
    while(playing):
        guess = int(input('Guess: '))
        bet = int(input('Bet: '))
        roll = random.randint(1, 6)
        if(guess == roll):
            points += bet * 2
        elif(guess != roll):
            points -= bet
        print('Points:', points)
        answer = input('Do you want to play again? ')
        if(answer == 'yes' or answer == 'Yes'):
            playing = True
        elif(answer == 'no' or answer == 'No'):
            playing = False

except KeyboardInterrupt:
    print('Program stopped using Ctrl+C.')
