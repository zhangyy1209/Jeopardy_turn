import json

class Question():
  def __init__(self, qid, content, answer, score, choices, choice_states, state=0):
    """
    Question class:
      qid: question id, int
      content: string
      answer: choice id, int
      score: int
      choices: string array
      choice_states: int array, 0: unselected, 1: selected
      state: int, 0: initial, 1: in answer, 2: finished
    """

    self.qid = qid
    self.content = content
    self.answer = answer
    self.score = score
    self.choices = choices
    self.choice_states = choice_states
    self.state = state


  def show(self):
    """
    Output a json file that contains the contents of the question.
    """

    pass


  def reset(self):
    """
    Reset a question.
    """

    pass


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
    self.load_questions(question_file)


  def load_questions(self):
    """
    Load questions.
    """
    with open(question_file) as quesitons:
      question_tmp = json.load(quesitons)


  def find(self, question_id):
    """
    return the question object.
    """
    pass


  def update_question_file(self, filename):
    """
    Write updated questions to file.
    """
    pass



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


  def answer(self, question_id, choice_id):
    question = question_list.find(question_id)
    score = question.update_choice_state(choice_id)
    self.update_score(score)

    if score < 0:
      # wrong answer
      pass
    else:
      # correct answer
      pass


  def update_score(self, score):
    self.score += score


class PlayerList():
  def __init__(self, n_player=4, player_file):
    """
    player list
    """
    self.players = {}
    self.n_player = n_player
    self.player_file = player_file


  def load_players(self):
    pass


  def update_player(self, player, score):
    pass


  def update_player_file(self):
    pass


