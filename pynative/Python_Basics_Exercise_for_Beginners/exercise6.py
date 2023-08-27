def diversable5(l):
    # This function will return list of numbers divisable by 5.
    # Parameter l is input list which should contain numbers.
    return_list = []
    for x in l:
        if x%5==0 and x!=0: return_list.append(x)
    return return_list

list1 = [1, 6, 7, 50, 555, 0, 30]
print(diversable5(list1))