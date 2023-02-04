sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
new_list = []
[new_list.append(x) for x in sample_list if x not in new_list]
print(new_list)

t = tuple(new_list)
print(t)
print(min(t))
print(max(t))