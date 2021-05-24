investmentAmount = eval(input('Enter final account value: '))
monthlyInterestRate = eval(input('Enter annual interest rate in percent: ')) / 1200.0
numberOfMonth = eval(input('Enter number of years:  ')) * 12
initialDepositAmount = investmentAmount * ((1 + monthlyInterestRate) ** numberOfMonth)
initialDepositAmount = int(initialDepositAmount * 100) / 100.0
print('Initial deposit value is ', initialDepositAmount)
