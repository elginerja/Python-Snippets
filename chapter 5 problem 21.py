import random
def get_computer_choice():
    choice = random.randint(1,3)
    if choice == 1:
        return 'rock'
    if choice == 2:
        return 'paper'
    else:
        return 'scissors'
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie, so basically you lose!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win bucko. I'll get you next time!"
    else:
        return "Computer wins! Ha!"
while True:
    user_choice = input(' \n' 'Enter your choice (rock, paper, or scissors:) ')
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Yeah buddy you can't do that. Enter one of the three we said earlier. ")
        continue
    computer_choice = get_computer_choice()
    print("The computer's choice is: ", computer_choice )
    result = determine_winner(user_choice, computer_choice)
    print(result)
    play_again = input("Yo, wanna play again? (y/n): ")
    if play_again != 'y':
        break