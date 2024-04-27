# voting system
es = 1
voteBJP = 0
voteCONGRESS = 0
voteAAP = 0
voteOTHERS = 0

while (es == 1):
    name = input("Enter candidate name: ")
    age = int(input("Enter candidate age: "))
    choice1 = int(input("To vote 'BJP', press 1\nTo vote 'Congress', press 2\nTo vote 'AAP', press 3\nTo vote 'Others', press 4\n"))
    choice2 = int(input("To continue, press 1\nTo exit, press 2\n"))

    if (age >= 18):
        if (choice1 == 1):
            print("You have successfully voted BJP. Thanks for voting!")
            voteBJP += 1
        elif (choice1 == 2):
            print("You have successfully voted Congress. Thanks for voting!")
            voteCONGRESS += 1
        elif (choice1 == 3):
            print("You have successfully voted AAP. Thanks for voting!")
            voteAAP += 1
        elif (choice1 == 4):
            print("You have successfully voted Others. Thanks for voting!")
            voteOTHERS += 1
        else:
            print("Enter a valid choice for voting the party. Two attempts left.")
            choice1 = int(input("To vote 'BJP', press 1\nTo vote 'Congress', press 2\nTo vote 'AAP', press 3\nTo vote 'Others', press 4\n"))
            if (choice1 == 1):
                print("You have successfully voted BJP. Thanks for voting!")
                voteBJP += 1
            elif (choice1 == 2):
                print("You have successfully voted Congress. Thanks for voting!")
                voteCONGRESS += 1
            elif (choice1 == 3):
                print("You have successfully voted AAP. Thanks for voting!")
                voteAAP += 1
            elif (choice1 == 4):
                print("You have successfully voted Others. Thanks for voting!")
                voteOTHERS += 1
            else:
                print("Enter a valid choice for voting the party. One attempt left.")
                choice1 = int(input("To vote 'BJP', press 1\nTo vote 'Congress', press 2\nTo vote 'AAP', press 3\nTo vote 'Others', press 4\n"))
                if (choice1 == 1):
                    print("You have successfully voted BJP. Thanks for voting!")
                    voteBJP += 1
                elif (choice1 == 2):
                    print("You have successfully voted Congress. Thanks for voting!")
                    voteCONGRESS += 1
                elif (choice1 == 3):
                    print("You have successfully voted AAP. Thanks for voting!")
                    voteAAP += 1
                elif (choice1 == 4):
                    print("You have successfully voted Others. Thanks for voting!")
                    voteOTHERS += 1

        if (choice2 == 2):
            if (voteBJP > voteCONGRESS and voteBJP > voteAAP and voteBJP > voteCONGRESS and voteBJP > voteOTHERS):
                print("BJP IS THE WINNER")
            elif (voteCONGRESS > voteBJP and voteCONGRESS > voteAAP and voteCONGRESS > voteOTHERS):
                print("CONGRESS IS THE WINNER")
            elif (voteAAP > voteBJP and voteAAP > voteCONGRESS and voteAAP > voteOTHERS):
                print("AAP IS THE WINNER ")
            elif (voteOTHERS > voteBJP and voteOTHERS > voteCONGRESS and voteOTHERS > voteAAP):
                print("OTHERS IS A WINNER ")
            elif (voteBJP == voteCONGRESS == voteAAP == voteOTHERS):
                print("All election parties got equal votes so elections is tied.")
            elif (voteBJP == voteCONGRESS == voteAAP):
                print("The election is tied between BJP, CONGRESS, and AAP and Others has lost the match ")
            elif (voteBJP == voteCONGRESS):
                if (voteBJP != 0 and voteCONGRESS != 0):
                    print("The elections has been tied between BJP and CONGRESS ")
                elif (voteAAP == voteOTHERS):
                    print("The elections has been tied between AAP and OTHERS ")
            elif (voteBJP == voteAAP):
                if (voteBJP != 0 and voteAAP != 0):
                    print("The elections has been tied between BJP and AAP ")
            elif (voteCONGRESS == voteOTHERS):
                print("The elections has been tied between CONGRESS and OTHERS ")
            elif (voteBJP == voteOTHERS):
                if (voteBJP != 0 and voteOTHERS != 0):
                    print("The elections has been tied between BJP and OTHERS ")
                elif (voteCONGRESS == voteAAP):
                    print("The elections has been tied between CONGRESS and AAP ")
            elif (voteCONGRESS == voteAAP):
                print("The elections has been tied between CONGRESS and AAP ")
            elif (voteCONGRESS == voteOTHERS):
                print("The elections has been tied between CONGRESS and OTHERS ")
            elif (voteAAP == voteOTHERS):
                print("The elections has been tied between AAP and OTHERS ")
            n = 2
        elif (choice2 == 1):
            n = 1
        else:
            print("Enter a valid choice to continue or exit. Two attempts left.")
            choice2 = int(input("To continue, press 1\nTo exit, press 2\n"))
            if (choice2 == 2):
                if (voteBJP > voteCONGRESS and voteBJP > voteAAP and voteBJP > voteCONGRESS and voteBJP > voteOTHERS):
                    print("BJP IS THE WINNER")
                elif (voteCONGRESS > voteBJP and voteCONGRESS > voteAAP and voteCONGRESS > voteOTHERS):
                    print("CONGRESS IS THE WINNER")
                elif (voteAAP > voteBJP and voteAAP > voteCONGRESS and voteAAP > voteOTHERS):
                    print("AAP IS THE WINNER ")
                elif (voteOTHERS > voteBJP and voteOTHERS > voteCONGRESS and voteOTHERS > voteAAP):
                    print("OTHERS IS A WINNER ")
                elif (voteBJP == voteCONGRESS == voteAAP == voteOTHERS):
                    print("All election parties got equal votes so elections is tied.")
                elif (voteBJP == voteCONGRESS == voteAAP):
                    print("The election is tied between BJP, CONGRESS, and AAP and Others has lost the election ")
                elif (voteBJP == voteCONGRESS):
                    if (voteBJP != 0 and voteCONGRESS != 0):
                        print("The elections has been tied between BJP and CONGRESS ")
                    elif (voteAAP == voteOTHERS):
                        print("The elections has been tied between AAP and OTHERS ")
                elif (voteBJP == voteAAP):
                    if (voteBJP != 0 and voteAAP != 0):
                        print("The elections has been tied between BJP and AAP ")
                elif (voteCONGRESS == voteOTHERS):
                    print("The elections has been tied between CONGRESS and OTHERS ")
                elif (voteBJP == voteOTHERS):
                    if (voteBJP != 0 and voteOTHERS != 0):
                        print("The elections has been tied between BJP and OTHERS ")
                    elif (voteCONGRESS == voteAAP):
                        print("The elections has been tied between CONGRESS and AAP ")
                elif (voteCONGRESS == voteAAP):
                    print("The elections has been tied between CONGRESS and AAP ")
                elif (voteCONGRESS == voteOTHERS):
                    print("The elections has been tied between CONGRESS and OTHERS ")
                elif (voteAAP == voteOTHERS):
                    print("The elections has been tied between AAP and OTHERS ")
                n = 2
                break
            elif (choice2 == 1):
                n = 1     
    else:
        print("Age can't be smaller than 18. Please enter a valid age.")
