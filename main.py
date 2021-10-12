import random
random_number = random.randint(0,10)
guesses_taken = 0
name = input("What is your name? ")
play = input("Hello " + name + " would you like to play a game? (Y or N) ")


if play == ("Y"):
    print("Okay, lets get started. I am thinking of a number between 1 and 10. Guess what it is! ")
    guess = input()
    guess = int(guess)
else:
    print("Alright lets play later!")


if guess < random_number:
    print("You were too low, maybe next time kid!")
if guess > random_number:
    print("You were too high, maybe you won't suck next time ya loser!")
if guess == random_number:
    print("You got it! You're a lot smarter than I thought! ")






