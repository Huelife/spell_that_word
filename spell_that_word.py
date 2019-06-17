#spell_that_word.py: Simple spelling text game

import re
from random import randint

words_store = ["cat","dog","mouse","bird","human","wolf"]
rand_num = randint(0,5)
words_rand = words_store[rand_num]

print(words_rand)

user_input = input("Type the word you see! ")

if re.match(words_rand, user_input):
  print("Correct!")
else:
  print("Incorrect!")
