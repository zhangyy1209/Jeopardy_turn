#!/usr/bin/env python3

# from optparse import OptionParser
import sys
from game import *

players = PlayerList( "../json/players.json")
question_list = QuestionList("../json/questions.json")
game = Game(question_list, players, "score", "status", "answered_id")

option = sys.argv[1]
args = sys.argv[2:]
print(option, args, len(args))

if option == 'a':
  # the answer argument
  if len(args) < 3:
    raise ValueError("Usage: ./Jeopardy.py a Player_id Question_id Choice")
  question_id = (ord(args[1][0]) - ord('a')) * 5 + int(args[1][1])
  player_id, choice_id = int(args[0]), ord(args[2]) - ord('a')
  print(player_id, question_id, choice_id)
  game.answer(player_id, question_id, choice_id)
elif option == 'r':
  game.reset()
  print("Game reset done.")
elif option == 's':
  # question_id = int(args[0])
  question_id = (ord(args[0][0]) - ord('a')) * 5 + int(args[0][1])
  game.select(question_id)
else:
  print("Usage: ./Jeopardy.py a Player_id Question_id Choice")

