def check_list(l):
    #This function check if first and last element of list is the same. Function return True or False
    if l[0] == l[len(l)-1]: return True
    else: return False

def check_list_v2(l):
    #This function check if first and last element of list is the same. Function return True or False
    if l[0] == l[-1]: return True
    else: return False

list1 = [1,3,1]
list2 = [9,3,5,6,7,1]
print(check_list(list1))
print(check_list(list2))
print(check_list_v2(list1))
print(check_list_v2(list2))
