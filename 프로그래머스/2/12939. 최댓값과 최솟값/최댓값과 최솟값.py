def solution(s):
    answer = ''
    arr = s.split(' ')
    nums = []
    for item in arr:
        nums.append(int(item))
    answer += str(min(nums))
    answer += ' '
    answer += str(max(nums))
    return answer