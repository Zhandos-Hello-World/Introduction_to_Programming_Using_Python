year = eval(input('Enter the number of years: '))
time = year * 3600 * 24 * 365
born = time / 7
death = time / 7
immigrant = time / 45
current_population = 312032486
population = born + immigrant - death
population += current_population
print('The population in', year, 'years is', int(population))