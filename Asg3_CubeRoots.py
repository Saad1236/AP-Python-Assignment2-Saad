num_guesses: int = 0
guess: float = 0
cube = float(input('Enter number greater than zero to find its cube root: '))

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
                print("low", low, "at", num_guesses + 1)
            else:  # look only in left half search space
                high = guess  # next guess is halfway in search space
                print("high", high, "at", num_guesses + 1)
            guess = (high + low) / 2.0
            print("Guess", guess, "at", num_guesses + 1)
            num_guesses += 1

else:  # For numbers between 0 & +-1 (Assignment requirement)
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
                print("low", low, "at", num_guesses + 1)
            else:  # look only in left half search space
                high = guess
                print("high", high, "at", num_guesses + 1)
            guess = (low + high) / 2.0
            num_guesses += 1

print('Number of guesses=', num_guesses)
print(guess, 'is closet to the cube root of', cube)
