# HangmanGame
HANGMAN GAME
KAVYA BORRA
1.	CREATE AND IMPORT IMAGE AND WORD FILE 
To bootstrap Hangman code, we need a word category dictionary and Hangman image to display incorrect guesses.
From hangman_pkg, created hangman image list and words list dictionary which is further imported into main python file.
Prompt user’s selection from Category:
i.	Here, it displays Category Dictionary keys for the user to select a category, it converts the category dictionary into the list. 
list(category.keys())
ii.	Checks if the user’s selection is valid else breaks out from the loop, and prompts the user to enter category selection again.

 
2.	USING RANDOM () CATEGORY:
The user’s selected category is stored in a variable, pass that variable as key in the category dictionary. 
With, the random choice function, pass category [input category] as a parameter and assign it to the variable. 
Note: Category is a dictionary and passes the user’s selection as the key and that user’s key should exist in category 
 chosen_category = random.choice(category[input_category]

3.	VARIABLES [COUNTS] TO KEEP TRACK OF HANGMAN TRIES:
TOTAL_CHANCES = 7 (HANGMAN TRIES)
 WRONG_COUNT = 0 (INCREMENTS WHILE THE WRONG LETTER IS GUESSED
4.	WHEN USER’S INPUT_LETTER, ALREADY EXISTS BLANKS:
i.	If the condition to check the user’s input letter already exists in blanks, then it must break out of that if loop and display a print statement to display the status of blanks. 

 
5.	REPLACE BLANKS WITH GUSSED_LETTER, IF GUSSED RIGHT:
i.	If the condition to check the user’s input letter (input_letter) is in the randomized variable of the category 
ii.	Iterate through the len of randomized variable(input_catergory) 
iii.	Further check if index of input_category == input_letter [User’s guessed]
iv.	Replace, the corresponding blanks with the correct guessed letter.
v.	Here it is divided into three-part, first part retains the substring until the index of input_letter + input_letter+ retains the substring until the end of the index. 
  blanks = blanks[:index] + input_letter + blanks[index + 1:]
6.	INCORRECT GUESS, INCREMENT COUNT OF HANGMAN TRIES:
i.	If the user guess is incorrect, then the total count must decrement (def =7)
ii.	Then for each incorrect guess, hangman_display [wrong_count] must be printed.
<img width="432" alt="image" src="https://github.com/kachow0001/HangmanGame/assets/24617401/7c1e5bf4-6790-44ed-817d-00cc7cbf65e7">
