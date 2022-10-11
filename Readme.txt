APP Assignment Number 2
Title: Python Code for Cube Root of Numbers between 0 and 1
Name: Saad Ali Babar
Reg. No.: 402049
======
Description:
For this assignment I have added (in the already given) code for two sets of numbers:
1)	-1 < Cube<1 
In this part I have to write a separate code based on the same logic where the limit of Bisection Search is between -1 and 1. It will run for the cube values that lie between 1 and -1.
In this part the main assignment question is addressed i.e. code for cube root of numbers between 0 and 1. For this the (nested) if condition: cube > 0 is incorporated which will check the cube root of numbers between 0 and 1, as the main if condition:  abs(cube) < 1 will filter the input number values to only between -1 and 1. 
2)	Cube=x < -1
In the part where abs(cube) is greater than 1, I appended the part where absolute of cube is less than 0 (i.e. for negative numbers less than -1).   
=====
# ***Code***

num_guesses: int = 0
guess: float = 0
cube = float(input('Enter number to find its cube root: '))

if abs(cube) > 1:
    epsilon = 0.01
    num_guesses = 0
    low = 0
    high = cube
    print("high", high, "at", num_guesses)
    guess = (high + low) / 2.0
    print("Guess", guess, "at", num_guesses)
    while abs(guess ** 3 - cube) >= epsilon:
        if cube > 0:  # For Numbers greater than 1
            if guess ** 3 < cube:  # look only in right half search space
                low = guess
                print("low", low, "at", num_guesses+1)
            else:  # look only in left half search space
                high = guess  # next guess is halfway in search space
                print("high", high, "at", num_guesses+1)
            guess = (high + low) / 2.0
            print("Guess", guess, "at", num_guesses+1)
            num_guesses += 1
        else:    # For Number less than -1
            if guess ** 3 > cube:  # look only in right half search space
                low = guess
                print("low", low, "at", num_guesses+1)
            else:  # look only in left half search space
                high = guess
                print("high", high, "at", num_guesses+1)
            guess = (low + high) / 2.0
            print("guess", guess, "at", num_guesses+1)
            num_guesses += 1

if abs(cube) < 1:     # For numbers between 0 & +-1
    num_guesses = 0
    epsilon = 0.01
    low = cube
    high = 1
    print("high", high, "at", num_guesses)
    guess = (high + low) / 2.0
    print("guess", guess, "at", num_guesses)
    while abs(abs(guess) ** 3 - abs(cube)) >= epsilon:
        if cube > 0:  # For numbers between 0 & +1
            if guess ** 3 < cube:  # look only in right half search space
                low = guess
                print("low", low, "at", num_guesses+1)
            else:  # look only in left half search space
                high = guess
                print("high", high, "at", num_guesses+1)
            guess = (low + high) / 2.0
            num_guesses += 1
        else:  # For numbers between -1 & 0
            low = -1
            high = cube
            if guess ** 3 > cube:  # look only in right half search space
                high = guess
                print("high", high, "at", num_guesses+1)
            else:  # look only in left half search space
                low = guess
                print("low", low, "at", num_guesses+1)
            guess = (low + high) / 2.0
            num_guesses += 1


print('Number of guesses=', num_guesses)
print(guess, 'is closet to the cube root of', cube)

