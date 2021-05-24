pounds = 0.45359237 * eval(input('Enter weight in pounds:'))
height = 0.0254 * eval(input('Enter height in inches: '))
BMI = pounds / (height ** 2)
BMI = int(round(BMI * 10000)) / 10000.0
print('BMI is ', BMI)