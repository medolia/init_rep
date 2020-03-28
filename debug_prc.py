# !python3 guess the coin: head or tail?
import random

guess = int(input("Guess the coin! Head(1) or tail(0): "))
toss = random.randint(0, 1)  # 0 for tail; 1 for heads.

if toss == guess:
    print('Bingo!')
else:
    print('Nope!Guess again!')
    guess = int(input("Guess the coin! Head(1) or tail(0): "))
    if toss == guess:
        print('Bingo')
    else:
        print('Nope. You are really bad at this game.')
