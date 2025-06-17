import random
from art import logo

comp_number = random.randint(1, 100)

easy_num = 10
hard_num = 5

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
user_ask = input("Choose a difficulty. Type 'easy' or 'hard': ")

if user_ask == "easy":
    attempts = easy_num
else:
    attempts = hard_num

print(f"You have {attempts} attempts remaining to guess the number.")

user_ans = None

while attempts > 0:
    user_ans = int(input("Make a guess: "))
    
    if user_ans > comp_number:
        print("Too high.")
    elif user_ans < comp_number:
        print("Too low.")
    else:
        print(f"You got it! The answer was {comp_number}.")
        break
    
    attempts -= 1
    if attempts > 0:
        print(f"You have {attempts} attempts remaining. Guess again.")
    else:
        print(f"You've run out of attempts. The correct answer was {comp_number}.")
