user_string = input('Enter a string: ')
frequency = {}

# couting the number of letters and store it in a dictionary
for _ in user_string:
    frequency[_] = user_string.count(_)

# sorting a dictionary bu its values and
frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))
for k,v in frequency.items():
    print(k, v)