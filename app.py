from user import get_user_association
from project import get_random_words
from user import choose_level
from user import choose_category
from user import quiz


def game():

    print('WELCOME TO THE FIRST INTERACTIVE LANGUAGE LEARNING GAME')
    category = choose_category()
    difficulty_level = (choose_level())

    quiz_list = []

    amount_of_words = 5
    words = get_random_words(difficulty_level, category, amount_of_words)
    print('NOW YOU WILL HAVE 5 WORD THAT YOU NEED TO ADD ASSOCIATION. AFTER THAT YOU NEED TO GUESS CORRECT PORTUGUES WORD')
    for word in words:
        user_association = get_user_association(word)
        quiz_list.append({
            "word": word,
            "association": user_association
        })

    for item in quiz_list:
        quiz(item["association"], item["word"])


game()
