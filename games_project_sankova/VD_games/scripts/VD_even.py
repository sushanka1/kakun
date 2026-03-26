import random
from games_project_sankova.VD_games.cli import welcome_user

def is_even(number):
    """Проверяет, является ли число чётным"""
    return number % 2 == 0

def play_game():
    """Основная логика игры"""
    name = welcome_user()
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    
    correct_answers = 0
    rounds_to_win = 3
    
    while correct_answers < rounds_to_win:
        number = random.randint(1, 100)
        correct_answer = 'yes' if is_even(number) else 'no'
        
        print(f"Question: {number}")
        user_answer = input('Your answer: ')
        
        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")

def main():
    play_game()

if __name__ == '__main__':
    main()
