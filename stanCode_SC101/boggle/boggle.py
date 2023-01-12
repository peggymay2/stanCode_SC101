"""
File: boggle.py
Name: 莊敏惠
----------------------------------------
Create a specific size boggle by enter alphabet.
Use recursion to find all words in neighbored each other and exist in dictionary.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# The Boggle Size
SIZE = 4


def main():
	"""
	Ask user to type alphabet in specific format.
	create all position index for all entered alphabet.
	use recursion to find all answer exist in boggle.
	"""
	boggle = {}
	for i in range(1, SIZE+1):
		s = input(f'{i} row of letters: ')
		lst = s.split()
		for j in range(len(lst)):
			if len(lst) != SIZE or len(lst[j]) != 1 or not lst[j].isalpha():
				print('Illegal input')
				exit()
			else:
				boggle[i-1, j] = lst[j].lower()
	start = time.time()
	find_boggle(boggle)
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		lst = []
		for word in f:
			if len(word.strip()) >= SIZE:
				lst.append(word.strip())
		words_set = set(lst)
	return words_set


def update_dictionary(boggle):
	"""
	:param boggle: a dictionary including all position index for all entered alphabet.
	:return: the new dictionary only exist alphabet in boggle.
	"""
	words_set = read_dictionary()
	boggle_word = ""
	new_words = []

	for position in boggle:
		boggle_word += boggle[position]

	for word in words_set:
		count = 0
		if len(word) <= SIZE*SIZE:
			for letter_w in word:
				if letter_w not in boggle_word:
					count += 1
				if count == 0:
					new_words.append(word)
	new_words_set = set(new_words)
	return new_words_set


def find_boggle(boggle):
	word_lst = []
	words_dic = update_dictionary(boggle)
	for position in boggle:
		position_lst = [position]
		current_s = boggle[position]
		find_boggle_helper(boggle, current_s, word_lst, words_dic, position, position_lst)
	print(f'There are {len(word_lst)} words in total')


def find_boggle_helper(boggle, current_s, word_lst, dictionary, position, position_lst):
	# Base Case
	# if has_prefix(current_s, boggle):
	if len(current_s) >= SIZE:
		if current_s in dictionary and current_s not in word_lst:
			print(f'Found "{current_s}"')
			word_lst.append(current_s)
	"""
	"else" is not necessary to separate base case and backtracking 
	because this recursion will be end definitely.
	"""
	# Choose
	for i in range(-1, 2):
		for j in range(-1, 2):
			x = position[0] + i
			y = position[1] + j
			if 0 <= x < SIZE and 0 <= y < SIZE and (x, y) != position:
				if (x, y) not in position_lst:
					current_s += boggle[x, y]
					position_lst.append((x, y))
					# Explore
					find_boggle_helper(boggle, current_s, word_lst, dictionary, (x, y), position_lst)
					# Un-choose
					current_s = current_s[:len(current_s)-1]
					position_lst.remove((x, y))
					position = position_lst[-1]


def has_prefix(sub_s, boggle):
	"""
	:param sub_s: the latest current_s
	:param boggle: a dictionary including all position index for all entered alphabet.
	:return: boolean
	"""
	for word in update_dictionary(boggle):
		prefix = word.startswith(sub_s)
		if prefix:
			return True
	return False


if __name__ == '__main__':
	main()
