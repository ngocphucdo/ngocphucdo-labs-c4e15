# from function_ex import randint
import function_ex

from random import randint, choice


# import random

a = randint(1, 10)
b = randint(1, 10)
error = randint (-1, 1)
true_result = 0

list = ['+','-','*', '/']
operation = choice(list)

true_result = function_ex.eval(a, b, operation)

result = true_result + error

print("{0} {1} {2} = {3}".format(a, operation, b, result))

user_choice = input("y/n :")
if true_result == result:
    if user_choice == 'y' :
        print("Bingo")
    else:
        print("Noob")
else:
    if user_choice == 'y':
        print("Noob")
    else:
        print("Bingo")
