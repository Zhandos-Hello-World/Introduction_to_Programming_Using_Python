finalAccountValue = eval(input('Enter final account value: '))
monthlyInterestRate = eval(input('Enter annual interest rate in percent: ')) / 1200.0
numberOfMonth = eval(input('Enter number of years:  ')) * 12
initialDepositAmount = finalAccountValue / ((1 + monthlyInterestRate) ** numberOfMonth)
print('Initial deposit value is ', initialDepositAmount)
