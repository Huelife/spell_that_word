#spell_that_word.py: Simple spelling text game

from random import randint

words_store = ["cat","dog","mouse","bird","human","wolf"]
rand_num = randint(0,5)

words_rand = words_store[rand_num]

user_input = input("Type the word you see! ")
