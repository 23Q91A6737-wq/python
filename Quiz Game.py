# Python Quiz Game

# Python Quiz Game

Questions = ("How many elements are there in periodic table ? : ",
             "Which animal lays the largest eggs ? :",
             "What is the most abundant gas in Earth's atmosphere ? :",
             "How many bones are there in Human body ? : ",
             "Which planet in the solar system is the hottest ?: ")

Options = (("A. 116 ","B . 117","C. 118 ","D. 119 "),
           ("A. Whale ","B. Crocodile ","C. Elephant ","D. Ostrich "),
           ("A. Nitrogen ","B. Oxygen ","C. Carbon-Dioxide ","D. Hydrogen "),
           ("A. 206 ","B. 207 ","C. 208 ","D. 209 "),
           ("A. Mercury ","B. Venus ","C. Earth ","D. Mars "))

answers = ("C" , "D", "A", "A","B")

guesses = []

score = 0

question_num = 0

for question in Questions:
    print("\n-----------------------------------------")
    print(question)

    for option in Options[question_num]:
        print(option)

    guess = input("Enter (A,B,C,D) :").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        print("CORRECT")
        score +=1
    else:
        print("INCORRECT")
        print(f"The CORRECT Answer is {answers[question_num]}")

    question_num += 1

print("\n--------------------------------------------------------")
print("QUIZ COMPLETED")
print("\n--------------------------------------------------------")
print("answers : ", end= " ")
for answer in answers:
    print(answer , end =" ")
print()

print("guesses : ",end = " ")
for guess in guesses:
    print(guess, end = " ")

print()
#print("Your score is :",score,"/",len(Questions))

score = int(score/len(Questions)*100)
print(f"your score is : {score}%")

