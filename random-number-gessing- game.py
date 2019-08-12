import random
def main():
    answer = random.randint(1,100)
    print("Welcome to the random number guessing game!")
    print("You have 6 tries to guess the mistery number.")
    tries = 6
    while (tries>0):
        guess = int(input("Guess a number between 1 and 100: "))
        if (answer == guess):
            print("YOU WIN! Have a cookie.")
            break
        elif (guess>answer):
            print("guess is too big")
            tries = tries - 1
        else 
            print("guess is too small")
            
    if (tries==0)
        print("you lose")
        
if __name__ == "__main__":
    main()