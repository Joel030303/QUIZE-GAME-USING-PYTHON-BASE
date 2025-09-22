import random
import threading
import time

# Questions and answers dictionary
questions = {
    "What is the capital of France?": "paris",
    "What is the largest planet in our solar system?": "jupiter",
    "What is the chemical symbol for gold?": "au",
    "In which year did World War II end?": "1945",
    "What is the square root of 64?": "8",
    "Who wrote 'To Kill a Mockingbird'?": "harper lee",
    "Which organ pumps blood through the body?": "heart",
    "What is the freezing point of water in Celsius?": "0",
    "Which continent is the Sahara Desert located in?": "africa",
    "What is the tallest mountain in the world?": "mount everest"
}

# Configuration
TIME_LIMIT=10
MAX_ATTEMPTS=3

def display_welcome():
    print("Welcome to the Python Quiz Game!")
    print("Rules:")
    print(f"You have {TIME_LIMIT} seconds to answer each question.")
    print(f"You have a maximum of {MAX_ATTEMPTS} attempts per question.")
    print("Answers are case-insensitive.")
    print("No negative marking for incorrect answers.\n")

def ask_question(question, answer):
    attempts=0
    while attempts<MAX_ATTEMPTS:
        timer=threading.Timer(TIME_LIMIT, print, ["\nTime's up!"])
        timer.start()
        try:
            user_input=input(f"{question}\nYour answer: ").strip().lower()
            timer.cancel()
            if user_input==answer:
                print("Correct!\n")
                return True
            else:
                attempts+=1
                print(f"Incorrect. Attempts left: {MAX_ATTEMPTS - attempts}\n")
        except Exception as e:
            timer.cancel()
            print(f"An error occurred: {e}")
            return False
    print(f"The correct answer was: {answer}\n")
    return False

def run_quiz():
    display_welcome()
    score=0
    question_items=list(questions.items())
    random.shuffle(question_items)
    for question, answer in question_items:
        if ask_question(question, answer):
            score += 1
    print(f"Quiz completed! Your score: {score}/{len(questions)}")
    if score == len(questions):
        print("Perfect score! Excellent work!")
    elif score >= len(questions) * 0.7:
        print("Good job! You have a solid understanding.")
    else:
        print("Needs improvement. Keep practicing!")

if __name__ == "__main__":
    run_quiz()