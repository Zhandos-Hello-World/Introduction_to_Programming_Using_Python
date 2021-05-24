subtotal = eval(input('Enter the subtotal and a gratuity rate: '))
gratuity = eval(input())
gratuity = (subtotal * (gratuity / 100))
subtotal += gratuity
subtotal = int(subtotal * 100) / 100.0
print('The gratuity is', gratuity, 'and the total is', subtotal)