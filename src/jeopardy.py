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

if options.operation == 'answer':
  # the answer argument
  if len(args) < 3:
    raise ValueError("Usage: ./Jeopardy.py -a Player_id Question_id Choice_id")
  player_id, question_id, choice_id = list(map(int, args))
  print(player_id, question_id, choice_id)
  game.answer(player_id, question_id, choice_id)
elif options.operation == 'start':
  game.reset()
  print("Game reset done.")
elif options.operation == 'select':
  question_id = int(args[0])
  game.select(question_id)
else:
  print("Usage: ./Jeopardy.py -o answer Player_id Question_id Choice_id")

