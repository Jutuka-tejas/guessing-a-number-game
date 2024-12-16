import random
def guess_num():
    print("Welcome to the guessing a number game.....")
    print("I Have a number between 1 and 100 :")
    num=random.randint(1,100)
    # print(num)
    challenge=input("Type 'h' for hard OR 'e' for Easy :")
    if challenge=='h':
        # print("You have 5 attempts to guess the number :\n")
        # guessnum=int(input())
        for i in range(5):
            print(f"You have {5-i} atempts to guess the number .")
            guessnum=int(input("Guess the number :: "))
            if guessnum>100 or guessnum<1:
                print("Guess the number between 1-100 !!")
            if num==guessnum:
                print(f"you won ,the number is :{num}")
                break
            elif guessnum<num:
                print("Too low\nToo High\n")
            elif guessnum>num:
                print("Too High\nToo low")
        if guessnum!=num:
            print(f"You lost the game. The number is {num}")
    elif challenge=='e':
        # print("You have 10 attempts to guess the number ")
        for _ in range(10):
            print(f"You have {10-i} atempts to guess the number .")
            guessnum=int(input("Guess the number :: "))
            if guessnum>100 or guessnum<1:
                print("Guess the number between 1-100 !!")
            if num==guessnum:
                print(f"You won ,the number is :{num}")
                break
            elif guessnum<num:
                print("Too low\nToo High\n")
            elif guessnum>num:
                print("Too High\nToo low")
        if guessnum!=num:
            print(f"You lost the game. The number is {num}")
    else:
        print("enter corrrect choice!!  ")
guess_num()
    
