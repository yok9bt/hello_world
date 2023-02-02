list1 = [1,5,6,7,98,8,4,21,7,5,4,634]
list2 = [3,4,85,75,9,8,74,256,47,8,5,5]
list3 = []
for x in list1:
    if x%2!=0: list3.append(x)
for x in list2:
    if x%2==0: list3.append(x)
print(list3)