#spell_that_word.py: Simple spelling text game

import re
from random import randint

#word and random number variables
words_store = ["cat","dog","mouse","bird","human","wolf"]
rand_num = randint(0,5)
words_rand = words_store[rand_num]

#loop continues until user input matches printed word
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
