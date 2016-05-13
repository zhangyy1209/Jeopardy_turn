import sys
from game import *

players = PlayerList( "../json/players.json")
question_list = QuestionList("../json/questions.json")
game = Game(question_list, players, "score", "status")

readin = sys.argv[1:]
print(readin)
player_id, question_id, choice_id = list(map(int, readin))
game.answer(player_id, question_id, choice_id)
