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


songs = "West End Girls, Always on my mind, Go West, Domino Dancing, Suburbia, Rent, Heart, Being Boring, The Dictator Decides, You Choose, Discoteca, I want a dog, This must be the place I waited years to leave, Vulnerable, Flamboyant, Love etc, Hit and miss"
songs = [x.strip() for x in songs.split(',')]

def get_random_song(songlist):
	song_index = random.randint(0,len(songlist)-1)
	return songlist[song_index]

answer = get_random_song(songs).lower()
progress = []
wrong_guesses = 0
letters_guessed = ""

for a in answer:
	if a == " ":
		progress.append(" ")
	else:
		progress.append("-")

def display_board(wrong_guesses, letters_guessed):
	print HANGMANPIX[wrong_guesses]
	print
	print "SONG TITLE: {}".format("".join(progress))
	print
	print "Letters guessed so far: {}".format(letters_guessed)

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
	print "Hello and welcome to hangman - Pet Shop Boys edition!"
	time.sleep(0.5)
	print "Try to find the song title I'm thinking of, or else a man will DIE."
	time.sleep(0.5)
	print 
	print ("DISCLAIMER: No men were harmed in the making of this game.")
	print 
	time.sleep(0.5)
	main_game(wrong_guesses, letters_guessed)


def main_game(wrong_guesses, letters_guessed):
	while wrong_guesses < 6:
		if answer == "".join(progress):
			print "YOU WON!! HURRAH!"
			break
		else:
			print 
			letter_guess = raw_input("Guess a letter: ")
			letter_guess = letter_guess.lower()
			if letter_guess in letters_guessed:
				print "You have already guessed that letter. Guess again."
			elif len(letter_guess) != 1:
				print "Please enter a single letter."
			elif letter_guess not in 'abcdefghijklmnopqrstuvwxyz':
				print'That was not a LETTER, guess again.'
			elif letter_guess in answer:
				print "YUP!\n{} is in the song title I'm thinking of.".format(letter_guess)
				letter_position = [pos for pos, char in enumerate(answer) if char == letter_guess]
				for position in letter_position:
					progress[position] = letter_guess
				letters_guessed += "{}, ".format(letter_guess)
				display_board(wrong_guesses,letters_guessed)
			else:
				print  "*ANGRY BEEP*\n{} is NOT in the song title I'm thinking of.".format(letter_guess)
				wrong_guesses += 1
				letters_guessed += "{}, ".format(letter_guess)
				display_board(wrong_guesses,letters_guessed)

	if wrong_guesses == 6:
		print "GAME OVER - YOU LOSE :("

start_game()