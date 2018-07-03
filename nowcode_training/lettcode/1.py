#!/usr/bin/env python2.7

def find(target, array):
    # if target >= array[0][len(array)-1]:
    #     for i in range(len(array)):
    #         if array[i][len(array)-1] == target:
    #             return 'true'
    #         continue
    #     return 'false'
    # else:
    #     for i in range(0,len(array[0])-1):
    #         if target>=array[0][i] and target <array[0][i+1]:
    #         #val = i
    #             for x in range(0, len(array)):
    #                 if array[x][i] == target:
    #                     return 'true'
    #                 continue
    #             return 'false'

    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == target:
                return 'true'
        continue
    return 'false'




list1 = [1,2,8,9]
list2 = [2,4,9,12]
list3 = [4,7,10,13]
list4 = [6,8,11,15]
array = [list1, list2, list3, list4]

print find(11, array)
