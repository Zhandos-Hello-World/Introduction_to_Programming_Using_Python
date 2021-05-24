balance, annualInterestRate = eval(input('Enter balance and interest rate (e.g., 3 for 3%): '))
interest = balance * (annualInterestRate / 1200)
interest = int(round(interest * 100000)) / 100000.0
print('The interest is', interest)