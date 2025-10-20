from random import randint

correct_num = randint(1,10)

guess_count = 0 

while True:
    guess = int(input("Pick a number between 1 and 10: "))

    # shortcut to increase a value by one!
    guess_count += 1

    if guess == correct_num:
        print("Correct!")
        break

    elif guess_count == 3:
        print(f"Sorry, you had three guesses! The correct number was {correct_num}")
        break

    elif guess < correct_num:
        print("You guessed too low!")

    elif guess > correct_num:
        print("You guessed too high!")
