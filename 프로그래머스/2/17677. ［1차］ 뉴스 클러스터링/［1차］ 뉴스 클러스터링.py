import math
def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    arr1 = list(str1)
    arr2 = list(str2)
    str_arr1 = []
    str_arr2 = []
    set1 = []
    set2 = []
    start = 0
    end   = 1
    
    for i in range(len(arr1)):
        tmp = ''
        if start < len(arr1) and end < len(arr1):
            tmp = arr1[start]+arr1[end]
            if tmp.isalpha():
                set1.append(tmp)
            start+=1
            end+=1
            
    start = 0
    end   = 1
    for i in range(len(arr2)):
        tmp = ''
        if start < len(arr2) and end < len(arr2):
            tmp = arr2[start]+arr2[end]
            if tmp.isalpha():
                set2.append(tmp)
            start+=1
            end+=1
            
    if len(set1) == 0 and len(set2) == 0:
        answer = 65536
    else:
        a_tmp = set1.copy()
        a_res = set1.copy()
        for i in set2:
            if i not in a_tmp:
                a_res.append(i)
            else:
                a_tmp.remove(i)
        result = []
        for i in set2:
            if i in set1:
                set1.remove(i)
                result.append(i)
                
        answer = ( len(result) / len(a_res) ) * 65536
    answer = math.floor(answer)
    return answer