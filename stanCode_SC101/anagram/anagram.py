"""
File: anagram.py
Name: 莊敏惠
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    Searching all anagrams of strings entered by user
    """

    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')

    while True:
        s = input(str('Find anagrams for: '))
        start = time.time()
        if s == EXIT:
            break
        else:
            find_anagrams(s)
            end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm:  {end-start} seconds.')


def read_dictionary():
    words = []
    with open(FILE, "r") as f:
        for line in f:
            word = line.strip()  # Remove line breaks
            words.append(word)
    return words


def update_dictionary(s):
    """
    :param s: the string entered by user
    :return: New dictionary only containing letter s
    """
    words = read_dictionary()

    s_dic = {}
    new_words = []

    for letter in s:
        s_dic[letter] = s.count(letter)

    for word in words:  # update dictionary only containing letter s
        if len(word) == len(s):
            word_dic = {}
            for letter_w in word:
                word_dic[letter_w] = word.count(letter_w)
                if s_dic == word_dic:
                    """
                    if word's letter amount is same as s's letter amount,
                    it can be considered as anagrams of s
                    """
                    new_words.append(word)
                    break
    return new_words


def find_anagrams(s):
    """
    :param s: the string entered by user
    :return: None
    """
    lst = []  # save all anagrams of s as a list
    new_words = update_dictionary(s)
    print('Searching...')
    find_anagrams_helper(s, '', lst, new_words)
    print(f'{len(lst)} anagrams: {lst}')


def find_anagrams_helper(s, current_s, lst, new_words):
    """
    :param s: the string entered by user
    :param current_s: empty string which will be filled with all permutations of s
    :param lst: empty list which will be filled with all anagrams of s
    :param new_words: dictionary only containing letter s
    :return: None
    """
    if has_prefix(current_s, new_words):
        if len(current_s) == len(s):  # Base Case
            if current_s not in lst and current_s in new_words:
                print(f'Found:  {current_s}')
                print('Searching...')
                lst.append(current_s)
        else:
            for letter in s:
                if current_s.count(letter) >= s.count(letter):
                    pass
                else:
                    # Choose
                    current_s += letter
                    # Explore
                    find_anagrams_helper(s, current_s, lst, new_words)
                    # Un-choose
                    current_s = current_s[:len(current_s)-1]


def has_prefix(sub_s, new_words):
    """
    :param sub_s: the part of string that user enter
    :param new_words: a dictionary containing only the letter s
    :return: boolean
    """
    for new_word in new_words:
        prefix = new_word.startswith(sub_s)
        if prefix:
            return True
    return False


if __name__ == '__main__':
    main()
