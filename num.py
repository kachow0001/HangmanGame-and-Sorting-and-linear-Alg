import random


def guess_random_num_binary(tries, start, stop):
    target_num = random.randint(start, stop)
    print(f"Random number to find: {target_num}")

    left = start
    right = stop

    while tries > 0:
        print(f"Number of tries left: {tries}")
        mid = (left + right) // 2

        if mid == target_num:
            print(f"The program has guessed the correct number: {mid}")
            return

        elif mid < target_num:
            print("Guessing Higher!")
            left = mid + 1

        else:
            print("Guessing Lower!")
            right = mid - 1

        tries -= 1

    print("No more tries left. The program couldn't guess the number.")


# Test driver code
guess_random_num_binary(5, 0, 100)
