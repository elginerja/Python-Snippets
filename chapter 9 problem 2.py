# File: <Chapter 9 problem 2>
# Description: <state capitals and a quiz for them>
# Assignment Name and Number: chapter 9 problem 2
#
# Name: <John Jack Elginer>
# GitHub: <johnjack>
#
# On my honor, <Jack Elginer>, this programming assignment is my own work
# and I have not provided this code to any other student.
import random
capitals_quiz ={}
state_capitals = {"Alabama": "Montgomery", "Alaska": "Jeanaeu", "Arizona": "Pheonix", "Arkansas": "Little Rock", "California": "Sacramento","Colorado": "Denver",
                "Connecticut": "Hartford","Delaware": "Dover","Florida": "Tallahassee","Georgia": "Atlanta","Hawaii": "Honolulu", "Idaho": "Boise",
                "Illinois": "Springfield","Indiana": "Indianapolis","Iowa": "Des Moines","Kansas": "Topeka","Kentucky": "Frankfort",
                "Louisiana": "Baton Rouge","Maine": "Augusta", "Maryland": "Annapolis", "Massachusetts": "Boston", "Michigan": "Lansing", "Minnesota": "St. Paul", "Mississippi": "Jackson",
                "Missouri": "Jefferson City","Montana": "Helena", "Nebraska": "Lincoln", "Nevada": "Carson City", "New Hampshire": "Concord",
                "New Jersey": "Trenton","New Mexico": "Santa Fe", "New York": "Albany","North Carolina": "Raleigh", "North Dakota": "Bismarck",
                "Ohio": "Columbus", "Oklahoma": "Oklahoma City", "Oregon": "Salem", "Pennsylvania": "Harrisburg","Rhode Island": "Providence",
                "South Carolina": "Columbia", "South Dakota": "Pierre", "Tennessee": "Nashville","Texas": "Austin", "Utah": "Salt Lake City",
                "Vermont": "Montpelier","Virginia": "Richmond", "Washington": "Olympia", "West Virginia": "Charleston", "Wisconsin": "Madison", "Wyoming": "Cheyenne"}
correct_count = 0
incorrect_count = 0
states_to_quiz = list(state_capitals.keys())
number_of_questions = 8
for num in range(number_of_questions):
    state = random.choice(states_to_quiz)
    correct_answer = state_capitals[state]
    print("\nWhat is the capital of", state, "? \n" )
    user_answer = input("Please enter the capital of said state: ")
    if user_answer == correct_answer:
        print("\nCorrect!! \n")
        correct_count += 1
    else:
        print("\nIncorrect!! \n")
        incorrect_count +=1
print("\nQuiz Complete! You got",correct_count, "correct and", incorrect_count, "incorrect.\n Good job dude!")
print(input('press any key to end: '))