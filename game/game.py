import platform
import re
from os import path,system

SCORE = 0
HIGH_SCORE = 0

def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

# Clear the Screen based on the users operating system
def clear():
	if platform.system() == "Windows":
		system('cls')
	else:
		system('clear')

# Add a word recursive function
def add_word(score, high_score, error=""):
	clear()

	# Prints error then prompts user for a word
	score_string = "Score: " + str(score) + "        High Score: " + str(high_score) + "\n\n"
	word = input(score_string + error + "Enter a Word: ")

	# Resets the error
	if error != "":
		error = ""

	# Create the file if it doesn't exist
	if path.exists("words.txt") == False:
		open("words.txt", "w").close()

	# Sets the error if the  user enters a blank string or multiple words
	if re.search('[a-zA-Z]', word) == None or len(word.split()) > 1:
		error = "Please Enter a Single Word\n"
		score = 0
	else:
		# Checks if the word already exists
		if findWholeWord(word)(open("words.txt", "r").read()):
			error = "Word Already Exists In List\n"
			score = 0
		else:
			open('words.txt', 'a').write(word + "\n")
			score = score + 1

	if score > high_score:
		high_score = score

	add_word(score, high_score, error)

if __name__ == "__main__":
	add_word(SCORE, HIGH_SCORE)
