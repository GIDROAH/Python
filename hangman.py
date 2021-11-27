import random 
import string
from words import words

# for choosing valid word
def get_valid_word(words):
	# for keep chosing wird from list
	word = random.choice(words)
	# will keep chose if dash or spaces in words 
	while "-" in word or " " in word:
		word = random.choice(words)
	#return is upper cases
	return word.upper()
	
'''we need to keep track a of what letter we gessed or what we gessed currectly we also need what is valid letter or what is it so that we can show the user what was right word'''
def hangman():
	word = get_valid_word(words)
	# tracking ussed letter in set format
	word_letter = set(word)
	alphabet = set(string.ascii_uppercase)
	# what the letter user gessed
	used_letter = set()
	# lives point
	lives = 6
	# taking user input
	while len(word_letter) > 0 and lives > 0:
		# letter we have used
		print("You have", lives, "left and You have used these letter ", " ".join(used_letter))
		# what current ward is (ie W - R D)
		word_list = [letter if letter in used_letter else "-" for letter in word]
		print("Current word is", " ".join(word_list))
		user_letter = input("Guess somthing : ").upper()
		if user_letter in alphabet - used_letter:
			used_letter.add(user_letter)
			if user_letter in word_letter:
				word_letter.remove(user_letter)
			else:
				lives = lives - 1  # take 1 life away
				
		elif user_letter in used_letter:
			print("You have already used that character. Please try again ")
		else:
			print("Inavlid character. Please try again!")
	# user gets here when len(word_list) == 0 or lives == 0
	if lives == 0:
		print("You died, sorry. The word was", word)
	else:
		print("You gessed the word", word, '!!')
hangman()