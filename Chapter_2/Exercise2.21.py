amount = eval(input('Enter the monthly saving amount: '))
x = (1 + 0.00417)
firstAmount = amount
amount = amount * x
amount = (firstAmount + amount) * x
amount = (firstAmount + amount) * x
amount = (firstAmount + amount) * x
amount = (firstAmount + amount) * x
amount = (firstAmount + amount) * x
amount = int(amount * 100) / 100.0
print('After the sixth month, the account value is', amount)


