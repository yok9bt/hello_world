speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
s = set()
for x in speed:
    s.add(speed[x])

my_list = list(s)
print(my_list)