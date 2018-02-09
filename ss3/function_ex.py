# parameter, argument
def eval(x, y, operation):

    result = 0

    if operation == '+':
        result = x + y
    elif operation == '-':
        result = x - y
    elif operation == '*':
        result = x * y
    elif operation =='/' :
        result = x / y

    return result

# x = int(input("x : "))
# operation = input("opp :")
# y = int(input("y :"))
#
r = eval(x, y, operation)

print(r)
