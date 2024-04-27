# roll the dice
import random

print("Welcome to the Dice Game")
username = input("Enter your name: ")

u = 0
c = 0

while True:
    input("Press Enter to roll the dice")
    rl = random.randint(1, 6)
    c1 = random.randint(1, 6)

    print(username + " rolled: " + str(rl))
    print("Computer rolled: " + str(c1))

    if (rl > c1):
        print(username + " wins this round!")
        u += 1
    elif (rl < c1):
        print("Computer wins this round!")
        c += 1
    else:
        print("It's a tie!")

    p = input("Do you want to continue? (yes/no): ")
    if (p.lower() != "yes"):
        break

print("\nGame Over!")
print(username + "'s score: " + str(u))
print("Computer's score: " + str(c))

if (u > c):
    print(username + " wins!")
elif (u < c):
    print("Computer wins!")
else:
    print("It's a tie!")
