def only_positive(x):
    if x<0: return 0
    else: return x

for x in range(10):
    print('Current Number ', x, 'Previous Number ', only_positive(x-1), 'Sum: ', x+only_positive(x-1))