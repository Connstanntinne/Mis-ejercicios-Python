# This is a guess the numbargame.
import random
secretNumber= random.randint(1,20)
print('I am tincking of a numbar between 1 and 20.')

# Askthe player to guess 6 times.
for guessesTaken in range(1,7):
    print('Take a guess.')
    guess= int(input())

    if guess < secretNumber:
        print('Yoyr guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break         #Tis condition is teh correct guess!

if guess == secretNumber:
    print('Good job! Your guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
