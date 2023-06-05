from question_bank import generate_questions

class Game:
  def __init__(self):
    pass
  def game_start(self):
    is_playing = True
    questions = generate_questions()
    score = 0
    current_index = 0
    while(is_playing):
      current_question = questions['results'][current_index]['question']
      current_answer = questions['results'][current_index]['correct_answer']
      
      choices = questions['results'][current_index]['incorrect_answers']
      choices.append(current_answer)

      print(current_question)
      for choice in choices:
        print(choice)

      answer = input('What is the correct answer: \n')

      if answer.lower() == current_answer.lower():
        score+=score+1
        print(f'Correct! Your new score is {score}\n')
      elif answer.lower() == 'exit':
        is_playing = False
      else:
        print('Incorrect, better luck next time!\n')

      current_index += 1
      
      