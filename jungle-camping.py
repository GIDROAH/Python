noises = (input(""))
n = noises.split()
result =[]
i =len(n)
for i in n:
    if i == ' ' :
        result.append(i)
    elif i == 'Grr':
        result.append('Lion')
    elif i == 'Rawr':
        result.append('Tiger')
    elif i == 'Ssss':
        result.append('Snake')
    elif i == 'Chirp':
        result.append('Bird')
print((' ').join(result))