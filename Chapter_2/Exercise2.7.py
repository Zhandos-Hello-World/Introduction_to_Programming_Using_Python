minute = eval(input('Enter the number of minutes: '))
year = int(minute / (60 * 24 * 365))
days = int(minute / (60 * 24)) - (year * 365)
print(minute, 'minutes is approximately', year, 'years and', days, 'days')
