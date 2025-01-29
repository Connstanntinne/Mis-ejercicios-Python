computer_number = 9
guessed_correct = False
for guesses in range (1,6):
    player_number = input ('Enter your guess ')
    if computer_number == player_number:
        guessed_correct = True
    print ('Try again! ', guesses, 'left')
message = 'You win' if guessed_correct else 'You lose!'
print (message)


