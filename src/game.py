import json
import pickle
import os.path

class Game():
  def __init__(self, question_list, player_list, score_file, request_file):
    self.question_list = question_list
    self.player_list = player_list
    self.score_file = score_file
    self.request_file = request_file


  def reset(self):
    self.question_list.reset()
    self.player_list.reset()


  def answer(self, player_id, question_id, choice_id):
    print(self.question_list.questions.items())
    player = self.player_list.players[player_id]
    question = self.question_list.questions[question_id]

    question.state = 1

    if question.aid == choice_id:
      player.update_score(question.score)
      question.state = 2
      str_output = "%d %d Home" % (question.qid, 1)
      self.output_score()
      self.output_request(str_output)
    else:
      player.update_score(-question.score)
      self.output_score()
      str_output = "%d %d" % (question.qid, 0)
      self.output_request(str_output)

    self.player_list.dump_player_pickle()


  def output_score(self):
    scores = [p.score for p in self.player_list.players.values()]
    str_scores = "%d %d %d %d" % tuple(scores)
    with open("../status/" + self.score_file, "w") as output:
      output.write(str_scores)


  def output_request(self, str_output):
    with open("../status/" + self.request_file, "w") as output:
      output.write(str_output)


  def select(self, question_id):
    str_output = str(question_id)
    self.output_request(str_output)


class Question():
  def __init__(self, qid, aid, score, state=0):
    """
    Question class:
      qid: question id, int
      aid: answer id, int
      score: int
      state: int, 0: initial, 1: in answer, 2: finished
    """

    self.qid = qid
    self.aid = aid
    self.score = score
    self.state = state


  def reset(self):
    """
    Reset a question.
    """

    self.state = 0


  def update_choice_state(self, choice_id):
    """
    Update the choice state of a question.
    """

    pass



class QuestionList():
  def __init__(self, question_file):
    """
    questions as a dict of question objects.
    """
    self.questions = {}
    self.question_file = question_file
    self.pkl_file = "question_list.pkl"
    
    if os.path.isfile("../pickle/" + self.pkl_file):
      self.load_questions_pickle()
    else:
      self.load_questions_initial()


  def load_questions_initial(self):
    """
    Load questions.
    """
    with open(self.question_file) as input_file:
      questions = json.load(input_file)

    for q in questions:
      self.questions[q['id']] = Question(qid=q['id'], aid=q['answer'], score=q['score'], state=q['state'])

    print("Questions loaded.")


  def load_questions_pickle(self):
    with open("../pickle/" + self.pkl_file, "rb") as input_file:
      self.questions = pickle.load(input_file)


  def dump_questions_pickle(self):
    with open("../pickle/" + self.pkl_file, "wb") as output_file:
      pickle.dump(self.questions, output_file, pickle.HIGHEST_PROTOCOL)


  def reset(self):
    """
    Write updated questions to file.
    """
    
    for q in self.questions.values():
      q.reset()

    self.dump_questions_pickle()


class Player():
  def __init__(self, id, name=None, score=0):
    """
    Player class:
      id: player id, int
      name: string
      score: int
    """

    self.id = id
    self.name = name
    self.score = score


  def reset(self):
    self.score = 0


  def update_score(self, score):
    self.score += score


class PlayerList():
  def __init__(self, player_file, n_player=4):
    """
    player list
    """
    self.players = {}
    self.n_player = n_player
    self.player_file = player_file
    self.pkl_file = "player_list.pkl"
    
    if os.path.isfile("../pickle/" + self.pkl_file):
      self.load_players_pickle()
    else:
      self.load_players_initial()


  def load_players_initial(self):
    with open(self.player_file) as input_file:
      players = json.load(input_file)
    
    for p in players:
      self.players[p['uid']] = Player(id = p['uid'], name = p['name'], score = p['score'])

    print("Players loaded.")


  def load_players_pickle(self):
    with open("../pickle/" + self.pkl_file, "rb") as input_file:
      self.players = pickle.load(input_file)


  def dump_player_pickle(self):
    with open("../pickle/" + self.pkl_file, "wb") as output_file:
      pickle.dump(self.players, output_file, pickle.HIGHEST_PROTOCOL)


  def reset(self):
    for p in self.players.values():
      p.reset()

    self.dump_player_pickle()


