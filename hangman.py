_BLUE = '\033[96m'
_RED = '\033[91m'
_END = '\033[0m'

QUIZ = "cat"

hangman = [
	"__________         ",
	"|        |         ",
	"|        o         ",
	"|       /|\        ",
	"|       / \        ",
	"|                  ",
]

quiz_letters = list(QUIZ)
possible_answers_count = len(QUIZ)
arrowble_incorrect_count = possible_answers_count

win = False
incorrect_count = 0
board = ["_"] * len(QUIZ)

# Game Start
while incorrect_count < possible_answers_count:
	if "_" not in board:
		win = True
		break
	
	print("Quiz: ", " ".join(board))
	print("Remaing Count:", arrowble_incorrect_count)
	answer = input("Please enter an answer: ")

	# Correct
	if answer in quiz_letters:
		correct_index = quiz_letters.index(answer)
		board[correct_index] = answer
		quiz_letters[correct_index] = "$"
		print(_BLUE + "Currect!" + _END)
	#  Wrong
	else:
		incorrect_count += 1
		arrowble_incorrect_count -= 1
		print(_RED + "Wrong..." + _END)

# Win
if win:
	print("You are winner.")
	print("Answer:", QUIZ)
# Lose
else:
	print("You are loser.")
	print("\n".join(hangman))
