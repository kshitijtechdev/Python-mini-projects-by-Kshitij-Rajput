# rock paper scissor game
import random

while True:
    uc = input("Enter your choice (rock, paper, scissors): ").lower()
    c = random.choice(['rock', 'paper', 'scissors'])
    print("Computer chooses:", c)

    if (uc == c):
        print("It's a tie!")
    elif (uc == 'rock' and c == 'scissors') or \
         (uc == 'paper' and c == 'rock') or \
         (uc == 'scissors' and c == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")

    o = input("Do you want to play again? (yes/no): ").lower()
    if (o != 'yes'):
        print("Thanks for playing!")
        break
