import random

# Coding quiz questions
questions = [
    {
        "question": "What does print() do in Python?",
        "options": ["1. Takes input from user", "2. Displays output on screen", "3. Adds numbers", "4. Deletes a file"],
        "answer": "2"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["1. //", "2. #", "3. /* */", "4. $$"],
        "answer": "2"
    },
    {
        "question": "What is the correct way to create a variable in Python?",
        "options": ["1. 1var = 10", "2. var1 = 10", "3. var-1 = 10", "4. var 1 = 10"],
        "answer": "2"
    },
    {
        "question": "Which of these is a loop in Python?",
        "options": ["1. if", "2. for", "3. def", "4. print"],
        "answer": "2"
    },
    {
        "question": "What does len('Hello') return?",
        "options": ["1. 4", "2. 5", "3. 6", "4. 0"],
        "answer": "2"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["1. func", "2. define", "3. def", "4. function"],
        "answer": "3"
    },
    {
        "question": "Which of these is a Python data type?",
        "options": ["1. int", "2. float", "3. string", "4. All of the above"],
        "answer": "4"
    },
    {
        "question": "What will 5 // 2 return in Python?",
        "options": ["1. 2.5", "2. 2", "3. 3", "4. Error"],
        "answer": "2"
    },
    {
        "question": "Which operator is used for multiplication in Python?",
        "options": ["1. +", "2. *", "3. x", "4. %"],
        "answer": "2"
    },
    {
        "question": "Which of these is correct to take input from user in Python?",
        "options": ["1. input()", "2. scanf()", "3. cin >>", "4. read()"],
        "answer": "1"
    }
]

# Shuffle questions
random.shuffle(questions)

score = 0

# Quiz loop
for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    
    user_answer = input("Enter the number of your answer: ")
    
    if user_answer == q["answer"]:
        print("Correct! ✅")
        score += 1
    else:
        print("Wrong! ❌ The correct answer was option", q["answer"])

print("\nYour final score is:", score, "out of", len(questions))