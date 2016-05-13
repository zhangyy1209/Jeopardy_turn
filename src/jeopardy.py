#!/usr/bin/env python3

from optparse import OptionParser
import sys
from game import *

players = PlayerList( "../json/players.json")
question_list = QuestionList("../json/questions.json")
game = Game(question_list, players, "score", "status")

parser = OptionParser()
parser.add_option("-o", "--operation", dest="operation", default=None ,help="start the Jeopardy game")

(options, args) = parser.parse_args()

if options.operation == 'a':
  # the answer argument
  if len(args) < 3:
    raise ValueError("Usage: ./Jeopardy.py -o a Player_id Question_id Choice")
  player_id, question_id, choice_id = int(args[0]), int(args[1]), ord(args[2]) - ord('a')
  print(player_id, question_id, choice_id)
  game.answer(player_id, question_id, choice_id)
elif options.operation == 'r':
  game.reset()
  print("Game reset done.")
elif options.operation == 's':
  question_id = int(args[0])
  game.select(question_id)
else:
  print("Usage: ./Jeopardy.py -o a Player_id Question_id Choice")

