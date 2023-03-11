import random
import time

correctCount = 0
count = 0
numberOfQuestions = 7
startTime = time.time()
while count < numberOfQuestions:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    if num1 < num2 :
        num1, num2 = num2, num1
    ans = eval(input(f"what is {num1} - {num2} ?: "))
    if num1 - num2 == ans:
        print("corret answer")
        correctCount +=1
    else:
        print("wrong answer")
    count +=1
endTime = time.time()
timeUsed = endTime - startTime

print(f"For {correctCount} questions you scored {correctCount} out of {numberOfQuestions} \
\
in {round(timeUsed)} seconds")