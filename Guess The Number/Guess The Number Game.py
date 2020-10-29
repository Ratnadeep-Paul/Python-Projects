import random
def guess_number():
    print("Welcome To The Number Guessing Game")
    print("You Have 10 Chances To Guess The Number.. (The Number is between 1-50)")
    print("Enter Your First Guess For The Number")
    guesses = 0
    gnum = random.randint(1, 50)
    finpu = int(input(":-"))

    while finpu != gnum and guesses < 10:           
        if finpu > gnum:
            guesses += 1
            print("Wrong!!! You Selected A Bigger Number")
            print(f"{10 - guesses} Chances Left")
            print("\nEnter A New Number")
            finpu = int(input(":-"))
        
        elif finpu < gnum:
            guesses += 1
            print("Wrong!!! You Selected A Smaller Number")
            print(f"{10 - guesses} Chances Left")
            print("\nEnter A New Number")
            finpu = int(input(":-"))

    if guesses > 10:
        print("Sorry, you had too many guesses")
        print(f'The number was {gnum}')
        
    elif finpu == gnum:
        print("\nCongratulations!! You Win The Game")
        print("Thanks For Playing This Game")
        print("\nDo you Want to play it again??\n     Play--1 , Exit--2")
        more = int(input(":-"))
        if more==1:
            print(guess_number())
        else:
            print("Exiting....")
            exit()
                
print(guess_number())
