import random

number = random.randint(1, 100)
hyphens = '-'*30
print('{0}\n{1:^30}\n{0}\n'.format(hyphens, 'GUESS THE NUMBER APP'))

while True:
    guess_string = input('Guess a number between 0 and 100: ')
    guess = int(guess_string)

    if guess < number:
        print('Sorry, but {} is LOWER than the number'.format(guess))
    elif guess > number:
        print('Sorry, but {} is HIGHER than the number'.format(guess))
    else: #guess == number:
        print('YES! You\'ve got it.  The number was {}'.format(number))
        break