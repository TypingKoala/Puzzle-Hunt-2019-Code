question = input('Input: ')
leftnum = int(question[0:2])
operation = question[2]
rightnum = int(question[3:5])

if operation == '+':
    answer = leftnum + rightnum
elif operation == '-':
    answer = leftnum - rightnum
elif operation == '*':
    answer = leftnum * rightnum
elif operation == '/':
    answer = leftnum / rightnum

print('Output: ' + str(answer))