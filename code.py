import random
import time

operators=['+','-','*']
min_operand=3
max_operand=12
total_problems=0

def generate_problem():
    left=random.randint(min_operand,max_operand)
    right=random.randint(min_operand,max_operand)
    operation=random.choice(operators)
    
    expr=str(left)+" "+operation+" "+str(right)
    answer=eval(expr)
    return expr,answer
    
wrong=0
input("Press enter to start")
total_problems=int(input("How many problems you want to try?"))
print("Test Started ALL THE BEST!!")
print("**************************")

start=time.time()
for i in range(total_problems):
    expr,answer=generate_problem()
    guess=input("Problem #"+str(i+1)+":"+expr+" = ")
    if(guess==str(answer)):
        print("Answered Correctly, done with testing")
        break
    else:
        print("Try and Try till you get right!")
        wrong+=1
          
end_time=time.time()
total_time=end_time-start

print("You answered wrongly",wrong,"questions")
print("Keep UP the good work, you finished in",total_time,"seconds!")
print("**************************")