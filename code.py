import random
import time

operators = ['+', '-', '*']
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 0

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operation = random.choice(operators)
    expression = str(left) + " " + operation + " " + str(right)
    result = eval(expression)
    return expression, result

WRONG = 0
input("Press enter to start")
TOTAL_PROBLEMS = int(input("How many problems you want to try?"))
print("Test Started ALL THE BEST!!")
print("**************************")

start = time.time()
for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    guess = input("Problem #" + str(i + 1) + ":" + expr + " = ")
    if guess == str(answer):
        print("Answered Correctly, done with testing")
        break
    print("Try and Try till you get right!")
    WRONG += 1

end_time = time.time()
total_time = end_time - start

print("You answered wrongly", WRONG, "questions")
print("Keep UP the good work, you finished in", total_time, "seconds!")
print("**************************")
