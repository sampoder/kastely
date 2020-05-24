from random import randint

import random

import interface

from ascii import ascii

import time

import sys

def load():

    sys.stdout.write('\rloading |')
    time.sleep(0.1)
    sys.stdout.write('\rloading /')
    time.sleep(0.1)
    sys.stdout.write('\rloading -')
    time.sleep(0.1)
    sys.stdout.write('\rloading \\')
    time.sleep(0.1)
    sys.stdout.write('\rloading |')
    time.sleep(0.1)
    sys.stdout.write('\rloading /')
    time.sleep(0.1)
    sys.stdout.write('\rloading -')
    time.sleep(0.1)
    sys.stdout.write('\rloading \\')
    time.sleep(0.1)
    sys.stdout.write('\rloading |')
    time.sleep(0.1)
    sys.stdout.write('\rloading /')
    time.sleep(0.1)
    sys.stdout.write('\rloading -')
    time.sleep(0.1)
    sys.stdout.write('\rloading \\')
    time.sleep(0.1)
    sys.stdout.write('\r')

def roll_dice(roller):

  time.sleep(2)

  interface.info_2(roller.name + " will now roll the dice. Press enter to roll.")

  interface.wait_key()

  load()

  luck = randint(1, 6)

  score = randint(1, 6)

  if luck != 1:

    if score <= 2:

      messages = ["RIP.", "Unluckly my friend.", "Wow, how rude of the die.", "Yikes.", "That die is one annoying die.", "You're not going to make it at this rate.", "The snail is catching up!", "That's got to hurt."]

    elif score <= 4:

      messages = ["Not fast not slow.", "Meh.", "Not much to say.", "I guess it's kinda good.", "Not so breaking news.", "Nothing to say here.", "Let's get some actual action going, ok?"]

    elif score <= 6:

      messages = ["Hooray!", "You'll be at the castle in no time!", "Keep up this speed!", "Breaking news!", "Amazing!", "Awesome!", "Wait what? How'd you do that.", "Let's go!", "To the castle and beyond!"]

    interface.info_2(random.choice(messages) + " You rolled at "+ str(score) + ". You're now " + str(25 - roller.score - score) + " kilometers away from the castle.")

  else:

    mystery = randint(0, 10)

  

    if randint(1,2) == 1:

      score = mystery * -1

    else:

      if 25 - roller.score <= mystery:

        score = 25 - roller.score

      score = mystery

      

    ascii("MYSTERY")

    interface.info_2(roller.name + " it seems you've landed on a mystery spot, let's find out what'll happen?")

    interface.wait_key()

    load()

    if score <= 0:

      messages = ["A big troll has arrived, you ran.", "The bridge has broken, yikes.", "You're starving.", "Someone just stole your wallet.", "Massive loss, your sword is broken.", "That's got to hurt, a tree has fallen."]


    elif score <= 3:

      messages = ["You hit a swamp, but you made it through.", "There's a fallen tree, but you've climbed over.", "Not so breaking news.", "Nothing to say here.", "Booorrring"]

    elif score <= 8:

      messages = ["You've got energy boost from some food!", "You found a shortcut, nice job", "Ohhh... it's a shortcut!", "A nice new pair of boots has got you speeding ahead."]

    elif score <= 10:

      messages = ["Hooray! You've got ultra lucky here and found a horse to rid on.", "The flying dragon has given you a ride, you'll be at the castle in no time!", "Your fellow knights have given you a ride,keep up this speed! I am wish I had your luck.", "Breaking news! You've got super lucky and teleported forward!"]

    interface.info_2(random.choice(messages) + " You're going to be moving "+ str(score) + " places. You're now " + str(25 - roller.score - score) + " kilometers away from the castle.")

  return score


