sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
d = {}
for x in sample_list:
    d[x]=0
for x in sample_list:
    d[x]+=1
print(d)