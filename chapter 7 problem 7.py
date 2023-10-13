student_answers = ['A', 'C', 'B', 'A', 'D', 'D', 'C', 'A', 'C', 'A', 'D', 'A', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
correct_answers = ["A", "C", "A", "A", "D", "B", "C", "A", "C", "B", "A", "D", "C", "A", "D", "C", "B", "B", "D", "A"]
try:
    with open('student_answers.txt', 'w') as file:
        student_answers = file.write('student_answers.txt',)
except FileNotFoundError:
    print("Yo, that file you were looking for of 'student_answers.txt', it ain't there brotha. ")
    exit(1)
number_correct = 0
number_incorrect = 0
incorrect_questions = []
for question_num, (correct, student) in enumerate(zip(int(correct_answers, student_answers)), 1):
    if correct == student:
        number_correct += 1
    else:
        number_incorrect += 1
        incorrect_questions.append(question_num)
in_order_to_pass = 15
if number_correct >= in_order_to_pass:
    result = '\n''CONGRATS!!!! GO GET YOUR VROOM VROOM. ' 
else:
    result = '\n''yeah bro today was not your day but come back soon alright? '
print('Your result is: ', result)
print('Your total questions right is: ', number_correct)
print('Your total questions wrong is: ', number_incorrect)
print('The questins you got wrong were:', incorrect_questions)