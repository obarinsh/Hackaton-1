from db_connect import get_connection

import requests


def is_portuguese(word):
    portuguese_chars = "abcdefghijklmnopqrstuvwxyzáàâãéèêíìîóòôõúùûç"
    return all(char.lower() in portuguese_chars for char in word)


def get_wiktionary_words():
    url = "https://pt.wiktionary.org/w/api.php?action=query&list=random&rnnamespace=0&format=json"

    response = requests.get(url)
    if response.status_code == 200:
        random_word = response.json().get("query", {}).get(
            "random", [{}])[0].get("title", "")
        if is_portuguese(random_word):
            return random_word
        else:
            return get_wiktionary_words()
    else:
        print("Error:", response.status_code, response.text)
        return None


def get_random_words(difficulty_level, category, amount_of_words):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        category = category.capitalize()
        cursor.execute(
            "SELECT word_id, portuguese_word, english_word, phonetic FROM vocabulary_noun WHERE difficulty_level = %s AND category=%s AND association IS NULL ORDER BY RANDOM() LIMIT %s;",
            (difficulty_level, category, amount_of_words)
        )
        random_words = cursor.fetchall()

        cursor.close()
        connection.close()

        if random_words:
            return random_words
        else:
            print("No words found for difficulty:",
                  difficulty_level, "and category:", category)
            return None

    except Exception as e:
        print("Error:", e)
        return None


# print(show_association(user_accociation, word))


# def restart_game():
#     try:
#         connection = get_connection()
#         cursor = connection.cursor()
#         cursor.execute('UPDATE vocabulary_noun SET association = NULL')
#         connection.commit()
#         print('Game reset: All associations cleared')

#     except Exception as e:
#         print('Error:', e)
#         connection.rollback()

#     finally:
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()
