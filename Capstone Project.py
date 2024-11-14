import random
x = random.randint(1,10)
print("Welcome to the Number Game! You have to guess a random number between 1-10!")

def game():
    turn=0
    while True:
        turn= turn+1
        guess = int(input("Enter a Number!:"))
        if guess < x:
            print("Your Number is lower than mine.")
        elif guess > x:
            print("Your number is higher than mine.")
        else:
            print("You got my number right!")
            print("Number of Attempts it took you to Guess my Number!", turn)
            break
game()
choice=input("Do you want to continue or restart the game yes/no?:")
if choice.lower()=="yes":
    x = random.randint(1,10)
    game()
else:
    print("Thank you for playing the Number Game!")