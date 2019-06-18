#spell_that_word.py: Simple spelling text game

import re
from random import randint

#Game class with word and random number variables
class Game():
  def __init__(self):
    self.words_store = ["cat","dog","mouse","bird","human","wolf"]
    self.rand_num = randint(0,5)
    self.words_rand = self.words_store[self.rand_num]
  
  #loop continues until user input matches printed word
  def question(self):
    while True:
      try:
        print(self.words_rand)
        user_input = input("Type the word you see! ").lower()
      except ValueError:
        print("Error!")
        continue
      else:
        if re.match(self.words_rand,user_input):
          print("Correct!")
          break
        else:
          print("Incorrect!")
          continue
          
start = Game()
start.question()
