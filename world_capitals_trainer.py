"""World Capitals Trainer.

A geography quiz where the user types the capital of a country.
Questions are read from a file and the results are saved in another file.
"""

import random

CAPITALS_FILE = "capitals.txt"
HISTORY_FILE = "history.txt"
QUESTIONS_PER_GAME = 10


def normalize_text(text):
    """Return the text in lowercase, without accents or extra spaces.

    It is used to compare the user's answer with the correct capital.
    """
    accented = "áéíóúüñàèç"
    plain = "aeiouunaec"
    result = ""
    for character in text.strip().lower():
        position = accented.find(character)
        if position >= 0:
            result += plain[position]
        else:
            result += character
    return result


def read_questions(file_name, level):
    """Read the capitals file and return the questions of one level.

    Each line of the file has the format: level,country,capital1/capital2
    The result is a list of lists: [country, [valid capitals]].
    """
    questions = []
    file = open(file_name, "r")
    for line in file:
        parts = line.strip().split(",")
        if len(parts) == 3 and parts[0] == level:
            valid_capitals = parts[2].split("/")
            questions.append([parts[1], valid_capitals])
    file.close()
    return questions


def choose_level():
    """Ask the user for a difficulty level until a valid one is typed.

    Returns the level as a string: "easy", "medium" or "hard".
    """
    print("Choose a difficulty level:")
    print("1. Easy   (well-known countries)")
    print("2. Medium (less familiar countries)")
    print("3. Hard   (challenging countries)")
    while True:
        option = input("Your choice (1, 2 or 3): ").strip().lower()
        if option == "1" or option == "easy":
            return "easy"
        elif option == "2" or option == "medium":
            return "medium"
        elif option == "3" or option == "hard":
            return "hard"
        print("Invalid option, please try again.")


def ask_question(country, valid_capitals):
    """Ask for the capital of a country and check the user's answer.

    Returns True if the answer is correct, otherwise it returns False.
    """
    answer = input("What is the capital of " + country + "? ")
    answer = normalize_text(answer)
    for capital in valid_capitals:
        if answer == normalize_text(capital):
            print("Correct!")
            return True
    print("Wrong. The correct answer is " + valid_capitals[0] + ".")
    return False


def play_quiz(questions):
    """Run the quiz with a random selection of questions.

    Returns the number of correct answers.
    """
    random.shuffle(questions)
    total = min(QUESTIONS_PER_GAME, len(questions))
    score = 0
    for i in range(total):
        print()
        print("Question " + str(i + 1) + " of " + str(total))
        if ask_question(questions[i][0], questions[i][1]):
            score += 1
    return score


def get_final_message(percentage):
    """Return a closing message that depends on the percentage."""
    if percentage >= 90:
        return "Excellent work! You possess a solid understanding of " \
            "world capitals."
    elif percentage >= 70:
        return "Great job! You know many capitals, keep practicing."
    elif percentage >= 50:
        return "Not bad! With a little more practice you will improve."
    return "Keep studying! Try again and you will do better."


def save_result(level, score, total):
    """Add the result of a game to the history file.

    Each line has the format: level,score,total,percentage
    """
    percentage = score * 100 / total
    file = open(HISTORY_FILE, "a")
    file.write(level + "," + str(score) + "," + str(total) + ","
               + str(round(percentage, 1)) + "\n")
    file.close()


def show_history(level):
    """Show how many games were played in a level and the best result.

    It reads the history file, which is created empty if it does not exist.
    """
    file = open(HISTORY_FILE, "a")
    file.close()
    games = 0
    best = 0.0
    file = open(HISTORY_FILE, "r")
    for line in file:
        parts = line.strip().split(",")
        if len(parts) == 4 and parts[0] == level:
            games += 1
            if float(parts[3]) > best:
                best = float(parts[3])
    file.close()
    if games == 0:
        print("This is your first game in this level. Good luck!")
    else:
        print("Games played in this level: " + str(games))
        print("Your best score: " + str(best) + "%")


def show_results(score, total):
    """Show the final score, the percentage and a closing message."""
    percentage = score * 100 / total
    print()
    print("Quiz finished!")
    print("Correct answers: " + str(score))
    print("Total questions: " + str(total))
    print("Final Score: " + str(score) + "/" + str(total) + " - "
          + str(round(percentage)) + "%")
    print(get_final_message(percentage))


def main():
    """Show the welcome message and control the whole program."""
    print("=== WORLD CAPITALS TRAINER ===")
    print("Test your knowledge of countries and their capitals.")
    print("Type the capital of each country. Accents are optional.")
    print()
    play_again = "yes"
    while play_again == "yes":
        level = choose_level()
        show_history(level)
        questions = read_questions(CAPITALS_FILE, level)
        score = play_quiz(questions)
        total = min(QUESTIONS_PER_GAME, len(questions))
        show_results(score, total)
        save_result(level, score, total)
        print()
        play_again = input("Do you want to play again? (yes/no): ")
        play_again = play_again.strip().lower()
    print("Thanks for playing. Goodbye!")


main()
