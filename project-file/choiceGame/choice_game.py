from Questions import Question

question_prompts = [
          'What color are apples?\n(a) Red\Green\n(b) Purple\n(c) Orange\n\n',
          'What color are Bananas?\n(a) Teal\n(b) Magneta \n (c) Yellow\n\n',
          'What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n',
          'How many Days makes one Year?\n (a) 300 days\n(b) 363 days\n (c) 365 days\n\n'
]

questions = [
          Question(question_prompts[0], 'a'),
          Question(question_prompts[1], 'c'),
          Question(question_prompts[2], 'b'),
          Question(question_prompts[3], 'c')
          
]

def run_test(questions):
          score = 0
          for question in questions:
                    answer = input(question.prompt)
                    if answer == question.answer:
                              score +=1
          print('You got ' + str(score) + '/' + str(len(questions)) + 'correct')

run_test(questions)




