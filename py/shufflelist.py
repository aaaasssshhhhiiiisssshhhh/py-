from copy import deepcopy 
from random import randint
def shuffle_list(lst):
    temp_list = deepcopy(lst)
    m = len(temp_list)
    while(m):
        m -= 1
        i = randint (0, m)
        temp_list[m], temp_list[i] = temp_list[i], temp_list [m]
    return temp_list
nums = [1,2,3,4,5,6]
print("original list:", nums )
print("\n shuffle the elements of the said list :")
print (shuffle_list(nums))    

