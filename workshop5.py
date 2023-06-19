import random
"""
#Task1
def guess_random_number(tries, start, stop):
    random_num = random.randint(start, stop)

    while tries != 0:
        print(f"Number of tries left: {tries}")
        guess_num = int(input(f"Guess a number between {start} and {stop}: "))

        if guess_num == random_num:
            print("You gussed the correct number!")
            continue

        elif guess_num > random_num:
            print("Guess Lower!")
            continue

        elif guess_num < random_num:
            print("Guess Higher!")
            continue

    tries -= 1

    print("Sorry, you failed to guess the number.")


#guess_random_number(5, 0, 10)

"""
# task:2 Linear
"""

def guess_random_num_linear(tries, start, stop):
    target_num = random.randint(start, stop)
    print(f"The number for the program to guess is: {target_num}")

    for num in range(start, stop+1):
        print(f"Number of tries left: {tries}")
        rand_num = num  # Each guess is one integer from the potential range

        print(f"The program is guessing.... {rand_num}")

        if rand_num == target_num:
            print("The program has guessed the correct number!")
            return

        tries -= 1

        if tries == 0:
            print("No more tries left. The program couldn't guess the number.")
            return


# Test driver code
guess_random_num_linear(5, 0, 10)

"""

# Task3


def guess_random_num_binary(tries, start, stop):
    target_num = random.randint(start, stop)
    print(f"Random number to find: {target_num}")

    lower_bound = start
    upper_bound = stop

    while tries > 0:
        print(f"Number of tries left: {tries}")
        pivot_val = (lower_bound + upper_bound) // 2

        if pivot_val == target_num:
            print(f"The program has guessed the correct number: {pivot_val}")
            return

        elif pivot_val < target_num:
            print("Guessing Higher!")
            lower_bound = pivot_val + 1

        else:
            print("Guessing Lower!")
            upper_bound = pivot_val - 1

        tries -= 1

    print("No more tries left. The program couldn't guess the number.")


# Test driver code
guess_random_num_binary(5, 0, 100)
