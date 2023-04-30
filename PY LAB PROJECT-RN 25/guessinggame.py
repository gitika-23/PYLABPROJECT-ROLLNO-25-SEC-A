from random import randint

print("(: Welcome to the Guesstum World :)")
name =input("enter your name: ")

# Get the lower and upper limits
a = int(input("Enter the lower limit: "))
b = int(input("Enter the higher limit: "))

# Initialize variables for attempts and score
attempts = 3
c=0

# Generate a random number between the limits
number = randint(a, b)

# Start the game loop
while attempts > 0:
    # Get the user's guess
    guess = int(input("Enter your guess: "))

    # Check if the guess is correct
    if guess == number:
        # Increase the score by 10 and break out of the loop
        print("Congratulations! You guessed the number.")
        break
    else:
        # Decrement the number of attempts and provide a hint
        attempts -= 1
        c=c+1
        if guess > number:
            print("Too high.")
        else:
            print("Too low.")
        print(f"You have {attempts} attempts remaining.")
score=10*(3-c)
# Check if the user ran out of attempts
if attempts == 0:
    print(f"Sorry, you ran out of attempts. The number was {number}.")
print(f"{name} your score is  out of 30: {score}")