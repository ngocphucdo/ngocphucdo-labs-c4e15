from random import randint

a = randint(1, 10)
b = randint(1 ,10)

true_result = a + b
erorr = randint (-1, 1)
result = true_result + erorr
print('{0} + {1} = {2}'.format(a, b, result))

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
