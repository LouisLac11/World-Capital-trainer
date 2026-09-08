
def calculate_percentage(correct_answers, total_questions):
    percentage = (correct_answers / total_questions) * 100
    return percentage


def performance_message(percentage):
    if percentage >= 80:
        message = "Excellent work!"
    elif percentage >= 60:
        message = "Good job!"
    else:
        message = "Keep practicing!"

    return message


def tests():
    print("Testing calculate_percentage:")
    print(calculate_percentage(8, 10))

    print("Testing performance_message:")
    print(performance_message(80))


def menu():
    print("World Capitals Trainer")
    print("1. Calculate a score")
    print("2. Run tests")
    print("3. Exit")

    option = int(input("Select an option: "))
    return option


def main():
    option = menu()

    if option == 1:
        correct_answers = int(
            input("Enter the number of correct answers: ")
        )

        total_questions = int(
            input("Enter the total number of questions: ")
        )

        if total_questions > 0:
            percentage = calculate_percentage(
                correct_answers,
                total_questions
            )

            message = performance_message(percentage)

            print("Final score:", percentage, "%")
            print(message)
        else:
            print("The total number of questions must be greater than 0.")

    elif option == 2:
        tests()

    elif option == 3:
        print("Goodbye!")

    else:
        print("Invalid option.")


main()