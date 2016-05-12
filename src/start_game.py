import sys
import re
from game import *

players = PlayerList( "../json/players.json")
question_list = QuestionList("../json/questions.json")
print("Game started!")

print("Please input player_id and question_id below:")
readin = input()
player_id, question_id = re.findall("[\w']+", readin)
# player id and question id should be an int.
player_id, question_id = int(player_id), int(question_id)
player_current = players.find(player_id)

print("Please input choice %s %s answered below" % (player_current.id, player_current.name))
readin = input()
choice_id = int(re.findall("[\w']+", readin))
player_current.answer(question_id, choice_id)
