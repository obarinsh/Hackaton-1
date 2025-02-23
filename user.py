import random
from project import get_wiktionary_words
from termcolor import colored


def choose_level():
    try:
        difficulty_level = int(
            input('Choose difficulty (1-5): 1 is the easiest, 5 is the most difficult:'))
        if difficulty_level < 1 or difficulty_level > 5:
            print("Invalid choice. Please enter a number between 1 and 5.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        return None
    return difficulty_level


def choose_category():
    categories = {'Food', 'Clothes', 'Nature'}
    category_input = input(
        "Choose a category - 'F' for Food, 'C' for Clothes, 'N' for Nature: ").strip().upper()
    category_map = {
        'F': 'Food',
        'C': 'Clothes',
        'N': 'Nature'
    }
    category = category_map.get(category_input)

    if category in categories:
        print(f"You selected: {category}")
        return category
    else:
        print("Invalid choice. Please enter 'F', 'C', or 'N'.")
        return choose_category()


def get_user_association(word):

    if word:
        word_id, portuguese_word, english_word, phonetic = word
        print(
            f"Enter an association for the word: {portuguese_word} ({english_word})")
        user_input = input("Your association: ")

        return user_input
    else:
        print("No more words left to associate!")
        return None, None


def quiz(user_association, word):
    wrong_answer = get_wiktionary_words()
    if word:
        word_id, portuguese_word, english_word, phonetic = word
        print('----------------------------------------')
        print(f'Translate the word {english_word}.')
        print(f'Your association is: {user_association}')
        print("Please choose the correct answer:")
        options = [(portuguese_word,  'Correct'), (wrong_answer, 'Wrong')]
        random.shuffle(options)
        for i, (word, _) in enumerate(options, start=1):
            print(f"{i}. {word}")
        user_answer = int(input("To choose, press the number(1 or 2): "))
        selected_word, correctness = options[user_answer - 1]

        if correctness == "Correct":
            print(colored("Correct!", "green"))
        else:
            print(
                colored(f"Wrong! The correct answer was: {portuguese_word}", 'red'))
