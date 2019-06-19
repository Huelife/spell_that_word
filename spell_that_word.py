#spell_that_word.py: Simple spelling text game

import csv
from random import randint

#Game class with word and random number variables
class Game():
  def __init__(self):
    self.words_store = []
    self.rand_num = randint(0,16)
    
    with open("words.csv","r") as fin:
      global word_list
      read_data = csv.reader(fin)
      for row in read_data:
        self.words_store += row
           
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
        if user_input == self.words_rand:
          print("Correct!")
          break
        else:
          print("Incorrect!")
          continue
          
start = Game()
start.question()
