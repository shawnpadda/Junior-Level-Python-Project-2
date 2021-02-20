# Listing 5.4 - Subtraction Quiz Loop
import random
import time

# Count the number of correct answers
correctCount = 0

# Count thr number of questions
count = 0

# Constant
NUMBER_OF_QUESTIONS = 5

# Get start time
startTime = time.time()

while count < NUMBER_OF_QUESTIONS:
    number1 = random.randint(0, 9)
    number2 = random.randint(0, 9)

    # if number1 < number 2, swap number1 with number2
    if number1 < number2:
        number1, number2 = number2, number1

    # Prompt the student to answer  " what is number1 - number2 ?"
    answer = eval(input(" What is " + str(number1) + " - " + str(number2) + " ? "))

    # Grade the answer and display the result
    if number1 - number2 == answer:
        print("You are correct!")
        correctCount += 1
    else:
        print("Your answer is wrong. \n ", number1, "-", number2, "is", number1 - number2)

    # Increase the count
    count += 1

# Get end time
endTime = time.time()

# Get test time
testTime = int(endTime - startTime)

# Display results
print("Correct count is", correctCount, "out of", NUMBER_OF_QUESTIONS, "\n Test time is", testTime, "Seconds")

