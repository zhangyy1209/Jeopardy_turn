from game import *

players = PlayerList( "../json/players.json")
question_list = QuestionList("../json/questions.json")
# game = Game(question_list, players)
# print("Game started!")

# print("Please input player_id and question_id below:")
# readin = input()
# player_id, question_id = re.findall("[\w']+", readin)
# # player id and question id should be an int.
# player_id, question_id = int(player_id), int(question_id)
# print(player_id, question_id)

# print("Please input choice Player %s: %s answered below" % (player_current.id, player_current.name))
# readin = input()
# choice_id = re.findall("[\w']+", readin)

# print(choice_id)
# if not game.answer(player_id, question_id, choice_id):
#   print("Wrong answer. Time to buzz.")
#   print("Please input player_id and choice_id:")
#   readin = input()
#   player_id, choice_id = re.findall("[\w']+", readin)
#   player_id, choice_id = int(player_id), int(choice_id)
#   game.answer(player_id, question_id, choice_id)

