x = int(input("x : "))
operation = input("opp :")
y = int(input("y :"))

result = 0

if operation == '+':
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '*':
    result = x * y
elif operation =='/' :
    result = x / y

print("{0} {1} {2} = {3}".format(x, operation, y, result))
