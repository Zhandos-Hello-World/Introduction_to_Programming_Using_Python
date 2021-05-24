v0, v1, t = eval(input('Enter v0, v1, and t: '))
a = (v1 - v0) / t
a = int(round(a * 10000)) / 10000.0
print('The average acceleration is', a)