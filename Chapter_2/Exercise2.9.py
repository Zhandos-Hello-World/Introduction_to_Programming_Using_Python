fahrenheit = eval(input('Enter the temperature in Fahrenheit between -58 and 41: '))
speed = eval(input('Enter the wind speed in miles per hour: '))

wind_chill = 35.74 + (0.6215 * fahrenheit) - 35.75 * (speed ** 0.16) + 0.4275 * fahrenheit * (speed ** .16)
wind_chill = int(round(wind_chill * 100000)) / 100000.0
print('The wind chill index is', wind_chill)