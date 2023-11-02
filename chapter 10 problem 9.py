# File: <Chapter 10 problem 9>
# Description: <trivia game>
# Assignment Name and Number: chapter 10 problem 9
#
# Name: <John Jack Elginer>
# GitHub: <johnjack>
#
# On my honor, <Jack Elginer>, this programming assignment is my own work
# and I have not provided this code to any other student.
class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
    def get_question(self):
        return self.question
    def get_options(self):
        return self.options
    def get_correct_answer(self):
        return self.correct_answer
questions = [Question("What is Jack Elginer's favorite color?", ["1. red", "2. green", "3. blue", "4. purple"], 4),
    Question("What is Jack Elginer's favorite TV Show?", ["1. The Big Bang Theory", "2. South Park", "3. Family Guy", "4. The Flash"], 1),
    Question("How many games did Jack Elginer and Crespi soccer win last year?", ["1. six", "2. four", "3. one", "4. three"], 4),
    Question("What song is the worst song ever?", ["1. Old Town Road", "2. Baby Shark", "3. Tequilla", "4. Any Karen Carpenter song"], 4),
    Question("Who is the worst crespi teacher?", ["1. Ms. DeVine", "2. Timothy Bangford", "3. Mrs. Bonino", "4. Mrs. Last Year's French Teacher"], 2),
    Question("What is the best animated movie of all time?", ["1. Kung Fu Panda trilogy", "2. The Incredibles", "3. Cars", "4. Nightmare before Christmas"], 3),
    Question("How many times in the past eleven years have the Dodgers won their division?", ["1. seven ", "2. ten ", "3. six", "4. three"], 2),
    Question("And how many world series did they win?", ["1. two", "2. one", "3. zero", "4. three"], 2),
    Question("What color should an english notebook be?", ["1. purple", "2. who cares", "3. yellow", "4. red"], 3),
    Question("What animal is the cutest little thing?", ["1. penguin", "2. hedgehog", "3. cats", "4. dogs"], 1)]
def play_trivia_game(questions):
    player1_score = 0
    player2_score = 0
    for i in range(len(questions)):
        print(f"Question {i + 1}: {questions[i].get_question()}")
        for option in questions[i].get_options():
            print(option)
        player1_answer = int(input("Player 1, enter your answer (1-4 pls) here: "))
        player2_answer = int(input("Player 2, enter your answer (1-4 pls) here: "))
        if player1_answer == questions[i].get_correct_answer():
            player1_score += 1
        if player2_answer == questions[i].get_correct_answer():
            player2_score += 1
    print("\nYou finished the game. Let's see the results guys: ")
    print(f"\nPlayer 1 your score is: {player1_score}")
    print(f"\nPlayer 2 your score is: {player2_score}")
    if player1_score > player2_score:
        print("\nPlayer 1 wins! Congrats Player 1, you are smarter. ")
        print("Player 2 you are god awful. Go home and study before trying again.")
    elif player2_score > player1_score:
        print("\nPlayer 2 wins! You deserve a cookie for that win.")
        print("Player 1, I'm embarrased for you.")
    else:
        print("It's a tie! Y'all both sucked the exact same amount.")
play_trivia_game(questions)





