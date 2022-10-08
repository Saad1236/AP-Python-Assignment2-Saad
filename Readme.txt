For this assignment I had to add for two sets of number:
1)	Cube< -1
In the part where abs(cube) is greater than 1 I added the part where cube is less than 0(i.e. for negative numbers less than -1.   
2)	-1< Cube<1 
In this part I have to write a separate code based on the same logic where the limit of Bisection Search is between -1 and 1. It will run for the cube values that lie between 1 and -1.

****Code***

cube = float(input('Enter number to find its cube root: '))
if abs(cube) > 1:
    epsilon = 0.01
    num_guesses = 0
    print("Iteration:", num_guesses)
    low = 0
    high = cube
    print("high", high)
    guess = (high + low) / 2.0
    print("Guess", guess)
    while abs(guess ** 3 - cube) >= epsilon:
        print("Iteration:", num_guesses+1)
        if cube > 0:
            # For Numbers greater than 1
            if guess ** 3 < cube:
                # look only in right half search space
                low = guess
                print("low", low)
            else:
                # look only in left half search space
                high = guess  # next guess is halfway in search space
                print("high", high)
            guess = (high + low) / 2.0
            print("Guess", guess)
            num_guesses += 1
        else:
            # For Number less than -1
            if guess ** 3 > cube:
                low = guess
                print("low", low)
            else:
                high = guess
                print("high", high)
            guess = (low + high) / 2.0
            print("guess", guess)
            num_guesses += 1

if abs(cube) < 1:
    # For numbers between 0 & +-1
    num_guesses = 0
    print("Iteration:", num_guesses)
    epsilon = 0.01
    low = cube
    high = 1
    print("high", high)
    guess = (high + low) / 2.0
    print("guess", guess)
    while abs(abs(guess) ** 3 - abs(cube)) >= epsilon:
        print("Iteration:", num_guesses+1)
        if cube > 0:
            if guess ** 3 < cube:
                low = guess
                print("low", low)
            else:
                high = guess
                print("high", high)
            guess = (low + high) / 2.0
            num_guesses += 1
            print("Iteration:", num_guesses)
        else:
            low = -1
            high = cube
            if guess ** 3 > cube:
                high = guess
                print("high", high)
            else:
                low = guess
                print("low", low)
            guess = (low + high) / 2.0
            num_guesses += 1
            print("Iteration:", num_guesses)

print('Number of guesses=', num_guesses)
print(guess, 'is closet to the cube root of', cube)
