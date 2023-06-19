import random
from hangman_pkg.image import hangman_display
from hangman_pkg.words_lst import category

total_chances = 7
wrong_count = 0

print("_____________Welcome to Hangman game!_______________\n")
print(f"Select the Category from following list: {list(category.keys())}")

# Taking desired category from user and converting to lowercase
while True:
    input_category = input(
        "Enter the desired Category from the above list: ").lower()
    if input_category not in category:
        print("Invalid selection. Please select from the list displayed above.")
    else:
        break

# Randomizing category list based on the user's selected category
chosen_category = random.choice(category[input_category])

# Generating the initial blanks for the chosen word
blanks = "_" * len(chosen_category)
print(blanks, "Here is the WORD to guess!")

while True:
    input_letter = input("Enter a letter to guess: ").lower()

    # Checking if the guessed letter is already in the blanks
    if input_letter in blanks:
        print("You have already guessed that letter. Try again.")
        continue

    if input_letter in chosen_category:
        for index in range(len(chosen_category)):
            if chosen_category[index] == input_letter:
                # Replacing the corresponding blanks with the correct guessed letter
                blanks = blanks[:index] + input_letter + blanks[index + 1:]

        if blanks == chosen_category:
            print("Bravo! You Won!")
            break

    else:
        total_chances -= 1
        print("Incorrect guess.")
        print(hangman_display[wrong_count])
        wrong_count += 1
        print("The remaining chances are:", total_chances)

        if total_chances == 0:
            print("Game over! You ran out of chances.")
            break

    print("Current progress:", blanks)

print("The word was:", chosen_category)
