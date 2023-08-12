import random
import time

OPERATOR = [ "+" , "-" , "*" ]
TOTAL_PROBLEMS = int(input("Enter the number of problems you want to solve : "))
Min = int(input("\nEnter the Minimum number you can solve problem with : "))
Max = int(input("\nEnter the Maximum number you can solve problem with : "))
 
def generator():
    left = random.randint(Min,Max)
    right = random.randint(Min,Max)
    operator = random.choice(OPERATOR)
    exp = f" {left} {operator} {right}"
    answer = eval(exp)
    return exp , answer

wrong = 0

input("Press Enter to start ")
print("---------------------------------------")
# a =time.perf_counter()   You can use this also
start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    exp , answer = generator()
    while True:
        
        question = input(f"Ptoblem #{i+1} {exp} = ")
        if question == str(answer):
            break
        wrong += 1     
print(f"\nTotal wrong ans you gave {wrong}")

# b= time.perf_counter()      You can you use this also
end_time = time.time()
# print(b-a)
print(f"You took {round(end_time - start_time , 2)}sec to complete the problems\n")

print("Well done")
print("-----------------------------------------")