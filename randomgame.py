import sys
from random import randint

first = int(sys.argv[1])
last = int(sys.argv[2])

randomno = randint(first, last)

while True:
    try:
        guess = int(input("What's your guess? :"))
        if guess == randomno:
            print("Nice Guess")
            break
    except ValueError:
        print("Please Enter a number")




