def display_question(question, options):
    print("\n" + question)
    for idx, option in enumerate(options):
        print(f"{idx + 1}. {option}")

def get_user_answer():
    while True:
        try:
            answer = int(input("Enter the number of your choice: "))
            if answer in [1, 2, 3, 4]:
                return answer - 1
            else:
                print("Invalid choice. Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    questions = [
        {"question": "Choose correct spelling ?", "options": ["Compoter", "Computer", "Compotar", "Compurt"], "correct": 1},
        {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "correct": 1},
        {"question": "What is capital of India?", "options": ["New Delhi", "lacknow", "Mumbai","Uttar Pradesh"], "correct": 0},
        {"question": "Who was the first Prime Minister of India?", "options": ["Chandrashekhar Ajad", "Bhimrav", "Pandit Jawahar lal Neharu","Bhagat Singh"], "correct": 2},
        {"question": "What is full form of CPU?", "options": ["Graphical User Interface", "Central Prossing Unit", "Central Problem Unit","Central Progress Unit"], "correct": 1},
        {"question": "What is cube of 9?", "options": ["792", "729", "739","749"], "correct": 1},
        {"question": "How many vowel in Hindi alphabet?", "options": ["9", "10", "11","12"], "correct": 2},
        {"question": "How many vowel in English alphabet?", "options": ["4", "5", "6","7"], "correct": 1},
        {"question": "How many colour in our national flag?", "options": ["2", "5", "3","4"], "correct": 2},
        {"question": "What is national animal?", "options": ["Camel", "lion", "Tiger","Hourse"], "correct": 2},
    ]
    
    print("Welcome to Rohan Quiz!")
    
    for q in questions:
        display_question(q["question"], q["options"])
        user_answer = get_user_answer()
        
        if user_answer == q["correct"]:
            print("Correct!")
        else:
            print("Incorrect. The correct answer was:", q["options"][q["correct"]])
            break
    else:
        print("Congratulations! You've answered all questions correctly!")

if __name__ == "__main__":
    main()

