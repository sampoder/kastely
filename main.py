from random import randint

from ascii import ascii

from start import start

import interface

from roll import roll_dice 

import os

import sys

names = start()

class player_1 :
  name = names[0]
  score = 0

class player_2 :
  name = names[1]
  score = 0

while player_1.score < 25 and player_2.score < 25:

  player_1.score += roll_dice(player_1)

  if player_1.score < 25:

    player_2.score += roll_dice(player_2)

ascii("WINNER")

if player_1.score > player_2.score:

  interface.info_2("Welcome to the castle " + player_1.name+", we're glad you finally made. Now can you do the honors? Chop off "+ player_2.name+ "'s head (actually don't).")

elif player_2.score > player_1.score:

  interface.info_2("Welcome to the castle " + player_2.name+", we're glad you finally made it! Now can you do the honors? Chop off "+ player_1.name+ "'s head (actually don't).")