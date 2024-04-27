# no guissing game
import random

print("Welcome to the Guessing Game")

s = random.randint(1, 100)

while True:
    g = int(input("Guess the number (between 1 and 100): "))
    
    if g == s:
        print("Congratulations! You guessed the correct number!")
        break
    elif g < s:
        print("its too low, Try guessing higher.")
    else:
        print("its too high, Try guessing lower.")
