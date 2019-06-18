#spell_that_word.py: Simple spelling text game

import re
from random import randint

words_store = ["cat","dog","mouse","bird","human","wolf"]
rand_num = randint(0,5)
words_rand = words_store[rand_num]

while True:
  try:
    print(words_rand)
    user_input = input("Type the word you see! ")
  except ValueError:
    print("Error!")
    continue
  else:
    if re.match(words_rand, user_input):
      print("Correct!")
      break
    else:
      print("Incorrect!")
      continue
