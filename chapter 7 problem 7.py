# File: <Chapter 7 problem 7>
# Description: <dmv numbers >
# Assignment Name and Number: chapter 7 problem 7
#
# Name: <John Jack Elginer>
# GitHub: <johnjack>
#
# On my honor, <Jack Elginer>, this programming assignment is my own work
# and I have not provided this code to any other student.
# i know this doesn't work but I am trying it anyway
print('\nIn this program, have the drivers test right next to you, you will type in the answers here.\nGood luck, you will need it. ')
correct_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B','A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
def main():
   student_answers = []
   for x in range(20):
      problem = input('\nFor this question, please enter the letter of your choice from your multiple choice sheet: "A", "B", "C","D": ')
      student_answers.append(problem)
   outfile = open('student_answerslist.txt', 'w')

   for item in student_answers:
     outfile.write(item + '\n')
    
   outfile.close()
main()
def main():
   print()
   infile = open('student_answerslist.txt', 'r')
   student_answers = infile.readlines()
   infile.close()
   index = 0
   answers_correct = 0
   answers_wrong = 0
   while index < len(student_answers):
      student_answers[index] = student_answers[index].rstrip('\n')
      if student_answers[index] == correct_answers[index]:
         answers_correct += 1
      if student_answers[index] != correct_answers[index]:
         answers_wrong += 1
      index += 1

   print('\nHere are your answers to the test my guy: ', student_answers)
   if answers_correct < 15:
      print("\nIm so sorry dude, you did not pass, because you got", answers_correct, "right and you got", answers_wrong, "wrong, and that is less than 15. ")
   if answers_correct >= 15:
      print("\nMy guy!!!!! you passed dude because you got", answers_correct, "right and you only have", answers_wrong, "wrong, and that is more than 15 correct. ")
   if answers_correct == 20:
      print('\nBRO. A PERFECT SCORE???? GOOD JOB DUDE!!!')
   if answers_correct ==0:
      print('\nDude, you didnt get any right. Go try again buckko. ')
   print()
main()