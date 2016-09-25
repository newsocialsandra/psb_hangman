import time
import random

HANGMANPIX = [""" ""","""
------------
|         |""","""

------------
|         |         
|          O""","""

------------
|         | 
|          O 
|         / ""","""

------------
|         | 
|          O 
|         / |""","""

------------
|         | 
|          O 
|         / | 
|          | ""","""

------------
|         |
|          O 
|         / |
|          |
|         / | 
|
|            """]


songs = "Being Boring, The Dictator Decides, You Choose, I'm not scared, Discoteca, I want a dog, This must be the place I waited years to leave, Vulnerable, Flamboyant, Love etc, Hit and miss"
print [x.strip() for x in songs.split(',')]

# Replace this with function to give a random answer:
answer = "Being boring".lower()
progress = []
wrong_guesses = 0
letters_guessed = ""

for a in answer:
	if a == " ":
		progress.append(" ")
	else:
		progress.append("-")

def start_game():
	print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	time.sleep(0.5)
	print ("~~~~~~~~~~~~~~~~~*INTRO TO WEST END GIRLS PLAYING*~~~~~~~~~~~~~~~~")
	time.sleep(0.5)
	print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	time.sleep(0.5)
	print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~HANGMAN~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	time.sleep(0.5)
	print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	time.sleep(0.5)
	print 
	print "Hello and welcome to hangman - Pet Shop Boys edition!!!!"
	time.sleep(0.5)
	print "Try to find the song title I'm thinking of, or else a man will DIE!"
	time.sleep(0.5)
	print 
	print ("DISCLAIMER: No men has been hurt in the making of this game.")
	print 
	time.sleep(0.5)
	game(wrong_guesses, letters_guessed)

def displayBoard(wrong_guesses, letters_guessed):
	print HANGMANPIX[wrong_guesses]
	print
	print "SONG TITLE: " + "".join(progress)
	print
	print "Letters guessed so far: {}".format(letters_guessed)


def game(wrong_guesses, letters_guessed):
	print "SONG TITLE: " + "".join(progress)
	print 

	while wrong_guesses < 6:
		if answer == "".join(progress):
			print "YOU WON!! HURRAH!"
			break
		else:
			print 
			letter_guess = raw_input("Guess a letter: ")
			letters_guessed += "{}, ".format(letter_guess)

			if letter_guess in answer:
				print "YUP!\n{} is in the song title I'm thinking of.".format(letter_guess)
				letter_position = [pos for pos, char in enumerate(answer) if char == letter_guess]
				for position in letter_position:
					progress[position] = letter_guess
				displayBoard(wrong_guesses,letters_guessed)
			else:
				print  "*ANGRY BEEP*\n{} is NOT in the song title I'm thinking of.".format(letter_guess)
				wrong_guesses += 1
				displayBoard(wrong_guesses,letters_guessed)

	if wrong_guesses == 6:
		print "GAME OVER - YOU LOSE :("

start_game()