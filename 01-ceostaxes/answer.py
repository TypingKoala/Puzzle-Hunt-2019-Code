income = int(input('Hi there, Mr. CEO. You are the best boss ever. What was your income in 2018? '))
monthsLate = int(input('How late do you expect to pay your taxes (in months)? '))

taxesOwed = income*.315*(1+.01)**monthsLate

print('You will owe $' + str(taxesOwed) + ' if you pay your taxes on $' + str(income) + ' ' + str(monthsLate) + ' months late.') 