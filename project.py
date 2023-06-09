import random
import time
n = int(input("enter the range you want to play:"))
number = random.randint(1, n)


def intro():
    print("May I ask you for your name?")
    name = input()
    print(name + ", we are happy to play a game with you. I am thinking of a number between 1 and 200")
    time.sleep(.5)
    print("Go ahead. Guess!")


def pick():
    guessesTaken = 0
    while guessesTaken < 6:
        time.sleep(.25)
        enter = input("Guess: ")
        try:
            guess = int(enter)

            if guess <= n and guess >= 1:
                guessesTaken = guessesTaken + 1
                if guessesTaken < 6:
                    if guess < number:
                        print("The guess of the number that you have entered is too low")
                    if guess > number:
                        print("The guess of the number that you have entered is too high")
                    if guess != number:
                        time.sleep(.5)
                        print("Try Again!")
                if guess == number:
                    break
            if guess > n or guess < 1:
                print("Silly Goose! That number isn't in the range!")
                time.sleep(.25)
                print("Please enter a number between 1 and 200")

        except:
            print("I don't think that " + enter + " is a number. Sorry")

    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job, You guessed my number in ' + guessesTaken + ' guesses!')

    if guess != number:
        print('Nope. The number I was thinking of was ' + str(number))


playagain = "yes"
while playagain == "yes" or playagain == "y" or playagain == "Yes":
    intro()
    pick()
    print("Do you want to play again?")
    playagain = input()
