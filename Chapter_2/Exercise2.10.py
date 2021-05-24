speed, acceleration = eval(input("Enter speed and acceleration: "))
length = (speed ** 2) / (2 * acceleration)
length = int(round(length * 1000)) / 1000.0
print('The minimum runway length for this airplane is', length, 'meters')