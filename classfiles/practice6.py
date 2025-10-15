
secret_number =7

for attempt in range(1,6): # 5 attempts
    guess = input(f"Attempt {attempt}/5: Guess the number(1-10):")

    if not guess.isdigit():
        print("invalid input  please enter a valid number")
        continue  # skips to next attempts
    guess =int(guess)

    if guess == secret_number:
        print("correct1! you guess the correct number")
        break # ext the loop if guessed
    else:
        print("wrong guess")
else:
    print("game over")
    











    
