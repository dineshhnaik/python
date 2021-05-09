# Simple secret game

secret_number = 7
no_of_attempts = 0
max_attempts = 3

while no_of_attempts < max_attempts:
    your_number = int(input("Enter your number between 0 & 10: "))
    no_of_attempts += 1
    if your_number == secret_number:
        guessed_correctly = True
        print("You guessed it right...you won the game!")
        break
else:
    print("You lost the game!")