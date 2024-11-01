from collections import Counter
def solution(nums):
    lst = list(set(nums))
    answer = len(lst)
    if len(lst) > len(nums) // 2:
        answer = len(nums) // 2
    return answer